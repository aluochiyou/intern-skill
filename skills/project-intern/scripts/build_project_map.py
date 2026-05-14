#!/usr/bin/env python3
"""Generate a lightweight project map for learning and onboarding."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DETECT_STACK = SKILL_DIR / "scripts" / "detect_stack.py"
IGNORE_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".pytest_cache"}
DOC_NAMES = {"README.md", "README.rst", "README.txt", "CONTRIBUTING.md", "docs"}
CONFIG_SUFFIXES = {".toml", ".yaml", ".yml", ".json", ".ini", ".cfg"}


def run(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    return proc.returncode, proc.stdout.strip()


def stack_report(repo: Path) -> dict:
    code, output = run([sys.executable, str(DETECT_STACK), str(repo)])
    if code != 0:
        return {"error": output}
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"error": output}


def top_dirs(repo: Path) -> list[str]:
    result = []
    for path in sorted(repo.iterdir()):
        if path.is_dir() and path.name not in IGNORE_DIRS:
            count = sum(1 for child in path.rglob("*") if child.is_file() and not (set(child.parts) & IGNORE_DIRS))
            result.append(f"{path.name}/ ({count} files)")
    return result[:30]


def collect_files(repo: Path) -> tuple[list[str], list[str]]:
    docs = []
    configs = []
    for path in repo.rglob("*"):
        rel_parts = set(path.relative_to(repo).parts)
        if rel_parts & IGNORE_DIRS:
            continue
        if path.is_file():
            rel = str(path.relative_to(repo))
            if path.name in DOC_NAMES or rel.startswith("docs/"):
                docs.append(rel)
            if path.suffix in CONFIG_SUFFIXES or path.name in {"Dockerfile", "Makefile", ".env.example"}:
                configs.append(rel)
    return sorted(docs)[:50], sorted(configs)[:80]


def render(repo: Path, stack: dict, dirs: list[str], docs: list[str], configs: list[str]) -> str:
    entrypoints = stack.get("entrypoints", [])
    tests = stack.get("test_paths", [])
    manifests = [f"{item.get('file')} - {item.get('hint')}" for item in stack.get("manifests", [])]
    commands = stack.get("command_hints", [])

    def bullet(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- Not detected"

    return "\n".join(
        [
            "# Project Map",
            "",
            f"Project: `{repo}`",
            "",
            "## Detected Stack",
            bullet(manifests),
            "",
            "## Main Entrypoint Candidates",
            bullet(entrypoints),
            "",
            "## Test Path Candidates",
            bullet(tests),
            "",
            "## Top-Level Modules",
            bullet(dirs),
            "",
            "## Documentation",
            bullet(docs),
            "",
            "## Configuration",
            bullet(configs),
            "",
            "## Command Hints",
            bullet(commands),
            "",
            "## Suggested Learning Route",
            "- Read README and setup docs.",
            "- Open one entrypoint candidate.",
            "- Trace one user action or command into a core module.",
            "- Check tests for expected behavior.",
            "- Record must know / useful to know / skip for now.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--write", action="store_true", help="Write docs/intern/PROJECT_MAP.md")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not repo.exists():
        print(f"Path does not exist: {repo}", file=sys.stderr)
        return 2

    stack = stack_report(repo)
    docs, configs = collect_files(repo)
    content = render(repo, stack, top_dirs(repo), docs, configs)
    if args.write:
        out = repo / "docs" / "intern" / "PROJECT_MAP.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(str(out))
    else:
        print(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
