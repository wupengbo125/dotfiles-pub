# render_env_to_json_yaml

环境变量渲染与 YAML 配置合并工具。

## 用法

1. **合并结构**（如果目标文件存在，将模板 YAML 键值合并/增补至目标文件）：
```bash
uv run tools/render_env_to_json_yaml/merge.py rc/ai/hermes-config.yaml ~/.hermes/config.yaml
```

2. **环境变量渲染**（原地替换目标文件中的 `$VAR` 或 `${VAR}`）：
```bash
uv run tools/render_env_to_json_yaml/render.py ~/.config/mimocode/mimocode.jsonc ~/.config/opencode/opencode.jsonc ~/.hermes/config.yaml
```
