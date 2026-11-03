---
titulo: "Terminal (zsh e utilitários)"
tags:
  - sistemas-operacionais
  - ferramenta
  - macos
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[PowerShell]]"
  - "[[grep]]"
  - "[[Permissões de Arquivos]]"
  - "[[MOC - Ferramentas Nativas do macOS]]"
---

# Terminal (zsh e utilitários)

## Finalidade

Aplicativo de emulação de terminal que executa um shell. Desde o macOS Catalina o shell padrão é **zsh** (antes, bash 3.2). Utilitários vêm do **BSD**, não do GNU.

> [!warning] BSD x GNU
> `sed -i` exige argumento (`sed -i '' 's/a/b/' arq`); `ls --color` não existe (use `ls -G`); `date`, `xargs`, `grep` têm flags diferentes. Instale versões GNU com Homebrew (`brew install coreutils gnu-sed`) se precisar.

## Comandos essenciais

```bash
sw_vers                          # versão do macOS
uname -a                         # kernel Darwin/XNU
system_profiler SPHardwareDataType   # hardware
open arquivo.pdf; open -a Safari url # abre com app padrão
pbcopy < arq.txt; pbpaste        # área de transferência
say "olá"                        # voz
caffeinate -d -t 3600            # impede suspensão por 1 h
mdfind "kind:pdf contrato"       # Spotlight na CLI
mdls arquivo                     # metadados
defaults read com.apple.finder   # preferências (plist)
defaults write com.apple.finder AppleShowAllFiles YES && killall Finder
plutil -p arquivo.plist
networksetup -listallhardwareports
ifconfig en0; scutil --dns
softwareupdate --list
xattr -l arquivo; xattr -d com.apple.quarantine app   # quarentena (Gatekeeper)
codesign -dv --verbose=2 /Applications/App.app        # assinatura
spctl --assess -v /Applications/App.app               # Gatekeeper
csrutil status                                        # SIP
```

## Permissões e segurança

- Permissões POSIX + ACLs (`chmod +a`, `ls -le`) ([[Permissões de Arquivos]]).
- **SIP** (*System Integrity Protection*) protege `/System`, `/usr` (exceto `/usr/local`) mesmo contra root.
- **TCC** (*Transparency, Consent, and Control*) controla acesso a câmera, microfone, arquivos; o Terminal precisa de "Acesso Total ao Disco" para certas pastas.
- `sudo` pede senha de admin; `sudo -v` renova.

## Estrutura de diretórios

| Caminho | Conteúdo |
|---|---|
| `/System`, `/usr`, `/bin` | Sistema (volume somente leitura, selado) |
| `/Applications` | Apps |
| `/Users/nome` | Home |
| `/Library` | Configurações globais; `~/Library` do usuário |
| `/opt/homebrew` | Homebrew em Apple Silicon (`/usr/local` em Intel) |
| `/private/var/log` | Logs tradicionais (`/var` é link) |

## Pontos-chave

- zsh por padrão; ferramentas BSD com flags próprias.
- `defaults`, `open`, `pbcopy`, `mdfind` são exclusivos do macOS.
- SIP e TCC limitam até o root.

## Veja também

[[PowerShell]] · [[grep]] · [[MOC - Ferramentas Nativas do macOS]]
