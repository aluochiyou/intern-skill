# Audit Checklist

Use this for testing, monitoring, data-flow, safety, and reliability reviews.

## Discovery

Find:

- README setup and test commands.
- Makefile, package scripts, tox, pytest, uv, poetry, pnpm, npm, yarn, cargo, go test, Docker, compose.
- CI workflows.
- Test folders and fixture data.
- Logging configuration.
- Metrics, traces, dashboards, or telemetry hooks.
- Error handling and retry utilities.
- Config and environment variable loading.
- External APIs, model providers, databases, file writes, queues, or caches.

## Data Flow

For critical paths, map:

```text
input source
-> validation
-> transformation
-> external calls
-> storage
-> output
-> logs / metrics / traces
-> evaluation artifacts
```

Check whether sensitive data, prompts, model outputs, user identifiers, or secrets are stored or logged.

## Testing

Look for:

- Unit tests for pure logic.
- Integration tests for service boundaries.
- End-to-end tests for main user actions.
- Regression tests for known failures.
- Fixtures or golden files.
- Mocked external services.
- Determinism controls for model calls or random behavior.
- CI coverage of install, lint, type check, and test.

Recommend the smallest meaningful test before broad test plans.

## Monitoring

For runtime behavior, ask:

- What events should be logged?
- What metrics indicate health?
- What traces reveal the execution path?
- What failures are silent today?
- What user-visible symptoms indicate backend problems?
- What data is needed for evaluation or debugging later?

For agent projects, consider events such as request received, model call start/end, tool start/end, memory read/write, stream chunk, error, retry, and final answer.

## Risk Categories

- Setup fragility.
- Missing or stale documentation.
- Unclear entrypoints.
- Silent exceptions.
- Weak input validation.
- Secret leakage.
- Overbroad logging.
- External dependency failures.
- Data loss or unsafe writes.
- Nondeterministic model behavior.
- Missing evaluation artifacts.
- Performance bottlenecks.

## Output

Prioritize findings by impact and fixability. Each finding should include:

```text
Finding:
Evidence:
Impact:
Smallest fix:
How to verify:
Career value:
```
