#!/usr/bin/env python3
"""Clone a GitHub project, detect its stack, and produce a setup plan.

Default behavior is safe: clone if needed, inspect, and write a report. Use
--install to run inferred dependency installation commands.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


SKILL_DIR = Path(__file__).resolve().parents[1]
DETECT_STACK = SKILL_DIR / "scripts" / "detect_stack.py"


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


def repo_name_from_url(url: str) -> str:
    parsed = urlparse(url)
    tail = Path(parsed.path).name or "downloaded-project"
    if tail.endswith(".git"):
        tail = tail[:-4]
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", tail).strip("-._")
    return safe or "downloaded-project"


def load_stack_report(repo: Path) -> dict:
    code, output = run([sys.executable, str(DETECT_STACK), str(repo)])
    if code != 0:
        return {"error": output}
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"error": output}


def choose_install_commands(stack: dict) -> list[list[str]]:
    manifests = stack.get("manifests", [])
    commands: list[list[str]] = []
    by_dir: dict[str, set[str]] = {}
    for item in manifests:
        path = Path(item.get("file", ""))
        by_dir.setdefault(str(path.parent), set()).add(item.get("name") or path.name)
    for dirname, names in by_dir.items():
        cwd_prefix = [] if dirname == "." else ["--cwd", dirname]
        if "package.json" in names:
            if "pnpm-lock.yaml" in names:
                commands.append(["pnpm", *cwd_prefix, "install"])
            elif "yarn.lock" in names:
                commands.append(["yarn", *cwd_prefix, "install"])
            else:
                commands.append(["npm", "install", "--prefix", dirname] if dirname != "." else ["npm", "install"])
        if "requirements.txt" in names:
            req = "requirements.txt" if dirname == "." else f"{dirname}/requirements.txt"
            commands.append([sys.executable, "-m", "pip", "install", "-r", req])
        if "pyproject.toml" in names:
            if "uv.lock" in names:
                commands.append(["uv", "sync"] if dirname == "." else ["uv", "sync", "--directory", dirname])
            elif "poetry.lock" in names:
                commands.append(["poetry", "install"] if dirname == "." else ["poetry", "-C", dirname, "install"])
        if "go.mod" in names:
            commands.append(["go", "mod", "download"] if dirname == "." else ["go", "-C", dirname, "mod", "download"])
        if "Cargo.toml" in names:
            commands.append(["cargo", "fetch"] if dirname == "." else ["cargo", "fetch", "--manifest-path", f"{dirname}/Cargo.toml"])
    return commands


def markdown_report(repo_url: str, repo: Path, stack: dict, install_results: list[dict]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Project Bootstrap Report",
        "",
        f"- Generated: {now}",
        f"- Source: {repo_url}",
        f"- Local path: `{repo}`",
        "",
        "## Detected Stack",
        "",
        "```json",
        json.dumps(stack, indent=2, ensure_ascii=False),
        "```",
        "",
        "## Install Results",
        "",
    ]
    if install_results:
        for item in install_results:
            lines.extend(
                [
                    f"### `{' '.join(item['command'])}`",
                    "",
                    f"- Exit code: {item['exit_code']}",
                    "",
                    "```text",
                    item["output"][-4000:],
                    "```",
                    "",
                ]
            )
    else:
        lines.append("No install commands were run. Re-run with `--install` after reviewing the plan.")
        lines.append("")
    lines.extend(
        [
            "## Next Learning Steps",
            "",
            "1. Read README and setup docs.",
            "2. Open the detected entrypoints.",
            "3. Follow one main user action through the code.",
            "4. Run tests or the smallest safe verification command.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("github_url", help="GitHub HTTPS/SSH URL to clone")
    parser.add_argument("--workspace", default=".", help="Directory where the repo should be cloned")
    parser.add_argument("--name", help="Override local folder name")
    parser.add_argument("--install", action="store_true", help="Run inferred dependency installation commands")
    parser.add_argument("--write-report", action="store_true", help="Write PROJECT_BOOTSTRAP_REPORT.md in the repo")
    args = parser.parse_args()

    workspace = Path(args.workspace).expanduser().resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    repo = workspace / (args.name or repo_name_from_url(args.github_url))

    actions = []
    if repo.exists():
        actions.append(f"Using existing directory: {repo}")
    else:
        code, output = run(["git", "clone", args.github_url, str(repo)])
        actions.append(output)
        if code != 0:
            print(json.dumps({"ok": False, "actions": actions}, indent=2, ensure_ascii=False))
            return code

    stack = load_stack_report(repo)
    install_results = []
    if args.install:
        for command in choose_install_commands(stack):
            code, output = run(command, cwd=repo)
            install_results.append({"command": command, "exit_code": code, "output": output})
            if code != 0:
                break

    report_text = markdown_report(args.github_url, repo, stack, install_results)
    if args.write_report:
        (repo / "PROJECT_BOOTSTRAP_REPORT.md").write_text(report_text, encoding="utf-8")

    response = {
        "ok": True,
        "repo": str(repo),
        "actions": actions,
        "stack": stack,
        "install_commands": choose_install_commands(stack),
        "install_results": install_results,
        "report_written": str(repo / "PROJECT_BOOTSTRAP_REPORT.md") if args.write_report else None,
        "next": [
            "Review README and PROJECT_BOOTSTRAP_REPORT.md",
            "Open detected entrypoints",
            "Run tests or smallest safe verification command",
        ],
    }
    print(json.dumps(response, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
