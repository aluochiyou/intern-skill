#!/usr/bin/env python3
"""Extract candidate project technical points for frontier research."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


KEYWORDS = {
    "agent loop": ["agent", "tool_call", "tool_calls", "run_conversation", "planner"],
    "tool calling": ["tool", "registry", "function_call", "handle_function_call"],
    "memory": ["memory", "mem0", "honcho", "recall", "session"],
    "retrieval": ["retrieval", "rag", "embedding", "vector", "search"],
    "evaluation": ["eval", "benchmark", "metric", "trajectory", "trace"],
    "observability": ["log", "trace", "telemetry", "langfuse", "monitor"],
    "data pipeline": ["dataset", "pipeline", "etl", "label", "annotation"],
    "deployment": ["docker", "compose", "kubernetes", "modal", "vercel"],
    "security": ["auth", "permission", "secret", "sandbox", "guardrail"],
    "frontend state": ["react", "next", "vite", "state", "component"],
    "api design": ["fastapi", "flask", "route", "endpoint", "server"],
    "plugin architecture": ["plugin", "extension", "adapter", "provider"],
}

IGNORE_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
TEXT_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".md", ".toml", ".yaml", ".yml", ".json"}


def iter_files(repo: Path):
    for path in repo.rglob("*"):
        rel_parts = set(path.relative_to(repo).parts)
        if rel_parts & IGNORE_DIRS:
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--top", type=int, default=8)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    scores: Counter[str] = Counter()
    evidence: dict[str, list[str]] = defaultdict(list)

    for path in iter_files(repo):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        rel = str(path.relative_to(repo))
        for point, words in KEYWORDS.items():
            count = sum(len(re.findall(rf"\b{re.escape(word.lower())}\b", text)) for word in words)
            if count:
                scores[point] += count
                if len(evidence[point]) < 5:
                    evidence[point].append(rel)

    result = [
        {
            "technical_point": point,
            "score": score,
            "evidence_files": evidence[point],
            "research_prompt": f"Research latest papers, benchmarks, and open-source projects about {point} and judge whether they can improve this project.",
        }
        for point, score in scores.most_common(args.top)
    ]
    print(json.dumps({"repo": str(repo), "candidates": result}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
