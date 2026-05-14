<p align="center">
  <img src="assets/logo.svg" alt="intern-skill" width="160">
</p>

<h1 align="center">intern-skill</h1>

<p align="center">
  An AI intern that helps you onboard, understand, research, and extend open-source projects.
</p>

## What It Is

intern-skill is a project onboarding, source-reading, and technical research Agent Skill for Codex, Claude Code, Hermes Agent, OpenClaw, and other SKILL.md-compatible agents.

Give it a GitHub repository or a local project. It identifies the stack, entrypoints, dependency setup, core modules, data flow, and main execution path, then teaches the project in small steps that match your current level. Once learning starts, it gives concrete next learning steps instead of repeatedly asking where you want to begin.

Its job is not only to explain code. It organizes project onboarding, setup diagnosis, main-path tracing, frontier research, audit, and publishing preparation into a reusable learning workflow.

It is organized as a set of on-demand intern roles:

- **Project Navigator Intern**: builds the project map, main paths, module priorities, and recommended learning order.
- **Foundation Tutor Intern**: explains prerequisite terms and minimal mental models when the user is new to the stack.
- **Environment Setup Intern**: clones projects, detects dependencies, checks launch commands, and writes setup reports.
- **Technology Research Intern**: extracts technical points, researches recent papers, repositories, benchmarks, and tools, then judges transfer value.
- **Quality Audit Intern**: reviews tests, data flow, logs, monitoring, failure modes, and reliability risks.
- **Project Review Lead**: asks independent supervisor-style questions across both learned and unexplored areas.
- **Release Prep Intern**: checks README, license, secrets, large files, remotes, and installation notes before GitHub publishing.
- **Career Narrative Intern**: only activates when users explicitly need resume, interview, or portfolio wording.

## Who It Is For

- Interns who just received a project and do not know where to start.
- Job seekers who want to learn a project quickly before presenting it.
- Developers who want to extend an existing project safely.
- Beginners who need concept explanations before reading code.
- Learners who want supervisor-style review questions.

## How To Use

Learn a GitHub project:

```text
Use intern-skill to learn this project: https://github.com/NousResearch/hermes-agent
```

Learn a local project:

```text
Use intern-skill to learn the current project. Start with a project map and give me the next learning steps.
```

Foundation Tutor Intern:

```text
I am a beginner. Explain tool calls, memory, and skills before reading the code.
```

Project Review Lead:

```text
Act like a project supervisor and ask me 5 questions. Do not show answers yet.
```

Environment Setup Intern:

```text
Check what is missing before this project can run.
```

Release Prep Intern:

```text
Prepare this project for GitHub publishing. Start with a publish readiness check.
```

Technology Research Intern:

```text
Analyze this project, pick one technical point worth researching, and find the latest related projects and papers.
```

## One-Command Install

After cloning this repository:

```bash
bash scripts/install.sh --platform codex
```

Supported platforms:

```bash
bash scripts/install.sh --platform codex
bash scripts/install.sh --platform claude
bash scripts/install.sh --platform hermes
bash scripts/install.sh --platform openclaw --openclaw-project /path/to/miniOpenClaw-main
```

Install to all targets:

```bash
bash scripts/install.sh --platform all --openclaw-project /path/to/miniOpenClaw-main
```

Remote install after publishing to GitHub:

```bash
PROJECT_INTERN_REPO_URL=https://github.com/aluochiyou/intern-skill.git \
  bash -c "$(curl -fsSL https://raw.githubusercontent.com/aluochiyou/intern-skill/main/scripts/install.sh)" -- --platform codex
```

## Extension Interns

| Module | Use When |
| --- | --- |
| **Technology Research Intern** | The most important extension. Extract a technical point from the project, research recent papers/projects/benchmarks/tools, and judge what is truly worth transferring |
| **Project Navigator Intern** | You need a project map, main path, and learning order |
| **Foundation Tutor Intern** | You need prerequisite concepts first |
| **Environment Setup Intern** | You need to clone a repo or check how it runs |
| **Quality Audit Intern** | You want tests, data flow, logs, and risks reviewed |
| **Project Review Lead** | You want supervisor-style questions, including checks on unexplored areas |
| **Release Prep Intern** | You want a publish readiness check |
| **Career Narrative Intern** | You explicitly need resume, interview, or portfolio wording |

The Project Review Lead should use an independent review angle when possible, so it does not only ask about recently discussed modules. This helps uncover unreviewed entrypoints, commands, data flows, and risks.

## Adaptive Growth

intern-skill grows like a real intern. It can keep project maps, learning logs, feedback, and evaluation notes under `docs/intern/`, then use them to match your current level. It avoids repeating what you already know and avoids jumping into explanations that are too advanced.

You can say:

```text
Review my learning progress and adjust how intern-skill explains this project.
```

## Install Locations

| Platform | Default Location |
| --- | --- |
| Codex | `~/.codex/skills/project-intern` |
| Claude Code | `~/.claude/skills/project-intern` |
| Hermes Agent | `$HERMES_HOME/skills/project-intern`, default `~/.hermes/skills/project-intern` |
| OpenClaw / miniOpenClaw | `<project>/backend/skills/project-intern` |

## Check

```bash
python scripts/check_package.py
```

## License

MIT
