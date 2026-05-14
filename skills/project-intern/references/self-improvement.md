# Self Improvement

Use this process to let model judgment improve the skill without turning it into a bloated assistant.

## Principle

Scripts collect stable evidence. The model reflects on task quality. The skill changes only when a recurring weakness is clear.

Do not add a new capability just because it is possible. Add or change something only if it reduces repeated reasoning, prevents a common error, improves safety, or makes outputs easier to evaluate.

## Loop

```text
run project-intern on a real task
-> save artifacts and outcome
-> score the session with the rubric
-> identify the lowest dimensions
-> ask why the skill failed
-> propose the smallest change
-> validate the skill
-> use it again on a similar task
```

## Model Reflection Prompt

Use this prompt internally when reflecting:

```text
Evaluate this project-intern session using references/evaluation-rubric.md.

Task:
<task>

Output or summary:
<output>

Artifacts:
<artifact paths or summaries>

For each low-scoring dimension, answer:
1. Was this a one-time execution mistake or a skill design problem?
2. Would a script, reference checklist, output template, or main SKILL.md change prevent it?
3. What is the smallest change?
4. What should not be added because it would bloat the skill?
```

## Patch Policy

- Prefer `references/` for reasoning guidance.
- Prefer `scripts/` for repeated deterministic actions.
- Keep `SKILL.md` short and focused on routing and rules.
- Delete or merge redundant guidance when adding new guidance.
- Validate after every change with `quick_validate.py`.

## Session Artifacts

Store project-local artifacts under:

```text
docs/intern/
├── PROJECT_MAP.md
├── ENV_DOCTOR.md
├── LEARNING_LOG.md
├── SESSION_SCORES.jsonl
└── SKILL_FEEDBACK.md
```
