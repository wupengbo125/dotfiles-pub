---
type: Reference
title: Utility Tools Reference
description: Proxy management, API verification, and config rendering utilities shipped in the tools/ directory of the dotfiles repository.
tags:
  - tools
  - mihomo
  - proxy
  - nvidia
  - config-rendering
---

# Utility Tools Reference

## Mihomo Proxy Manager

**Path**: `tools/mihomo/mihomo.py`  
**Binary**: `~/bin/mihomo/mihomo` (Mihomo/Clash Meta core)  
**Config**: `tools/mihomo/config.yaml` (deployed to `~/bin/mihomo/config.yaml` by `install.sh`)

A Python wrapper around Mihomo (Clash Meta) that manages proxy node selection via the local REST API at `127.0.0.1:9090`.

### Commands

| Command | Behavior |
|:--------|:---------|
| `mihomo` (no args) | Start Mihomo if not running, find first available node, switch to it |
| `mihomo auto` | Full speed test of all nodes, automatically select the fastest |
| `mihomo man` | Full speed test, then present manual selection prompt |
| `mihomo list` | Print all available proxy node names |
| `mihomo stop` | Kill the Mihomo process |

### How It Works

1. Queries `/providers/proxies/mysub` for available nodes
2. If no nodes respond, starts `~/bin/mihomo/mihomo -d ~/bin/mihomo`
3. Tests each node's latency via `/proxies/PROXY/delay` against `http://www.gstatic.com/generate_204`
4. Switches the active proxy via `PUT /proxies/PROXY` with the selected node name

Source: [`tools/mihomo/mihomo.py`](tools/mihomo/mihomo.py), [`tools/mihomo/config.yaml`](tools/mihomo/config.yaml)

## NVIDIA API Model Verifier

**Path**: `tools/nvidia_api/verify.py`  
**Config**: `tools/nvidia_api/config.yaml`

Tests all configured NVIDIA NIM models by sending a minimal `chat/completions` request with `max_tokens: 5` and measuring response latency. Outputs sorted results and copy-ready `export MODEL_N_N="..."` lines for pasting into `rc/bash/exports`.

Models tested (from config):

- `nvidia/nemotron-3-super-120b-a12b`
- `nvidia/nemotron-3-ultra-550b-a55b`
- `openai/gpt-oss-120b`
- `deepseek-ai/deepseek-v4-flash`
- `qwen/qwen3.5-397b-a17b`
- `deepseek-ai/deepseek-v4-pro`

## Config Renderers

**Path**: `tools/render_env_to_json_yaml/`

| Script | Purpose |
|:-------|:--------|
| `render.py` | Replace `${ENV}` / `$ENV` placeholders in target files using values from `rc/bash/exports` |
| `merge.py` | Incrementally merge `model:` section from source YAML into an existing hermes config without overwriting user content |

Both are invoked via `uv run --no-project` with no virtual environment. Called automatically by `install.sh`.

Source: [`tools/render_env_to_json_yaml/render.py`](tools/render_env_to_json_yaml/render.py), [`tools/render_env_to_json_yaml/merge.py`](tools/render_env_to_json_yaml/merge.py)

## Other Executables (`bin/`)

| Script | Purpose |
|:-------|:--------|
| `claudee` | Interactive Claude model selector — sets Anthropic env vars for chosen provider/model |
| `cm` | One-liner git commit-and-push: `git add . && git commit -m "$msg" && git push` |
| `mihomo` | Wrapper that runs `uv run tools/mihomo/mihomo.py "$@"` |
| `pili` | Launch pili-download tool via `uv run python -m pili_download` |
| `tokaggle` | (Kaggle token helper — 56 bytes) |
