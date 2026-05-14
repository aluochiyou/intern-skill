#!/usr/bin/env python3
"""Append a structured project-intern session log."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--task", required=True)
    parser.add_argument("--outcome", default="")
    parser.add_argument("--artifacts", nargs="*", default=[])
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    out = repo / "docs" / "intern" / "LEARNING_LOG.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    record = [
        f"## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"- Task: {args.task}",
        f"- Outcome: {args.outcome or 'Not recorded'}",
        f"- Artifacts: {', '.join(args.artifacts) if args.artifacts else 'None'}",
        f"- Notes: {args.notes or 'None'}",
        "",
    ]
    with out.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(record))
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
