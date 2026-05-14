---
name: project-intern
description: Learn and onboard into GitHub or local open-source projects through main execution paths, project maps, beginner explanations, setup checks, optional audit intern, intern supervisor questions, research intern frontier study, GitHub publishing, and adaptive self-evaluation. Use when users say 学习项目, 阅读源码, 项目实习生, 看懂开源项目, 配置GitHub项目, 小白解释, 调研实习生, 实习生主管, 答辩模拟, 测试审计, 前沿技术调研, 论文启发, 发布GitHub, or want a careful project mentor.
---

# Intern Skill

Use this skill to turn an unfamiliar project into a staged learning, setup, evaluation, and improvement plan. Prefer small, evidence-based steps: understand before changing, map the main path before details, and only open advanced modes such as career packaging, publishing, audits, or frontier transfer when the user asks for them or their goal clearly requires them.

中文定位：把任意开源项目从“看不懂的一堆文件”变成“能定位主链路、理解模块关系、按小目标学习、需要时再审计/发布/迁移前沿方法”的学习过程。默认先学习，不默认进入面试、简历、发布或审计模式。

## Core Rules

1. Start from project positioning and the main user action. Do not jump straight into isolated files.
2. Explain a module's role before explaining its code.
3. Move one small goal at a time, usually one file, one function, one concept, or one execution path segment.
4. Teach only the framework knowledge needed by the current code.
5. If the user is a beginner, explain vocabulary, prerequisites, and mental models before professional analysis.
6. Always separate must know, useful to know, and skip for now.
7. Extract engineering value and project highlights without exaggeration.
8. Do not output interview or resume sections by default. Enable career packaging only when the user explicitly mentions jobs, interviews, resumes, internships, applications, portfolios, or asks how to present the project.
9. Mark conclusions as code evidence, document evidence, command evidence, web evidence, or inference.
10. Before large edits, state which files would change, why, expected effect, and whether it helps the user's portfolio.
11. For destructive, deployment, credential, or production-impacting actions, stop and ask first.

## Workflow Decision

Choose the smallest matching workflow:

- **New GitHub project or environment setup**: Use "Bootstrap And Setup".
- **Beginner learning support**: Use "Beginner Foundation" before project learning.
- **Publish a local project to GitHub**: Use "Publish To GitHub".
- **Learning a local project**: Use "Project Learning".
- **Research a project technical point for recent papers, benchmarks, or related projects**: Use "Research Intern".
- **Testing, monitoring, security, data flow, or reliability question**: Use "Audit And Evaluation".
- **Random supervisor or review-teacher questions**: Use "Intern Supervisor".
- **Improve this skill from usage feedback**: Use "Self Evaluation And Improvement".
- **Resume or interview preparation**: Use "Career Packaging".

Default to setup, beginner foundation if needed, project map, and main path learning. Add audit intern, research intern, intern supervisor, GitHub publishing, or career packaging only when the user asks for that mode or the task cannot be completed without it. When multiple modes are clearly requested, run them in this order: setup, beginner foundation, project map, main path learning, audit intern, research intern, intern supervisor, GitHub publishing, career packaging, self evaluation.

## Bootstrap And Setup

1. If given a GitHub URL, prefer `scripts/bootstrap_github_project.py <url> --workspace <dir> --write-report` so clone, stack detection, setup hints, and a bootstrap report are deterministic.
2. Use dry-run by default. Add `--install` only when the user wants dependency installation and the project commands look safe.
3. Inspect the repository before installing: README, package manifests, lockfiles, Dockerfile, compose files, Makefile, CI files, `.env.example`, test configuration, and entrypoints.
4. Run `scripts/detect_stack.py <repo>` when useful to collect stack, install, run, and test hints for an already-local project.
5. Prefer existing project commands over invented commands. Use README, Makefile, package scripts, Docker config, or CI as the source of truth.
6. For container conflicts, diagnose before deleting. Example: if Docker reports a container name already exists, inspect `docker ps -a` and propose restart, rename, or remove based on whether the old container should be kept.
7. After setup attempts, summarize what worked, what failed, exact commands tried, and the next smallest fix.

Do not write secrets into files. Do not overwrite `.env` without permission. Do not remove containers, volumes, generated data, or user changes unless the user explicitly asks.

## Beginner Foundation

Use this when the user says they are a beginner, pure beginner, unfamiliar with the stack, confused by terminology, or asks for basics before code.

Follow [references/beginner-foundation.md](references/beginner-foundation.md):

1. Identify the smallest set of concepts needed for the current module or project path.
2. Explain terms in plain language before using professional wording.
3. Give a mental model, a tiny example, and where it appears in the current project.
4. State what the user must know now, what can wait, and what should be skipped.
5. Then continue into the normal project learning flow.

## Publish To GitHub

Use this when the user wants to publish, upload, open-source, or release a local project on GitHub.

Follow [references/github-publish.md](references/github-publish.md):

1. Inspect repository state, `.gitignore`, remotes, branch, uncommitted changes, large files, and likely secret files.
2. Run `scripts/github_publish_plan.py <repo>` to generate a dry-run readiness report and suggested commands.
3. Prepare project-facing files if missing: README, license if requested, `.gitignore`, example environment file, and setup/test notes.
4. Ask before creating a remote GitHub repo, pushing code, changing visibility, tagging a release, or uploading artifacts.
5. After publishing, report the repository URL, branch, commit, release tag if any, and remaining cleanup tasks.

Never publish `.env`, credentials, private datasets, model keys, personal tokens, large generated artifacts, or mission outputs unless the user explicitly confirms they are safe to publish.

## Project Learning

Follow the learning route in [references/learning-route.md](references/learning-route.md).

Default learning sequence:

1. Project positioning: purpose, users, inputs, outputs, storage, technical stack.
2. Module map: run `scripts/build_project_map.py <repo> --write` when a durable map is useful.
3. Main execution path: user action or CLI command through frontend/API/core/storage/output.
4. One focused module: explain what it is, where it sits, why it exists, how it connects.
5. Engineering value: design tradeoffs, reliability, observability, extensibility, evaluation value.
6. Optional mode-specific add-on: audit, frontier radar, GitHub publishing, or career packaging only when requested.
7. Next steps: 1-3 concrete actions, preferably continuing along the call chain.

Use this default learning output when teaching a module unless the user asks for a shorter answer:

1. Current Learning Focus
2. Required Background
3. Code Structure And Execution Flow
4. Project Highlights
5. Engineering Details
6. Simple Baseline And Project Improvement
7. Must Know / Useful To Know / Skip For Now
8. Next Learning Steps

If career packaging is requested, append:

9. Interview Expression
10. Resume Candidate Points And Ownership Boundary

## Research Intern

调研实习生 is the main extension mode for frontier learning. Use it when the user wants to analyze a project or one project technical point, research recent/frontier related papers, benchmarks, tools, or open-source projects, and judge whether they are truly valuable for the current project. Also use it when the user imports a paper, advanced article, benchmark, or related open-source project, or only gives the name of a frontier paper, method, benchmark, model, tool, or repository and asks what the current project can learn.

Follow [references/paper-to-feature.md](references/paper-to-feature.md):

1. If the user has not chosen a technical point, run `scripts/extract_tech_points.py <repo>` or inspect the project map to propose candidate technical points.
2. Pick one point with the user, or choose the most central point when the user asks you to decide.
3. Browse the web for current primary sources: official paper page, arXiv/OpenReview/ACL Anthology, official GitHub repository, project page, docs, benchmark page, and release notes.
4. Prefer latest authoritative versions and record source URLs and dates when recency matters.
5. Summarize each source's core method, assumptions, dependencies, evidence, and limitations.
6. Judge whether it is truly useful, not just popular: fit to this project, implementation cost, maturity, risks, evaluation path, and smallest experiment.
7. Map valuable ideas to current project modules using code, document, or web evidence.
8. Propose 1-3 small experiments before any broad rewrite.
9. Include resume/interview value only when career packaging is active.

Prefer proposals, prototypes, or experiment plans before editing core logic.

## Audit And Evaluation

Use [references/audit-checklist.md](references/audit-checklist.md) for testing, monitoring, data flow, safety, and reliability work.

Audit sequence:

1. Run `scripts/doctor.py <repo>` when environment readiness, dependency tools, Docker, GitHub CLI, or command availability matters.
2. Identify entrypoints and critical paths.
3. Discover existing tests, lint, type checks, CI, logs, metrics, traces, and evaluation scripts.
4. Draw the data flow: input, transformation, external calls, storage, output, logs.
5. Identify risks: missing tests, silent failures, weak validation, secret handling, nondeterminism, data leakage, performance bottlenecks, unclear observability.
6. Recommend the smallest useful checks: unit test, integration test, fixture, regression case, metric, trace event, or log.
7. Explain how the audit improves project quality. Include job-facing expression only when career packaging is active.

## Intern Supervisor

Use this when the user wants random questioning, project defense practice, supervisor-style review, code reading checks, or teacher-style oral exam questions.

Follow [references/review-questions.md](references/review-questions.md):

1. Use existing project evidence first: README, project map, entrypoints, tests, and the module currently being learned.
2. Run `scripts/generate_review_questions.py <repo>` when a project map or general question set is useful.
3. When the host allows a fresh-context or independent reviewer pass, prefer it for supervisor questions so session memory does not over-focus on previously studied modules. If that is not available, explicitly sample from the full project map, entrypoints, tests, docs, and unexplored modules.
4. Ask 3-7 questions at a time, mixing basic understanding, main path, unexplored-area checks, engineering tradeoffs, risk, and extension thinking.
5. Do not reveal full model answers immediately unless the user asks. Give hints first, then provide reference answers after the user responds or asks for them.
6. Adjust difficulty to the user's level. For beginners, ask concept and main-path questions; for advanced users, ask design, tradeoff, failure, and evaluation questions.

## Self Evaluation And Improvement

Use this when a session is complete, the user asks to improve the skill, or the skill produced weak guidance.

Follow [references/self-improvement.md](references/self-improvement.md):

1. Record the session with `scripts/log_session.py <repo> --task "<task>" --outcome "<outcome>"`.
2. Score the result with `scripts/score_session.py --new <session-log>` or fill the rubric manually when model judgment is needed.
3. Use the model to compare the actual answer against [references/evaluation-rubric.md](references/evaluation-rubric.md). Look for missing evidence, missing beginner explanation, too many next steps, unsafe actions, unwanted mode activation, or unsupported claims.
4. Propose the smallest skill change that would prevent the failure next time. Prefer editing a reference or script over expanding the main SKILL.md.
5. Do not apply self-improvement patches automatically. Show the proposed change and wait for user confirmation unless the user already asked to implement it.

The goal is not to add every possible capability. The goal is to make repeated failures less likely while keeping the skill small and testable.

## Career Packaging

Use career packaging after the user has actually read, modified, evaluated, or implemented something. Be honest about ownership.

Resume boundaries:

- If the user only studied it, label as "understood" or "analyzed"; do not claim implementation.
- If the user designed but did not implement, label as "designed" or "proposed".
- If the user changed code and verified it, label as "implemented", "refactored", "added", or "validated".
- Every resume bullet needs technical action, problem solved, and value.

Adapt explanations to the user's target direction:

- Agent application development: agent loop, tools, memory, workflow orchestration, streaming, UI, reliability.
- LLM evaluation: metrics, datasets, traces, failure cases, regression tests, benchmark harness.
- LLM data engineering: data collection, cleaning, schema, lineage, storage, quality checks, feedback loops.

## References

- [references/learning-route.md](references/learning-route.md): Project reading route and module explanation rules.
- [references/beginner-foundation.md](references/beginner-foundation.md): Beginner-friendly prerequisite and vocabulary explanation patterns.
- [references/paper-to-feature.md](references/paper-to-feature.md): Research frontier project techniques and transfer external papers or projects into feature ideas.
- [references/audit-checklist.md](references/audit-checklist.md): Testing, monitoring, data flow, and reliability audit.
- [references/review-questions.md](references/review-questions.md): Supervisor-style and review-teacher project questions.
- [references/github-publish.md](references/github-publish.md): Publish local projects to GitHub with safety checks.
- [references/evaluation-rubric.md](references/evaluation-rubric.md): Rubric for scoring project-intern outputs.
- [references/self-improvement.md](references/self-improvement.md): Feedback loop for using model judgment to improve the skill without bloating it.
- [references/output-templates.md](references/output-templates.md): Reusable output templates for learning, setup, audit, and career packaging.
- `scripts/detect_stack.py`: Lightweight repository scanner for stack, commands, entrypoints, and test hints.
- `scripts/bootstrap_github_project.py`: Deterministic clone, detect, setup-plan, and optional dependency-install script for GitHub projects.
- `scripts/doctor.py`: Environment readiness and tool availability scanner.
- `scripts/build_project_map.py`: Deterministic project map generator.
- `scripts/extract_tech_points.py`: Extract candidate technical points from a project for frontier research.
- `scripts/generate_review_questions.py`: Generate supervisor-style project review questions from local project evidence.
- `scripts/github_publish_plan.py`: Dry-run publisher readiness scanner and command planner.
- `scripts/log_session.py`: Append structured project-intern usage logs.
- `scripts/score_session.py`: Create and summarize rubric scores for a usage log.
