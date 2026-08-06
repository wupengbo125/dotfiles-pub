---
type: Plan
title: Dotfiles Wiki Init Plan
description: Temporary plan for wiki init/update — covers accuracy audit, targeted updates, and concept graph verification for the dotfiles repository.
tags:
  - plan
  - init
---

# Wiki Init Plan

## Assessment

The wiki was previously initialized on 2025-08-02 with 7 well-structured pages. All pages have proper OKF front matter and mermaid diagrams. The core content is accurate and grounded in source files.

## Pages to Update

### 1. /openwiki/quickstart.md
- **Status**: Accurate. Minor: verify Backlog section is current.
- **Action**: Keep as-is (content is current and accurate).

### 2. /openwiki/architecture/overview.md
- **Status**: Accurate. Shell sourcing chain, installer flow, and cross-platform design are correctly documented.
- **Action**: Keep as-is.

### 3. /openwiki/ai-toolchain/config-management.md
- **Status**: Accurate. Provider routing, config rendering, and NVIDIA verification documented correctly.
- **Action**: Keep as-is.

### 4. /openwiki/skills/skill-management.md
- **Status**: Mostly accurate. Minor discrepancy: says "250-line bash script" — actual `install_skill.sh` is ~200 lines with the select_menu function. Also SKILL_SOURCES array now has 4 entries (was shown with 3 + custom comment).
- **Action**: Minor accuracy fix: update line count and SKILL_SOURCES count.

### 5. /openwiki/tools/utilities.md
- **Status**: Accurate. All tools correctly described.
- **Action**: Keep as-is.

### 6. /openwiki/workflows/blueprint-driven.md
- **Status**: Accurate. Five-command pipeline with state diagram is correct.
- **Action**: Keep as-is.

### 7. /openwiki/agent-config/global-constitution.md
- **Status**: Accurate. All principles correctly summarized.
- **Action**: Keep as-is.

## Cross-Links and Concept Graph

Existing links:
- quickstart → architecture, ai-toolchain, skills, tools, workflows, agent-config (all valid)
- ai-toolchain → tools/nvidia_api (valid)
- skills → skills source (valid)
- architecture → installer flow (valid)
- workflows → docs (valid)

No orphaned pages. All concept links resolve.

## Actions

1. Fix minor accuracy in skills/skill-management.md (line count, SKILL_SOURCES count)
2. Update .last-update.json timestamp
3. Verify mermaid diagrams render correctly
