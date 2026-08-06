# nvidia_api

检查 NVIDIA NIM API 哪些模型可用且响应快。

## 用法

```bash
uv run tools/nvidia_api/verify.py
```

## AI 操作指南

1. 运行 `uv run tools/nvidia_api/verify.py`
2. 复制输出结果中的 `export MODEL_2_N="..."` 粘贴到 `rc/bash/exports`
3. 同步更新 `rc/ai/mimocode.jsonc` 和 `rc/ai/opencode.jsonc` 的模型条目数量
