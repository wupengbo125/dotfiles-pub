---
type: Blueprint
title: Dotfiles blueprint
description: 跨平台 Shell 环境基础配置管理与 AI 工具链初始化全量业务蓝图
tags:
  - blueprint
  - dotfiles
---

# Dotfiles blueprint

## 目标

为跨平台 Shell 环境（Linux / macOS / Windows Git Bash）提供幂等的基础配置管理与 AI 工具链初始化。

## 功能地图

### 一键安装 dotfiles

- **入口**：用户 clone 仓库后执行 `bash install.sh`。
- **流程**：
  1. 拷 `rc/gitconfig` → `~/.gitconfig`
  2. 注入 source 行到 `~/.bashrc`（带去重）
  3. 拷 `global-agents.md` 到各 AI 工具全局配置（Claude / Gemini / OpenCode / Cursor / Copilot）
  4. 渲染并部署 AI 工具链配置（mimocode / opencode / hermes）
  5. `chmod +x bin/*` 后立即 source `bashrc.personal`
- **出口**：Shell 重启后，`~/.bashrc` 自动 source `rc/bash/bashrc.personal`，所有 alias / 函数 / PATH / 环境变量生效。

### 交互式安装 Skill

- **入口**：在任何目录执行 `skills`（即 `install_skill.sh`）。
- **流程**：
  1. 第一步：↑/↓ 选择目标位置（当前项目 `./.agents/skills` / 用户全局 / 两者都要）。
  2. 第二步：↑/↓ + 空格勾选 Skill，回车确认。
  3. 脚本把 `skills/<name>/*` 拷贝到所选目标目录。
- **出口**：目标目录出现对应 Skill 子目录，agent 启动时自动加载。

### 渲染 AI 工具链配置

- **入口**：`install.sh` 自动调用，或手动 `uv run tools/render_env_to_json_yaml/render.py <targets...>`。
- **流程**：
  1. 读取 `rc/ai/*.jsonc` / `*.yaml` 里的 `${ENV}` 占位符。
  2. 用真实环境变量值替换。
  3. 写到 `~/.config/mimocode/`、`~/.config/opencode/`、`~/.local/share/{mimocode,opencode}/`、`~/.hermes/`。
- **出口**：AI 工具启动时使用最新的 API 配置；hermes 已有 config 时走 `merge.py` 增量合并，不覆盖用户内容。

## 验收要点

- 执行 `install.sh` 不报错，且可反复执行不产生重复注入。
- 在任何项目根目录执行 `skills` 能交互式勾选并把 Skill 正确复制到 `./.agents/skills/`。
- 重新渲染 AI 配置后，重启对应工具能读到新的 token / endpoint。