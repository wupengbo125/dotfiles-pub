# dotfiles

个人环境配置与蓝图驱动（Blueprint-Driven）Agent 开发技能库。

## 1. 首次初始化与安装

在全新机器上部署：

**Step 1**: 配置 Git 凭据

```bash
echo 'https://YOUR_USERNAME:YOUR_GITHUB_TOKEN@github.com' > ~/.git-credentials
```

**Step 2**: Clone 仓库并一键安装

```bash
git clone https://github.com/wupengbo125/dotfiles.git $github_dir/dotfiles
bash $github_dir/dotfiles/install.sh
```

---

## 2. 快捷别名与配置更新 (Aliases)

仓库配置或环境变量更新后，可直接使用以下快捷别名一键拉取并刷新：

- **`.ba`**：更新最新 dotfiles，重新运行安装并重载 `~/.bashrc`
  ```bash
  .ba
  ```
- **`.baa`**：强制重置同步远端最新 dotfiles 并重载 `~/.bashrc`
  ```bash
  .baa
  ```

---

## 3. Skill 技能安装与管理

运行交互式技能安装工具（选择安装到当前项目 `./.agents/skills` 或全局）：

```bash
skills
```

第三方 Skill 快捷安装：

```bash
matt        # 快捷安装 Matt Pocock 的 skills (npx skills)
superpower  # 快捷拉取 superpowers 技能库
```

---

## 4. 蓝图驱动开发工作流 (Blueprint-Driven Workflow)

| 技能命令 | 作用说明 |
| :--- | :--- |
| **`/init-blueprint-driven`** | 项目起步：初始化全局 Agent 导航区块 (`AGENTS.md` / `CLAUDE.md`) |
| **`/build-map`** | 结构地图：扫描项目代码与文件，生成层级导航地图 (`MAP.md`) |
| **`/chat-prd`** | 聊需求：通过交互对话澄清需求，落地需求方案书 (`docs/prd/<slug>.md`) |
| **`/build-blueprint`** | 业务蓝图：综合代码事实与需求方案，沉淀全量业务蓝图 (`BLUEPRINT.md`) |
| **`/update-docs`** | 智能维护：开发与重构完成后，按需增量更新 `MAP.md` 与 `BLUEPRINT.md` |
| **`/build-flowchart`** | 可视化流程：生成产品用户操作流程 HTML 流程图 (`docs/graph.html`) |
