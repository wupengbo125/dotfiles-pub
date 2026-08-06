# Project Handoff: Skill Consolidation & Documentation Architecture

## 1. Context & Background (背景与动机)

This session focused on simplifying and standardizing the repository's `.agents/skills` and `skills/` architecture. Previously, there were too many overlapping and ambiguously named skills (`build-map`, `build-blueprint`, `merge-to-blueprint`, `build-change`, `chat-req`), causing user confusion and high mental overhead.

Key problems identified during user discussion:
- **Name Confusion**: `chat-req` was confusing; in Python projects `requirements.txt` is standard, making "requirement" ambiguous. `chat-prd` was chosen as the clear entry point for interactive requirement discussions.
- **Skill Bloat**: Multiple disjointed skills (`build-map`, `build-blueprint`, `merge-to-blueprint`) did similar things (updating docs without user interaction).
- **Blueprint Misconceptions**: `BLUEPRINT.md` was previously treated as if every directory needed one. **This is wrong.** `BLUEPRINT.md` is strictly optional and should ONLY exist in directories that define distinct, high-level business rules. `MAP.md` handles structural indexing.
- **Mechanical Updates**: Updating docs should never be mechanical. Internal refactorings (e.g., variable renames, formatting) **must NOT** trigger updates to `BLUEPRINT.md` or `MAP.md`.

---

## 2. Established Architecture & Rules (架构与准则)

### Entry Points & Skill Responsibilities
1. **`chat-prd` (Interactive / 聊需求)**
   - **Trigger**: User says "聊需求", "讨论新想法", "写PRD".
   - **Behavior**: Uses `/grill-me` style multi-turn interview to uncover background, scope, edge cases, and technical steps.
   - **Output**: `docs/prd/<slug>.md` with OKF header (`type: PRD`).

2. **`update-docs` (Non-Interactive / 补文档)**
   - **Trigger**: Called after code implementation or refactoring is finished.
   - **Behavior**: Silently inspects code diffs against `docs/prd/`.
   - **Core Logic**:
     - **Business logic changed?** -> Update `BLUEPRINT.md` (or create if the directory defines core business rules). If no business logic changed (e.g. variable rename, refactor), **do NOT touch `BLUEPRINT.md`**.
     - **Directory/file structure changed?** -> Update `MAP.md` (Mermaid dependency graphs & directory index).
     - **Do NOT create `BLUEPRINT.md` everywhere!** It is strictly optional.

---

## 3. Work Completed in Commit `eb3ff78`

- Removed obsolete skills: `build-change`, `build-spec`, `merge-to-blueprint`, `chat-req`.
- Created/Standardized: `chat-prd` (with `PRD-TEMPLATE.md`) and `update-docs`.
- Root docs updated: `MAP.md` (structure) and `BLUEPRINT.md` (business overview).
- Updated navigation references in `AGENTS.md`, `CLAUDE.md`, and `readme.md`.

---

## 4. Specific Action Items for Next Session (下一会话具体任务)

1. **Refine `skills/update-docs/SKILL.md`**:
   - Verify that Step 2 explicitly states: "`BLUEPRINT.md` is optional. Only create or update `BLUEPRINT.md` if user-facing business logic has changed AND the directory requires business documentation. Never automatically create `BLUEPRINT.md` in every folder."
   - Ensure Step 3 explicitly specifies: "Only update `MAP.md` if file paths, directory structures, or module dependencies have changed."

2. **Validate Skill Files in `skills/`**:
   - Ensure `skills/chat-prd/SKILL.md` and `skills/update-docs/SKILL.md` reflect the exact user consensus and are synced with `.agents/skills/`.

3. **Test Workflow**:
   - Test a sample `chat-prd` flow and an `update-docs` run to verify non-intrusive behavior.
