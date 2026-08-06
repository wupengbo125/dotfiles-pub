# Windows 第三方 CLI 工具装机指南

> 新机器初始化时按这份文档装，配置到 `~/.bashrc`。
> 不进个人 dotfiles（`rc/`），不进 install.sh。

## 安装

winget 一次装多个因 VCRedist 会失败，逐个装：

```bash
winget install --id eza-community.eza              --accept-source-agreements --accept-package-agreements
winget install --id sharkdp.bat                    --accept-source-agreements --accept-package-agreements
winget install --id BurntSushi.ripgrep.MSVC        --accept-source-agreements --accept-package-agreements
winget install --id starship.starship              --accept-source-agreements --accept-package-agreements
winget install --id ajeetdsouza.zoxide             --accept-source-agreements --accept-package-agreements
winget install --id junegunn.fzf                   --accept-source-agreements --accept-package-agreements
```

装完新开 Git Bash。

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

`source ~/.bashrc`。

## 坑

- 装完 PATH 没刷新：新开 shell
- fzf winget 版没 shell 集成，只有二进制；Ctrl-T/Alt-C 走 `git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install`
- starship 是 MSI，装到 `C:\Program Files\starship\bin\`，卸载走"应用和功能"
- bat 实际叫 `bat.exe`，shim 让 `bat` 直接能跑
- zoxide init 必须交互式 shell，`bash -c z` 报 "no match found" 是故意

## 卸载

```bash
winget uninstall eza-community.eza
winget uninstall sharkdp.bat
winget uninstall BurntSushi.ripgrep.MSVC
winget uninstall starship.starship
winget uninstall ajeetdsouza.zoxide
winget uninstall junegunn.fzf
```

清 `~/.bashrc` 对应段。
