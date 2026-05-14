# Learning Route

Use this route when guiding a user through an unfamiliar project.

## Project Positioning

Before reading code, answer:

1. What does the project do?
2. Who uses it?
3. What are the core user actions?
4. What are the inputs and outputs?
5. Where is data stored?
6. What are the main technologies?
7. What are the most important one or two execution paths?

Use evidence from README, docs, manifests, entrypoint files, route files, command handlers, tests, and CI.

## Main Path First

Map the core user action before details:

```text
user action
-> frontend / CLI / API entry
-> route or command handler
-> core service or business class
-> model / tool / database / file system / external API
-> response or output
-> persistence, logging, monitoring, evaluation
```

Common variants:

- Web app: page action -> API -> service -> database -> response.
- Agent app: user input -> chat API -> agent loop -> tools -> memory -> stream.
- Data project: input data -> cleaning -> transform -> storage -> evaluation.
- CLI project: command args -> command handler -> core logic -> terminal output.

## Module Explanation

For each module, explain:

1. What it is.
2. Where it sits in the project.
3. What problem it solves.
4. How it connects to other modules.
5. What the user should be able to say after learning it.

Avoid full framework lectures. Teach only the current code's required background. For example:

- SSE: explain why it fits streaming output.
- FastAPI: explain request model, route handler, response shape.
- React: explain state and rendering only as used by the code.
- Database: explain this project's read/write path and schema.

## Learning Priority

Always classify material:

- **Must know**: required to understand the main path or modify the project safely.
- **Useful to know**: helps deepen understanding but is not blocking.
- **Skip for now**: framework internals, rare edge cases, or side modules unrelated to the current path.

## Engineering Value

Look for real, evidence-based highlights:

- Structured execution flow instead of one-off scripts.
- Evented or traceable intermediate states.
- Clear module boundaries.
- Configuration and dependency isolation.
- Error handling and retry behavior.
- Logs, metrics, traces, or saved execution artifacts.
- Evaluation hooks, datasets, test fixtures, or failure analysis.
- Extensible tools, skills, plugins, prompts, or adapters.

Do not call a project impressive only because it uses a popular framework.

## Optional Modes

Do not open every mode by default. Match the user's current goal:

- **Career packaging**: only when the user mentions job search, resume, interviews, internship applications, portfolio, or asks how to present the work.
- **Audit and evaluation**: only when the user asks to test, monitor, evaluate, trace data flow, find risks, or improve reliability.
- **External insight transfer**: only when the user provides or names a paper, benchmark, method, article, or related project.
- **GitHub publishing**: only when the user asks to publish, upload, release, open-source, or package the project.

If the user's goal is simply learning, keep the answer focused on understanding and next learning steps.

## Baseline To Improvement

Use this explanation pattern:

```text
Simple baseline:
An initial implementation might...

Problem:
This breaks down because...

Current project approach:
This project instead...

Career expression:
Only include this when career packaging is active.
```

Useful comparisons:

- One-shot response -> streaming events.
- Hard-coded prompt -> file or skill based prompt.
- Only final answer -> full execution trace.
- Manual capabilities -> documented skills/tools.
- Raw model call -> agent plus tools plus memory plus guardrails.
- Only final accuracy -> trace-level error analysis.

## Pace

Prefer one small unit per response. Good units include one endpoint, one command, one class, one state object, one database table, one event type, or one test path.

After learning has started, end with recommended next steps instead of asking the user to choose from scratch. Only ask a question when the next step depends on unavailable information, user credentials, destructive actions, or a genuine goal conflict.
