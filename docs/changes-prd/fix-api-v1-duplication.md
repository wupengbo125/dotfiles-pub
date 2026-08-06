# 移除 AI 配置模板中硬编码的路径拼接

## 1. 变更背景

模板文件中 `${AI_API}/v1` 导致渲染后出现重复的 `/v1`（如 `https://api.xiaomimimo.com/v1/v1`）。原因是 `AI_API` 环境变量已包含 `/v1`，模板又追加了一次。

核心原则：**模板不应拼接路径，地址的完整性由环境变量决定。**

## 2. 当前状态

| 文件 | 模板值 | 渲染结果 |
|------|--------|----------|
| `rc/ai/hermes-config.yaml:3` | `base_url: ${AI_API}/v1` | `https://api.xiaomimimo.com/v1/v1` |
| `rc/ai/opencode.jsonc:11` | `"baseURL": "${AI_API}/v1"` | `https://api.xiaomimimo.com/v1/v1` |
| `rc/ai/opencode.jsonc:29` | `"baseURL": "${AI_API_2}/v1"` | `https://integrate.api.nvidia.com/v1` |
| `rc/ai/mimocode.jsonc:11` | `"baseURL": "${AI_API}/v1"` | `https://api.xiaomimimo.com/v1/v1` |
| `rc/ai/mimocode.jsonc:29` | `"baseURL": "${AI_API_2}/v1"` | `https://integrate.api.nvidia.com/v1` |
| `bin/claudee` (6处) | `ANTHROPIC_BASE_URL="${AI_API_2}/v1"` | `https://integrate.api.nvidia.com/v1` |
| `rc/bash/exports:14` | `AI_API_2="https://integrate.api.nvidia.com"` | 缺少 `/v1` |

## 3. 目标状态

模板中零路径拼接。所有 API 地址在环境变量中写完整。

## 4. 本次变更范围

### 4.1 新增或修改

**模板文件（去掉 `/v1`）：**
- `rc/ai/hermes-config.yaml` — `${AI_API}/v1` → `${AI_API}`
- `rc/ai/opencode.jsonc` — 两处 `/v1` 全部去掉
- `rc/ai/mimocode.jsonc` — 两处 `/v1` 全部去掉
- `bin/claudee` — 6 处 `${AI_API_2}/v1` → `${AI_API_2}`

**环境变量（补全地址）：**
- `rc/bash/exports` — `AI_API_2` 从 `https://integrate.api.nvidia.com` 改为 `https://integrate.api.nvidia.com/v1`

### 4.2 明确不变

- `AI_API` 环境变量（已是完整地址）
- 渲染脚本逻辑
- `hermes-config.yaml` 的 merge 逻辑

### 4.3 本次不包含

- 不改变渲染脚本逻辑
- 不改变 `install.sh` 流程

## 5. 受影响的业务流程

`install.sh` → `render.py` 渲染后的配置文件中 `base_url` / `baseURL` 值直接使用环境变量，不再拼接。

## 6. 验收标准

- 渲染后 `~/.hermes/config.yaml` 中 `base_url` 为 `https://api.xiaomimimo.com/v1`（无重复）
- 渲染后 `~/.config/mimocode/mimocode.jsonc` 和 `~/.config/opencode/opencode.jsonc` 中两个 provider 的 `baseURL` 均无 `/v1` 重复
- `bin/claudee` 选择 Provider 2 时 `ANTHROPIC_BASE_URL` 正确指向 nvidia