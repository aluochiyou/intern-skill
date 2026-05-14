#!/usr/bin/env python3
"""Check local environment readiness for a project."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


TOOLS = ["git", "python", "python3", "pip", "node", "npm", "pnpm", "yarn", "docker", "docker compose", "gh", "make"]


def run(args: list[str], cwd: Path | None = None) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout.strip()


def tool_status(tool: str) -> dict:
    parts = tool.split()
    exe = shutil.which(parts[0])
    if not exe:
        return {"tool": tool, "available": False, "version": None}
    version_args = parts + ["--version"]
    code, output = run(version_args)
    return {"tool": tool, "available": code == 0, "version": output.splitlines()[0] if output else None}


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not repo.exists():
        print(f"Path does not exist: {repo}", file=sys.stderr)
        return 2

    files = {p.name for p in repo.iterdir()} if repo.is_dir() else set()
    tool_results = [tool_status(tool) for tool in TOOLS]
    warnings = []

    if ".env" in files:
        warnings.append(".env exists; do not publish or share it without review")
    if ".env.example" not in files and ".env" in files:
        warnings.append(".env.example is missing; consider adding a sanitized template")
    if "Dockerfile" in files and not any(item["tool"] == "docker" and item["available"] for item in tool_results):
        warnings.append("Dockerfile exists but docker command is unavailable")
    if "package.json" in files and not any(item["tool"] in {"npm", "pnpm", "yarn"} and item["available"] for item in tool_results):
        warnings.append("package.json exists but no Node package manager was found")
    if "requirements.txt" in files and not any(item["tool"] in {"pip", "python3"} and item["available"] for item in tool_results):
        warnings.append("requirements.txt exists but Python/pip tooling is incomplete")

    report = {
        "repo": str(repo),
        "tools": tool_results,
        "project_files": sorted(files),
        "warnings": warnings,
        "next": [
            "Run detect_stack.py to identify project commands",
            "Use README, Makefile, package scripts, or CI before inventing commands",
            "Resolve warnings before publishing or deployment",
        ],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
