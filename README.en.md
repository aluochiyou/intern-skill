<p align="center">
  <img src="assets/logo.svg" alt="Intern Skill" width="160">
</p>

<h1 align="center">Intern Skill</h1>

<p align="center">
  An AI intern that helps you onboard, understand, and extend open-source projects.
</p>

## What It Is

Intern Skill is a project-learning Agent Skill for Codex, Claude Code, Hermes Agent, OpenClaw, and other SKILL.md-compatible agents.

Give it a GitHub repository or a local project. It helps you understand what the project does, where to start, how the main execution path works, and what to learn next.

## Who It Is For

- Interns who just received a project and do not know where to start.
- Job seekers who want to learn a project quickly before presenting it.
- Developers who want to extend an existing project safely.
- Beginners who need concept explanations before reading code.
- Learners who want supervisor-style review questions.

## How To Use

Learn a GitHub project:

```text
Use Intern Skill to learn this project: https://github.com/NousResearch/hermes-agent
```

Learn a local project:

```text
Use Intern Skill to learn the current project. Start with a project map.
```

Beginner mode:

```text
I am a beginner. Explain tool calls, memory, and skills before reading the code.
```

Review questions:

```text
Act like a project supervisor and ask me 5 questions. Do not show answers yet.
```

Environment check:

```text
Check what is missing before this project can run.
```

GitHub publishing:

```text
Prepare this project for GitHub publishing. Start with a publish readiness check.
```

Frontier radar:

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

## Modules

| Module | Use When |
| --- | --- |
| Beginner Mode | You need prerequisite concepts first |
| Setup | You need to clone a repo or check how it runs |
| Review Questions | You want supervisor-style questions |
| Audit | You want tests, data flow, logs, and risks reviewed |
| Frontier Radar | You want to extract a technical point, research recent projects/papers/benchmarks, and judge whether they are useful |
| GitHub Publishing | You want a publish readiness check |
| Career Framing | You explicitly need resume, interview, or portfolio wording |

## Adaptive Learning

Intern Skill can keep project maps, learning logs, and feedback under `docs/intern/`. This helps it match your current level: it can avoid repeating what you already know and avoid jumping into explanations that are too advanced.

You can say:

```text
Review my learning progress and adjust how Intern Skill explains this project.
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
