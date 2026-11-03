---
tags:
  - docker
  - instalacao
aliases:
  - Instalar Docker no Windows
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Verificando com hello-world]]"
  - "[[Alternativas ao Docker Desktop]]"
  - "[[Autocompletar do Docker CLI]]"
---

# Instalação no Windows com WSL2

No Windows, o caminho recomendado é o **Docker Desktop com backend WSL 2**. O WSL 2 executa um kernel Linux real em uma VM leve, com bom desempenho de arquivos dentro do sistema de arquivos Linux.

> [!question] Verificar na documentação oficial
> Requisitos mínimos exatos (builds do Windows 10/11, edições, virtualização) mudam com as versões. Confira "Install Docker Desktop on Windows" na documentação oficial.

## Pré-requisitos gerais

- Windows 11 ou Windows 10 atualizado (64 bits).
- Virtualização habilitada na BIOS/UEFI.
- WSL 2 instalado.

## Passo a passo

```powershell
# 1. Em um PowerShell como Administrador: instala WSL 2 e uma distribuição (Ubuntu por padrão)
wsl --install

# Reinicie o computador se solicitado.

# 2. Atualize o kernel do WSL e confirme que a distribuição usa a versão 2
wsl --update
wsl --list --verbose
```

3. Baixe o instalador do Docker Desktop no site oficial e execute-o. Mantenha marcada a opção **Use WSL 2 instead of Hyper-V**.
4. Abra o Docker Desktop, aceite os termos e aguarde o status "Engine running".
5. Teste:

```powershell
docker version
docker run --rm hello-world
```

## Integração com distribuições WSL

Em **Settings → Resources → WSL Integration**, habilite a integração para sua distribuição (Ubuntu, por exemplo) e use `docker` direto no terminal Linux.

> [!tip] Desempenho
> Mantenha o código do projeto **dentro do sistema de arquivos do WSL** (por exemplo `~/projetos`), e não em `C:\Users\...` acessado via `/mnt/c`. Bind mounts do Windows são significativamente mais lentos.

## Containers Windows

O Docker Desktop também pode alternar para **containers Windows** (menu da bandeja → *Switch to Windows containers*), usados para aplicações .NET Framework. Neste material usamos **containers Linux**, que são a maioria dos casos.

> [!bug] Problemas comuns
> - *WSL 2 installation is incomplete*: execute `wsl --update` e reinicie.
> - *Virtualization disabled*: habilite VT-x/AMD-V na BIOS.
> - Docker Desktop lento ou consumindo muita memória: limite recursos em `%UserProfile%\.wslconfig`:
> ```ini
> [wsl2]
> memory=6GB
> processors=4
> ```
> Depois execute `wsl --shutdown` para aplicar.

## Exercício

Instale o Docker Desktop com WSL2, habilite a integração com sua distribuição e rode `docker run --rm hello-world` de dentro do terminal Linux.

## Veja também

- [[Docker Desktop vs Docker Engine]]
- [[Verificando com hello-world]]
- [[Alternativas ao Docker Desktop]]
- [[Autocompletar do Docker CLI]]
- [[MOC - Instalação e Configuração]]
