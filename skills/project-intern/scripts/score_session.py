#!/usr/bin/env python3
"""Create or summarize a project-intern session rubric score."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


DIMENSIONS = [
    "project_positioning",
    "main_path_focus",
    "evidence_quality",
    "beginner_support",
    "scope_control",
    "engineering_value",
    "mode_discipline",
    "safety",
    "actionability",
    "skill_fitness",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--task", default="")
    parser.add_argument("--scores", help="JSON object with 1-5 scores")
    parser.add_argument("--notes", default="")
    parser.add_argument("--new", action="store_true", help="Print an empty score template")
    args = parser.parse_args()

    if args.new:
        template = {name: None for name in DIMENSIONS}
        print(json.dumps({"task": args.task, "scores": template, "notes": args.notes}, indent=2))
        return 0

    scores = json.loads(args.scores or "{}")
    missing = [name for name in DIMENSIONS if name not in scores]
    if missing:
        raise SystemExit(f"Missing score dimensions: {', '.join(missing)}")
    values = [float(scores[name]) for name in DIMENSIONS]
    average = round(sum(values) / len(values), 2)
    low = [name for name in DIMENSIONS if float(scores[name]) <= 3]
    record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "task": args.task,
        "scores": scores,
        "average": average,
        "low_dimensions": low,
        "notes": args.notes,
    }

    repo = Path(args.repo).resolve()
    out = repo / "docs" / "intern" / "SESSION_SCORES.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(json.dumps(record, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
