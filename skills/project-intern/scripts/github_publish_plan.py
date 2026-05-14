#!/usr/bin/env python3
"""Generate a dry-run GitHub publish readiness report for a local project."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


SECRET_OR_PRIVATE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "id_rsa",
    "id_ed25519",
    "credentials.json",
    "token.json",
    "cookies.txt",
}

GENERATED_OR_LARGE_DIRS = {
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "runs",
    "outputs",
    "mission_outputs",
}

LARGE_FILE_BYTES = 50 * 1024 * 1024


def run(repo: Path, args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout.strip()


def maybe_git(repo: Path, args: list[str]) -> str:
    code, output = run(repo, ["git", *args])
    return output if code == 0 else f"Unavailable: {output}"


def walk_warnings(repo: Path) -> tuple[list[str], list[str]]:
    sensitive = []
    large = []
    for path in repo.rglob("*"):
        rel_parts = set(path.relative_to(repo).parts)
        if ".git" in rel_parts:
            continue
        if path.name in SECRET_OR_PRIVATE_NAMES:
            sensitive.append(str(path.relative_to(repo)))
        if rel_parts & GENERATED_OR_LARGE_DIRS:
            sensitive.append(str(path.relative_to(repo)))
        if path.is_file():
            try:
                if path.stat().st_size >= LARGE_FILE_BYTES:
                    large.append(str(path.relative_to(repo)))
            except OSError:
                pass
    return sorted(set(sensitive))[:100], sorted(set(large))[:100]


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not repo.exists():
        print(f"Path does not exist: {repo}", file=sys.stderr)
        return 2

    is_git = (repo / ".git").exists()
    sensitive, large = walk_warnings(repo)
    has_gh = shutil.which("gh") is not None

    report = {
        "repo": str(repo),
        "is_git_repo": is_git,
        "branch": maybe_git(repo, ["branch", "--show-current"]) if is_git else None,
        "remotes": maybe_git(repo, ["remote", "-v"]) if is_git else None,
        "status": maybe_git(repo, ["status", "--short"]) if is_git else None,
        "has_readme": any((repo / name).exists() for name in ("README.md", "README.rst", "README.txt")),
        "has_gitignore": (repo / ".gitignore").exists(),
        "has_license": any((repo / name).exists() for name in ("LICENSE", "LICENSE.md", "COPYING")),
        "github_cli_available": has_gh,
        "possible_sensitive_or_generated_paths": sensitive,
        "large_files_over_50mb": large,
        "suggested_next_commands": [
            "git init" if not is_git else "git status --short",
            "git add <reviewed-files>",
            "git commit -m \"Initial project publish\"",
            "gh repo create OWNER/REPO --private --source . --remote origin --push",
        ],
        "confirmation_required_for": [
            "creating a GitHub repository",
            "publishing as public",
            "pushing commits",
            "creating tags or releases",
            "including generated outputs, datasets, or mission outputs",
        ],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
