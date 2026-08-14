---
type: Playbook
title: Dotfiles Repository Quickstart
description: Entry point for the dotfiles repository wiki covering cross-platform bash configuration, AI toolchain setup, skill management, and blueprint-driven development workflow.
tags:
  - quickstart
  - dotfiles
  - bash
  - ai-toolchain
  - blueprint-driven
---

# Dotfiles Repository Quickstart

A personal environment configuration and blueprint-driven Agent development skill repository. Provides idempotent setup for Linux, macOS, and Windows Git Bash environments with integrated AI coding toolchain management.

## Repository Overview

| Area | Path | Purpose |
|:-----|:-----|:--------|
| Shell Config | `rc/bash/` | Source files sourced by `bashrc.personal`: exports, aliases, functions, PATH |
| Install Script | `install.sh` | Idempotent installer: copies configs, injects bashrc source line, renders AI configs |
| Skill Installer | `install_skill.sh` | Interactive ANSI menu for selecting and copying skills to local/global targets |
| Global Rules | `global-agents.md` | AI Coding Constitution distributed to all AI tools during install |
| AI Config Sources | `rc/ai/` | JSONC/YAML templates with `${ENV}` placeholders for mimocode, opencode, hermes |
| Utility Tools | `tools/` | Helper scripts: proxy management, API verification, config rendering |
| Executables | `bin/` | Scripts on PATH: model selector, git helper, proxy manager |
| Blueprint Docs | `docs/` | Product blueprint, project notes, agent domain/issue-tracker config |
| Skills Source | `skills/` | Skill definitions (git-tracked source of truth) |

## First-Time Setup

```bash
git clone https://github.com/wupengbo125/dotfiles.git $github_dir/dotfiles
bash $github_dir/dotfiles/install.sh
```

The installer (`install.sh`) performs these steps idempotently:

1. Copies `rc/gitconfig` to `~/.gitconfig`
2. Injects source line into `~/.bashrc` (deduped via `grep -qF`)
3. Copies `global-agents.md` to AI tool config directories (Claude, Gemini, OpenCode, Cursor, Copilot)
4. Renders AI toolchain configs by replacing `${ENV}` placeholders with real values
5. Makes `bin/*` executable and sources `bashrc.personal`

## Daily Aliases

| Alias | Action |
|:------|:-------|
| `.ba` | Pull latest dotfiles, reinstall, reload bashrc |
| `.baa` | Force-reset to origin/main, reinstall, reload |
| `skills` | Open interactive skill installer |
| `claude` | Launch Claude Code with `--dangerously-skip-permissions` |
| `mihomo` | Start/stop/sort proxy nodes |

## Key Documentation Pages

- **[Architecture Overview](architecture/overview.md)** — Shell sourcing chain, installer flow, cross-platform conditionals
- **[AI Toolchain](ai-toolchain/config-management.md)** — Multi-provider model routing, config rendering pipeline, provider setup
- **[Skill System](skills/skill-management.md)** — Skill source directories, interactive installer, adding new skills
- **[Tools Reference](tools/utilities.md)** — Mihomo proxy manager, NVIDIA API verifier, config renderers
- **[Blueprint Workflow](workflows/blueprint-driven.md)** — Blueprint-driven development: init, build-blueprint, build-change, build-spec, merge
- **[Agent Config](agent-config/global-constitution.md)** — AI Coding Constitution principles distributed to all tools

## Known Pitfalls

- **CRLF on Windows**: Always use LF line endings; `\r` causes `command not found` errors
- **`OSTYPE` is unreliable in Git Bash**: Use `uname -s` for platform detection
- **Skill source vs copy**: `skills/` is the editable source; `.agents/skills/` is the install output — never edit the copy
- **`install.sh` deduplication**: The `grep -qF` check prevents duplicate source lines — do not refactor to `sed`
- **Secrets in `rc/bash/exports`**: Environment variables contain API keys and tokens used for local config rendering; never commit actual secret values

## Backlog

- Cross-platform CI testing (no Windows verification available locally)
- Skill uninstall flow completeness audit
