#!/usr/bin/env python3
"""Generate supervisor-style project review questions from local evidence."""

from __future__ import annotations

import argparse
import random
from pathlib import Path


QUESTION_BANK = {
    "project": [
        "这个项目主要解决什么问题？它的目标用户是谁？",
        "如果用三句话向别人介绍这个项目，你会怎么说？",
        "这个项目的输入和输出分别是什么？",
    ],
    "main_path": [
        "项目最核心的一条用户操作或命令是什么？它从哪个入口文件开始？",
        "从入口到核心逻辑，中间经过了哪些模块？",
        "如果要追踪一次完整执行，你会先打开哪三个文件？为什么？",
    ],
    "module": [
        "你认为这个项目最核心的模块是哪一个？它负责什么？",
        "哪些模块是主链路，哪些模块暂时可以跳过？",
        "如果删除一个支持模块，主流程会在哪里受到影响？",
    ],
    "data": [
        "数据从哪里进入项目？在哪里被转换？最终到哪里输出或保存？",
        "这个项目有没有持久化数据？如果有，保存在哪里？",
        "哪些数据需要特别注意隐私、密钥或安全问题？",
    ],
    "quality": [
        "这个项目有哪些测试入口？它们覆盖的是主流程还是边缘功能？",
        "如果你要给核心流程补一个测试，你会测什么？",
        "项目运行失败时，你会先看日志、配置、依赖还是测试？为什么？",
    ],
    "tradeoff": [
        "这个项目有没有比简单 demo 更工程化的设计？体现在哪里？",
        "当前设计相比最简单写法，解决了什么问题？",
        "如果项目规模扩大，哪个模块最可能先需要重构？",
    ],
    "extension": [
        "如果要加一个新功能，你会放在哪个模块？为什么？",
        "你会如何验证新功能没有破坏原有主流程？",
        "有没有一个外部项目或论文的方法可以借鉴到这里？它适合放在哪里？",
    ],
}


def read_project_map(repo: Path) -> str:
    for rel in ("docs/intern/PROJECT_MAP.md", "PROJECT_BOOTSTRAP_REPORT.md", "README.md"):
        path = repo / rel
        if path.exists():
            return path.read_text(encoding="utf-8", errors="ignore")[:4000]
    return ""


def infer_focus(evidence: str) -> list[str]:
    focus = ["project", "main_path", "module"]
    low = evidence.lower()
    if any(word in low for word in ("test", "pytest", "vitest", "e2e")):
        focus.append("quality")
    if any(word in low for word in ("database", "memory", "storage", "data", "dataset")):
        focus.append("data")
    if any(word in low for word in ("agent", "tool", "skill", "plugin", "workflow")):
        focus.append("tradeoff")
    focus.append("extension")
    return focus


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    evidence = read_project_map(repo)
    rng = random.Random(args.seed)
    categories = infer_focus(evidence)

    questions = []
    for category in categories:
        questions.extend((category, q) for q in QUESTION_BANK[category])
    rng.shuffle(questions)
    selected = questions[: max(1, min(args.count, len(questions)))]

    print("# 项目评审主管随机提问")
    print()
    print(f"项目：`{repo}`")
    print()
    print("本轮提问重点：")
    print()
    for idx, (category, question) in enumerate(selected, 1):
        print(f"{idx}. [{category}] {question}")
    print()
    print("回答建议：先用自己的话回答；不确定时说明你的猜测和证据位置。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
