#!/usr/bin/env python3
"""Run lightweight publish checks for intern-skill."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"PyYAML is required for package checks: {exc}")


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "project-intern"


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def check_skill() -> None:
    skill_md = SKILL_DIR / "SKILL.md"
    if not skill_md.exists():
        fail("skills/project-intern/SKILL.md is missing")
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    meta = yaml.safe_load(text[4:end]) or {}
    if meta.get("name") != "project-intern":
        fail("SKILL.md frontmatter name must be project-intern")
    if not meta.get("description"):
        fail("SKILL.md frontmatter description is required")
    if len(str(meta["description"])) > 1024:
        fail("SKILL.md description should stay under 1024 characters")


def check_layout() -> None:
    for rel in [
        "README.md",
        "README.en.md",
        "LICENSE",
        "scripts/install.py",
        "scripts/install.sh",
        "skills/project-intern/references",
        "skills/project-intern/scripts",
    ]:
        if not (REPO_ROOT / rel).exists():
            fail(f"Missing {rel}")
    pycache = list(REPO_ROOT.rglob("__pycache__"))
    if pycache:
        fail(f"Remove __pycache__ directories: {pycache}")


def check_python() -> None:
    for path in list((REPO_ROOT / "scripts").glob("*.py")) + list((SKILL_DIR / "scripts").glob("*.py")):
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    for platform in ("codex", "claude", "hermes"):
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "install.py"), "--platform", platform, "--dry-run"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode != 0:
            fail(f"install.py dry run failed for {platform}:\n{result.stdout}")
    shell_result = subprocess.run(
        ["bash", "-n", str(REPO_ROOT / "scripts" / "install.sh")],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if shell_result.returncode != 0:
        fail(f"install.sh syntax check failed:\n{shell_result.stdout}")


def main() -> int:
    check_layout()
    check_skill()
    check_python()
    print("Package checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
