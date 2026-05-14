# Frontier Technology Radar

Use this when comparing an external paper, benchmark, product, or related repository with the current project. Also use it when the user asks to analyze the current project, pick a technical point, and research the latest related projects, papers, methods, benchmarks, and tools.

## Technical Point Selection

If the user has not chosen a technical point:

1. Read the project map, README, entrypoints, dependency files, and major modules.
2. Optionally run `scripts/extract_tech_points.py <repo>` to get candidate points.
3. Prefer points that are central to the project and have active outside innovation.
4. Offer 3-5 candidates, then choose one with the user. If the user asks you to decide, choose the point with the clearest project impact.

Good candidates include:

- Agent loop, tool calling, memory, retrieval, evaluation, observability.
- Data pipeline, dataset construction, labeling, benchmark design.
- Planning, scheduling, routing, state management, plugin architecture.
- Deployment, sandboxing, security, permission control, monitoring.
- Model provider abstraction, prompt management, trace compression.

## Source Discovery

When only a name is provided:

1. Search the web for primary sources.
2. Prefer official or authoritative pages: arXiv, OpenReview, ACL Anthology, NeurIPS/ICLR/ICML pages, official project pages, official GitHub repositories, benchmark leaderboards, release notes, and vendor docs.
3. Check whether a newer version, code release, follow-up benchmark, renamed repository, or deprecation exists.
4. Use secondary summaries only to find primary sources, not as the main evidence.
5. Record URLs and access dates in the final answer when recency matters.

If the source is a GitHub project, inspect README, examples, paper links, issues/discussions if useful, and core implementation files. If it is a paper, inspect abstract, method, experiments, limitations, and available code.

## Extraction

Summarize the source in engineering terms:

1. Core problem.
2. Main method.
3. Required data or infrastructure.
4. Claims and evidence.
5. Assumptions.
6. Failure modes or limitations.

Avoid copying abstract language. Convert claims into implementable mechanisms.

## Mapping

Map the source to the current project:

- Current module that could adopt the idea.
- Missing dependency or data.
- Input/output changes.
- New storage, schema, event, metric, or UI requirement.
- Test or evaluation method needed to prove value.

Mark each mapping as:

- **Directly transferable**: fits existing architecture with small changes.
- **Adaptable**: useful idea, but needs simplification or different assumptions.
- **Research only**: informative, but not worth implementing now.
- **Not worth it**: popular or impressive, but too costly, too immature, unsupported by evidence, or misaligned with this project.

## Value Judgment

Do not treat "latest" or "popular" as automatically valuable. Judge each source by:

1. **Project fit**: Does it solve a problem this project actually has?
2. **Evidence**: Does it have experiments, benchmarks, users, stars/issues, or working code?
3. **Maturity**: Is it maintained and reproducible?
4. **Integration cost**: Can it be tested in a small experiment?
5. **Risk**: Does it add security, reliability, maintenance, or data-quality risk?
6. **Evaluation path**: Can the benefit be measured?
7. **Learning value**: Will it help the user understand or improve the project?

## Proposal Format

For each candidate idea, provide:

```text
Technical point:
Idea:
Where it fits:
Required change:
Smallest experiment:
How to evaluate:
Evidence:
Risks:
Cost:
Recommendation:
```

Limit to 1-3 ideas unless the user asks for a broader survey.

## Implementation Boundary

Do not directly rewrite core project logic based on a paper. First produce an experiment plan, prototype scope, or design note. Only implement after the user confirms the chosen idea.
