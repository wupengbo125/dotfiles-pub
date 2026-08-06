#!/bin/bash
DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"
BASHRC="$HOME/.bashrc"
echo "Installing dotfiles from $DOTFILES_DIR ..."

# gitconfig
cp "$DOTFILES_DIR/rc/gitconfig" "$HOME/.gitconfig"

# bashrc source line (清理旧路径，写新路径)
sed -i '\|shell/bashrc.personal|d' "$BASHRC"
grep -qF "rc/bash/bashrc.personal" "$BASHRC" || echo ". \"$DOTFILES_DIR/rc/bash/bashrc.personal\"" >> "$BASHRC"

# vimrc source line (清理旧路径，写新路径)
VIMRC="$HOME/.vimrc"
sed -i '\|dotfiles.*vimrc|d' "$VIMRC" 2>/dev/null
echo "source $DOTFILES_DIR/rc/bash/vimrc" >> "$VIMRC"

# mihomo
[ -d "$HOME/bin/mihomo" ] && cp -f "$DOTFILES_DIR/tools/mihomo/config.yaml" "$HOME/bin/mihomo/config.yaml"

# rules
for t in "$HOME/.claude/CLAUDE.md" "$HOME/.gemini/GEMINI.md" "$HOME/.gemini/config/AGENTS.md" "$HOME/.gemini/antigravity/AGENTS.md" "$HOME/.config/opencode/AGENTS.md" "$HOME/.cursor/AGENTS.md" "$HOME/.copilot/copilot-instructions.md"; do
    mkdir -p "$(dirname "$t")" && cp -f "$DOTFILES_DIR/global-agents.md" "$t"
done

# render AI JSON configs
mkdir -p "$HOME/.config/mimocode" "$HOME/.config/opencode"
cp -f "$DOTFILES_DIR/rc/ai/mimocode.jsonc" "$HOME/.config/mimocode/mimocode.jsonc"
cp -f "$DOTFILES_DIR/rc/ai/opencode.jsonc" "$HOME/.config/opencode/opencode.jsonc"
mkdir -p "$HOME/.local/share/mimocode" "$HOME/.local/share/opencode"
cp -f "$DOTFILES_DIR/rc/ai/mimo_opencode_auth.json" "$HOME/.local/share/mimocode/auth.json"
cp -f "$DOTFILES_DIR/rc/ai/mimo_opencode_auth.json" "$HOME/.local/share/opencode/auth.json"
# merge hermes config (若 ~/.hermes/config.yaml 存在)
uv run --no-project "$DOTFILES_DIR/tools/render_env_to_json_yaml/merge.py" "$DOTFILES_DIR/rc/ai/hermes-config.yaml" "$HOME/.hermes/config.yaml"

# render all target configs
uv run --no-project "$DOTFILES_DIR/tools/render_env_to_json_yaml/render.py" "$HOME/.config/mimocode/mimocode.jsonc" "$HOME/.config/opencode/opencode.jsonc" "$HOME/.local/share/mimocode/auth.json" "$HOME/.local/share/opencode/auth.json" "$HOME/.hermes/config.yaml"

# chmod bin
chmod +x "$DOTFILES_DIR/bin/"*

# source now
. "$DOTFILES_DIR/rc/bash/bashrc.personal"
echo "Done! Restart your shell or run: source ~/.bashrc"
