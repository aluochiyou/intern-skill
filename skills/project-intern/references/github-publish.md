# GitHub Publish

Use this when preparing a local project for GitHub publication.

## Safety First

Publishing can expose private files. Before any remote action, inspect:

- Git status and current branch.
- Existing remotes.
- `.gitignore` coverage.
- `.env`, credentials, tokens, private keys, certificates, cookies, logs, mission outputs, datasets, model weights, archives, and generated build artifacts.
- Large files that may need Git LFS or should be excluded.
- Personal paths, hostnames, API keys, or internal URLs in configs and docs.

Do not run `git push`, `gh repo create`, `gh release create`, or change repository visibility without explicit user confirmation.

## Publish Flow

1. **Readiness scan**
   - Run `scripts/github_publish_plan.py <repo>`.
   - Inspect warnings before planning commands.

2. **Project cleanup**
   - Add or update `.gitignore`.
   - Move secrets to `.env.example` with placeholder values.
   - Decide whether generated outputs belong in Git.
   - Remove caches, build folders, local logs, and private data from tracking.

3. **Project presentation**
   - Ensure README includes purpose, features, quick start, requirements, run commands, tests, project structure, and limitations.
   - Add screenshots or demos only if they are safe and useful.
   - Add license only when the user chooses one.

4. **Git preparation**
   - Review `git status`.
   - Stage intended files only.
   - Commit with a clear message.
   - Confirm branch name, usually `main`.

5. **Remote creation**
   - If GitHub CLI is available and authenticated, use `gh repo create`.
   - Otherwise, give the user commands for adding an existing remote.
   - Choose private by default unless the user explicitly requests public.

6. **Push and verify**
   - Push the selected branch.
   - Open or report the URL.
   - Verify README renders and no obvious secret or unwanted file is visible.

7. **Optional release**
   - Tag only stable milestones.
   - Include release notes with changes, setup, known issues, and artifacts.

## Command Patterns

Private repo creation with GitHub CLI:

```bash
gh repo create OWNER/REPO --private --source . --remote origin --push
```

Public repo creation after confirmation:

```bash
gh repo create OWNER/REPO --public --source . --remote origin --push
```

Existing remote:

```bash
git remote add origin git@github.com:OWNER/REPO.git
git branch -M main
git push -u origin main
```

Release:

```bash
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
gh release create v0.1.0 --notes "Initial release"
```

## Output

Use this structure:

```text
Publish Readiness:
Safety Warnings:
Files To Exclude:
Files To Add Or Improve:
Suggested Commands:
Needs User Confirmation:
After Publish Checks:
```
