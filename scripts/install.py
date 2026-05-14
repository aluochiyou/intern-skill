#!/usr/bin/env python3
"""Install Project Intern Skill into Codex, Claude Code, Hermes Agent, or OpenClaw."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "project-intern"
SOURCE_SKILL = REPO_ROOT / "skills" / SKILL_NAME
EXCLUDE_DIRS = {"__pycache__", ".git"}


def copy_skill(destination: Path, *, force: bool, dry_run: bool) -> None:
    if not SOURCE_SKILL.exists():
        raise SystemExit(f"Missing source skill: {SOURCE_SKILL}")

    if destination.exists() and not force and not dry_run:
        raise SystemExit(
            f"Destination already exists: {destination}\n"
            "Re-run with --force to replace it."
        )

    print(f"Install {SOURCE_SKILL} -> {destination}")
    if dry_run:
        return

    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)

    def ignore(_dir: str, names: list[str]) -> set[str]:
        return {name for name in names if name in EXCLUDE_DIRS or name.endswith(".pyc")}

    shutil.copytree(SOURCE_SKILL, destination, ignore=ignore)


def codex_dir() -> Path:
    home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
    return home / "skills" / SKILL_NAME


def claude_dir() -> Path:
    return Path.home() / ".claude" / "skills" / SKILL_NAME


def hermes_dir() -> Path:
    home = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")).expanduser()
    return home / "skills" / SKILL_NAME


def resolve_openclaw_base(path_arg: str | None) -> Path:
    if not path_arg:
        # Generic fallback for OpenClaw-like user-level installs.
        return Path(os.environ.get("OPENCLAW_HOME", Path.home() / ".openclaw")).expanduser()

    path = Path(path_arg).expanduser().resolve()
    if (path / "backend" / "tools" / "skills_scanner.py").exists():
        return path / "backend"
    if (path / "tools" / "skills_scanner.py").exists():
        return path
    if (path / "backend" / "skills").exists():
        return path / "backend"
    return path


def openclaw_dir(path_arg: str | None) -> Path:
    return resolve_openclaw_base(path_arg) / "skills" / SKILL_NAME


def refresh_openclaw_snapshot(base_dir: Path, *, dry_run: bool) -> None:
    scanner = base_dir / "tools" / "skills_scanner.py"
    if not scanner.exists():
        print(f"OpenClaw snapshot refresh skipped; scanner not found under {base_dir}")
        return
    print(f"Refresh OpenClaw skills snapshot under {base_dir}")
    if dry_run:
        return
    code = (
        "import sys; "
        f"sys.path.insert(0, {str(base_dir)!r}); "
        "from tools.skills_scanner import refresh_snapshot; "
        f"print(refresh_snapshot(__import__('pathlib').Path({str(base_dir)!r})))"
    )
    subprocess.run([sys.executable, "-c", code], check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform",
        choices=["codex", "claude", "hermes", "openclaw", "all"],
        default="codex",
        help="Target platform to install into.",
    )
    parser.add_argument(
        "--openclaw-project",
        help="OpenClaw/miniOpenClaw repo root or backend directory.",
    )
    parser.add_argument("--force", action="store_true", help="Replace existing installation.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without copying.")
    args = parser.parse_args()

    targets: list[tuple[str, Path]] = []
    if args.platform in {"codex", "all"}:
        targets.append(("codex", codex_dir()))
    if args.platform in {"claude", "all"}:
        targets.append(("claude", claude_dir()))
    if args.platform in {"hermes", "all"}:
        targets.append(("hermes", hermes_dir()))
    if args.platform in {"openclaw", "all"}:
        targets.append(("openclaw", openclaw_dir(args.openclaw_project)))

    for platform, destination in targets:
        copy_skill(destination, force=args.force, dry_run=args.dry_run)
        if platform == "openclaw":
            refresh_openclaw_snapshot(destination.parent.parent, dry_run=args.dry_run)

    print("Done. Restart Codex/OpenClaw if needed. Claude Code usually detects skill edits live. In Hermes Agent, use /reload-skills if the session is already running.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
