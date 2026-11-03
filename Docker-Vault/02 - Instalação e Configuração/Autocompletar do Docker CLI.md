---
tags:
  - docker
  - instalacao
  - cli
  - produtividade
  - shell
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Docker CLI e API]]"
  - "[[Instalação no Linux]]"
  - "[[Instalação no Windows com WSL2]]"
---

# Autocompletar do Docker CLI

O Docker CLI gera scripts de autocompletar para vários shells com o comando `docker completion`.

## Bash

```bash
# Requer o pacote bash-completion (sudo apt-get install bash-completion)
echo 'source <(docker completion bash)' >> ~/.bashrc
source ~/.bashrc
```

## Zsh

```bash
mkdir -p ~/.zfunc
docker completion zsh > ~/.zfunc/_docker

# Adicione ao ~/.zshrc, antes de compinit:
#   fpath=(~/.zfunc $fpath)
#   autoload -Uz compinit && compinit
```

## Fish

```bash
docker completion fish > ~/.config/fish/completions/docker.fish
```

## PowerShell

```powershell
# Carrega na sessão atual
docker completion powershell | Out-String | Invoke-Expression

# Para persistir, adicione a linha acima ao seu $PROFILE
```

> [!tip] O que ele completa
> Subcomandos, flags e, em muitos casos, nomes de containers, imagens, redes e volumes existentes (ex.: `docker exec <TAB>`).

> [!question] Verificar na documentação oficial
> O comando `docker completion` depende da versão da CLI (disponível nas versões modernas). Em versões antigas, os scripts vinham do pacote da distribuição.

## Exercício

Habilite o autocompletar no seu shell e teste digitando `docker con` seguido de TAB.

## Veja também

- [[Docker CLI e API]]
- [[Instalação no Linux]]
- [[Instalação no Windows com WSL2]]
- [[MOC - Instalação e Configuração]]
