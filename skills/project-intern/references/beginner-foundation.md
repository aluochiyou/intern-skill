# Beginner Foundation

Use this when the user is new to a stack, project type, or concept.

## Goal

Help the user understand enough vocabulary and mental models to follow the project explanation. Do not turn this into a full textbook lesson.

## Process

1. Identify the current learning target: project setup, API route, frontend state, agent loop, data pipeline, test, deployment, or paper method.
2. List only the concepts needed for that target.
3. Explain each concept in three layers:
   - Plain meaning.
   - Why projects need it.
   - Where it appears in the current project.
4. Use one tiny concrete example.
5. End with priority:
   - Must know now.
   - Useful later.
   - Skip for now.

## Common Concepts

For web projects:

- Frontend: the part the user sees and interacts with.
- Backend: the service that receives requests, runs logic, and returns results.
- API: the contract between frontend and backend.
- Route: a specific backend address that handles one type of request.
- Database: where persistent data is stored.
- Environment variable: configuration supplied outside code, often for keys or paths.

For agent projects:

- Agent loop: repeated observe, think, act, and respond process.
- Tool: an external capability the model can call, such as search or file access.
- Memory: stored context reused across turns or tasks.
- Skill: reusable instructions and resources for a class of tasks.
- Trace: saved intermediate steps, tool calls, errors, and outputs.
- Evaluation: measuring whether the agent did the right thing and why it failed.

For data and evaluation projects:

- Dataset: structured examples used for training, testing, or evaluation.
- Label: expected answer or annotation.
- Metric: a rule for scoring output quality.
- Pipeline: ordered data processing steps.
- Data lineage: where data came from and how it changed.
- Regression test: a test that prevents old bugs from returning.

For deployment:

- Dependency: external package needed by the project.
- Container: a packaged runtime environment.
- Image: the template used to start containers.
- Port: network doorway where a service listens.
- CI: automated checks that run on code changes.
- Release: a versioned package or milestone for users.

## Output Template

```text
Before the code, you need these concepts:

1. Term
   Plain meaning:
   Why it exists:
   Where it appears here:

Tiny example:

Must know now:
Useful later:
Skip for now:
Now we can read the module:
```
