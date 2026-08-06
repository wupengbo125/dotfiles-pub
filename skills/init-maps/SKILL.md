---
name: init-maps
description: 初始化项目的结构地图（MAP.md）、业务蓝图（BLUEPRINT.md）与 AGENTS.md 导航区块。在新建项目或初始化文档体系时使用。
---

# Init Maps

初始化项目的完整文档与导航体系：
1. **`MAP.md`**：记录物理文件结构与模块依赖地图。
2. **`BLUEPRINT.md`**：记录产品业务逻辑与功能规约（可选，有明确业务时创建）。
3. **`AGENTS.md` 导航区块**：注入项目导航索引，引导 AI 优先查阅相关文档。

## 流程

### Step 1: 扫盘与 OpenWiki 检测
- 检查项目根目录是否存在 `openwiki/` 目录：
  - **若存在 `openwiki/`**：跳过 `MAP.md` 的生成（代码结构与依赖图由 OpenWiki 负责），仅专注初始化 `BLUEPRINT.md`、`user-say.md` 与导航区块。
  - **若不存在 `openwiki/`**：按正常流程初始化 `MAP.md` 与 `BLUEPRINT.md`。
- 遍历项目目录结构，分析主要模块与核心业务边界。

### Step 2: 建立结构地图 (MAP.md)
- **注意**：若 Step 1 检测到 `openwiki/` 目录存在，则**跳过此步骤**。
- 读取本 skill 目录下的 `MAP-TEMPLATE.md` 模板。
- 根据当前项目实际代码结构生成根目录及各独立子模块/子目录下的 `MAP.md`。

### Step 3: 建立业务蓝图 (BLUEPRINT.md)
- 如果项目（或具体子模块）包含产品业务逻辑，读取本 skill 目录下的 `BLUEPRINT-TEMPLATE.md` 模板，在根目录及对应子目录下生成 `BLUEPRINT.md` 描述产品功能规约与架构设计。
- 若项目或子模块为纯工具/配置库且无独立业务，可跳过此文件。

### Step 4: 创建用户指令文件 (user-say.md)
- 若项目根目录下尚不存在 `user-say.md`，则创建该文件并填入初始注释：
  ```markdown
  <!-- 用户可以在这里写一些对 AI 说的话/全局指令 -->
  ```

### Step 5: 注入项目导航区块 (AGENTS.md & CLAUDE.md)
在项目根目录的 `AGENTS.md`（并同步复制至 `CLAUDE.md`）中插入或更新以下导航区块：

```markdown
<!-- PROJECT-NAV:START -->
## Project Navigation

Before analysis or coding, check and read existing files:

- `user-say.md` — user instructions
- `MAP.md` — Project structure & file index
- `BLUEPRINT.md` — Product business blueprint
- `docs/prd/` — Active requirements & implementation plans
- `docs/adr/` — Architecture decision records
<!-- PROJECT-NAV:END -->
```

仅保留项目实际存在的文件项目。

### Step 6: 报告完成
- 告知用户 `MAP.md`、`BLUEPRINT.md`、`user-say.md` 及导航区块已初始化完成。
