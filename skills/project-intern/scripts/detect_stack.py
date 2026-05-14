#!/usr/bin/env python3
"""Lightweight repository stack and command detector."""

from __future__ import annotations

import json
import sys
from pathlib import Path


MANIFESTS = {
    "package.json": "Node.js / JavaScript / TypeScript",
    "pnpm-lock.yaml": "pnpm",
    "yarn.lock": "Yarn",
    "package-lock.json": "npm",
    "requirements.txt": "Python pip",
    "pyproject.toml": "Python pyproject",
    "poetry.lock": "Poetry",
    "uv.lock": "uv",
    "Pipfile": "Pipenv",
    "Cargo.toml": "Rust",
    "go.mod": "Go",
    "pom.xml": "Java Maven",
    "build.gradle": "Java/Gradle",
    "Dockerfile": "Docker",
    "docker-compose.yml": "Docker Compose",
    "compose.yml": "Docker Compose",
    "Makefile": "Make",
}

ENTRYPOINT_NAMES = {
    "main.py",
    "app.py",
    "server.py",
    "manage.py",
    "index.js",
    "server.js",
    "main.ts",
    "index.ts",
    "main.go",
    "main.rs",
}

TEST_DIR_NAMES = {"test", "tests", "__tests__", "spec", "e2e"}
IGNORE_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not repo.exists():
        print(f"Path does not exist: {repo}", file=sys.stderr)
        return 2

    found = []
    for path in repo.rglob("*"):
        rel = path.relative_to(repo)
        if set(rel.parts) & IGNORE_DIRS:
            continue
        if len(rel.parts) > 4:
            continue
        if path.is_file() and path.name in MANIFESTS:
            found.append({"file": str(rel), "name": path.name, "hint": MANIFESTS[path.name]})

    package_scripts = {}
    for item in found:
        if item["name"] == "package.json":
            package_json = repo / item["file"]
            scripts = read_json(package_json).get("scripts", {})
            if scripts:
                package_scripts[item["file"]] = scripts

    entrypoints = []
    test_paths = []
    for path in repo.rglob("*"):
        rel_parts = set(path.relative_to(repo).parts)
        if rel_parts & IGNORE_DIRS:
            continue
        if path.is_file() and path.name in ENTRYPOINT_NAMES:
            entrypoints.append(str(path.relative_to(repo)))
        if path.is_dir() and path.name in TEST_DIR_NAMES:
            test_paths.append(str(path.relative_to(repo)))

    hints = []
    names = {item["name"] for item in found}
    files_by_name = {}
    for item in found:
        files_by_name.setdefault(item["name"], []).append(item["file"])
    for package_file, scripts in package_scripts.items():
        package_dir = str(Path(package_file).parent)
        prefix = "." if package_dir == "." else package_dir
        sibling_names = {Path(item["file"]).name for item in found if str(Path(item["file"]).parent) == package_dir}
        manager = "pnpm" if "pnpm-lock.yaml" in sibling_names else "yarn" if "yarn.lock" in sibling_names else "npm"
        hints.append(f"Install ({prefix}): cd {prefix} && {manager} install")
        for key in ("dev", "start", "test", "build", "lint", "typecheck"):
            if key in scripts:
                hints.append(f"{key} ({prefix}): cd {prefix} && {manager} run {key}")
    for req in files_by_name.get("requirements.txt", []):
        req_dir = str(Path(req).parent)
        prefix = "." if req_dir == "." else req_dir
        hints.append(f"Install ({prefix}): cd {prefix} && python -m pip install -r requirements.txt")
    for pyproject in files_by_name.get("pyproject.toml", []):
        py_dir = str(Path(pyproject).parent)
        prefix = "." if py_dir == "." else py_dir
        hints.append(f"Inspect ({prefix}): pyproject.toml for build backend and tool commands")
    if "Makefile" in names:
        for makefile in files_by_name.get("Makefile", []):
            make_dir = str(Path(makefile).parent)
            prefix = "." if make_dir == "." else make_dir
            hints.append(f"Inspect ({prefix}): Makefile targets before inventing commands")
    if "Dockerfile" in names or "docker-compose.yml" in names or "compose.yml" in names:
        hints.append("Inspect Docker configuration before running containers")

    report = {
        "repo": str(repo),
        "manifests": found,
        "package_scripts": package_scripts,
        "entrypoints": sorted(entrypoints)[:50],
        "test_paths": sorted(set(test_paths))[:50],
        "command_hints": hints,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
