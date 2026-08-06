# Linux 第三方 CLI 工具装机指南


## 装什么

- starship
- zoxide
- eza
- bat
- fzf
- ripgrep

安装完给我配置一下，不要配置到dotfile里面，直接配置到~/.bashrc
## ~/.bashrc 末尾追加

```bash
eval "$(starship init bash)"
eval "$(zoxide init bash)"
alias ls='eza --icons'
alias ll='eza --icons -lh'
alias la='eza --icons -lha'
alias tree='eza --icons --tree'
alias cat='bat -pp'
alias catp='bat --plain'
```

