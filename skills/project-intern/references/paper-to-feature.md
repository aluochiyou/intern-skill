# Paper To Feature

Use this when comparing an external paper, benchmark, product, or related repository with the current project. If the user only gives a name, search for and inspect authoritative sources before comparing.

## Source Discovery

When only a name is provided:

1. Search the web for primary sources.
2. Prefer official or authoritative pages: arXiv, OpenReview, ACL Anthology, NeurIPS/ICLR/ICML pages, official project pages, official GitHub repositories, benchmark leaderboards, and vendor docs.
3. Check whether a newer version, code release, follow-up benchmark, or renamed repository exists.
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

## Proposal Format

For each candidate idea, provide:

```text
Idea:
Where it fits:
Required change:
Smallest experiment:
How to evaluate:
Risks:
Cost:
Resume / interview value:
Recommendation:
```

Limit to 1-3 ideas unless the user asks for a broader survey.

## Implementation Boundary

Do not directly rewrite core project logic based on a paper. First produce an experiment plan, prototype scope, or design note. Only implement after the user confirms the chosen idea.
