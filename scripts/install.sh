#!/usr/bin/env bash
set -euo pipefail

# One-command installer for Project Intern Skill.
#
# Local usage:
#   bash scripts/install.sh --platform codex
#
# Remote usage after publishing:
#   PROJECT_INTERN_REPO_URL=https://github.com/OWNER/project-intern-skill.git \
#     bash -c "$(curl -fsSL https://raw.githubusercontent.com/OWNER/project-intern-skill/main/scripts/install.sh)" -- --platform codex

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ -d "${REPO_ROOT}/skills/project-intern" ]]; then
  python "${REPO_ROOT}/scripts/install.py" "$@"
  exit 0
fi

if [[ -z "${PROJECT_INTERN_REPO_URL:-}" ]]; then
  echo "PROJECT_INTERN_REPO_URL is required for remote one-command install." >&2
  echo "Example:" >&2
  echo "  PROJECT_INTERN_REPO_URL=https://github.com/OWNER/project-intern-skill.git bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/OWNER/project-intern-skill/main/scripts/install.sh)\" -- --platform codex" >&2
  exit 2
fi

tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT
git clone --depth 1 "${PROJECT_INTERN_REPO_URL}" "${tmpdir}/project-intern-skill"
python "${tmpdir}/project-intern-skill/scripts/install.py" "$@"
