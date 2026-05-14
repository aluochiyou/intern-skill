# Project Intern Skill

Project Intern is an Agent Skill for learning open-source projects. Give it a GitHub repository or a local project, and it helps you understand the project step by step: what it does, where to start, which files matter, and how the main code path works.

It is useful when you want to:

- Learn an unfamiliar open-source project.
- Find the main entrypoints, modules, tests, and configuration.
- Get explanations that match your current level.
- Check environment setup before running a project.
- Practice with random supervisor-style review questions.
- Optionally audit tests, study related papers/projects, or prepare a GitHub release.

## Positioning

Project Intern focuses on project learning first. It starts with the project map and the main execution path, then moves through one small module, function, or concept at a time.

Optional modes such as interview/resume framing, audit, publishing, and frontier research are used only when you ask for them.

It can also run a review-question mode where it acts like a project supervisor and asks focused questions about the project before showing reference answers.

## Installation

Clone this repository, then run:

```bash
cd project-intern-skill
```

One-command local install:

```bash
bash scripts/install.sh --platform codex
```

After publishing this repository to GitHub, replace `OWNER/REPO` with your repo:

```bash
PROJECT_INTERN_REPO_URL=https://github.com/OWNER/REPO.git \
  bash -c "$(curl -fsSL https://raw.githubusercontent.com/OWNER/REPO/main/scripts/install.sh)" -- --platform codex
```

Codex:

```bash
python scripts/install.py --platform codex
```

Claude Code:

```bash
python scripts/install.py --platform claude
```

Hermes Agent:

```bash
python scripts/install.py --platform hermes
```

Hermes installs to `$HERMES_HOME/skills/project-intern`, defaulting to `~/.hermes/skills/project-intern`. If Hermes is already running, use:

```text
/reload-skills
```

OpenClaw / miniOpenClaw:

```bash
python scripts/install.py --platform openclaw --openclaw-project /path/to/miniOpenClaw-main
```

Install to all supported targets:

```bash
python scripts/install.py --platform all --openclaw-project /path/to/miniOpenClaw-main
```

Use `--force` to replace an existing installation.

## Usage

Learn a GitHub project:

```text
Use project-intern to learn this project: https://github.com/NousResearch/hermes-agent
```

Learn a local project:

```text
Use project-intern to learn the current project. Start with a project map.
```

Beginner mode:

```text
I am a beginner. Explain tool calls, memory, and skills before reading the code.
```

Continue with one module:

```text
Continue learning only the AIAgent.run_conversation loop.
```

Environment check:

```text
Check what is missing before this project can run.
```

Audit:

```text
Audit this project’s data flow and test coverage.
```

Random review questions:

```text
Act like a project supervisor and ask me 5 random questions. Do not show answers yet.
```

Related research or project:

```text
Compare this project with SWE-agent and suggest what can be learned.
```

GitHub publishing:

```text
Prepare this project for GitHub publishing. Start with a publish readiness check.
```

## Package Check

```bash
python scripts/check_package.py
```

## Structure

```text
project-intern-skill/
├── README.md
├── README.en.md
├── scripts/
│   ├── install.py
│   └── check_package.py
└── skills/
    └── project-intern/
        ├── SKILL.md
        ├── references/
        └── scripts/
```

## License

MIT
