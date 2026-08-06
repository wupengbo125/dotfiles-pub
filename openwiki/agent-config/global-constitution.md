---
type: Reference
title: AI Coding Constitution
description: Global AI behavior rules distributed to all coding tools during install, enforcing simplicity-first, surgical changes, and minimal defensive code.
tags:
  - ai-rules
  - global-agents
  - coding-constitution
  - simplicity
---

# AI Coding Constitution

`global-agents.md` is copied to seven AI tool config locations during `install.sh` execution. It defines behavioral rules that override default LLM coding tendencies.

## Core Principles

### 1. Think Before Coding

- State assumptions explicitly; ask when uncertain
- Present multiple interpretations rather than silently choosing
- Stop and ask when confused — do not guess

### 2. Simplicity First

- Never add functionality beyond what was requested
- Never abstract one-time code
- Never introduce unsolicited flexibility or configurability
- Never write error handling for impossible scenarios
- When asked to remove something, delete it — do not add "deprecated" markers
- If 50 lines suffice, do not write 200

### 3. No Defensive Code for Deterministic Things

Files in the project are always present. Hardcoded paths never change. Do not add `[ -f ]` or `command -v` checks for project-internal resources. Only validate user input and external dependencies.

### 4. No Fallback Plans

If method A works, use method A. If A fails, fix A — do not build method B as a fallback. Fallbacks create bloat and mask root causes.

### 5. Surgical Changes

- Only modify what is strictly necessary
- Do not refactor surrounding working code
- Match existing code style even if it differs from personal preference
- Delete references that became orphaned due to your changes
- Every modified line must trace to a specific user request

### 6. Brief Communication

Keep user-facing responses short and to the point. The user is a leader who cares about results, not code explanations. Answer yes/no questions with yes/no.

## Special Rules

- **Python**: Use UV as the package manager
- **Windows**: Never use `.bat`, `.cmd`, `.ps1` scripts — all automation must use bash (Git Bash)
- **Removal**: When a feature is removed, do not leave any references to it in code, tests, or documentation

## Distribution Targets

| Tool | Config Path |
|:-----|:------------|
| Claude Code | `~/.claude/CLAUDE.md` |
| Gemini | `~/.gemini/GEMINI.md`, `~/.gemini/config/AGENTS.md`, `~/.gemini/antigravity/AGENTS.md` |
| OpenCode | `~/.config/opencode/AGENTS.md` |
| Cursor | `~/.cursor/AGENTS.md` |
| Copilot | `~/.copilot/copilot-instructions.md` |

Source: [`global-agents.md`](global-agents.md)
