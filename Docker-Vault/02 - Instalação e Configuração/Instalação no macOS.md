---
tags:
  - docker
  - instalacao
aliases:
  - Instalar Docker no Mac
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Verificando com hello-world]]"
  - "[[Alternativas ao Docker Desktop]]"
---

# Instalação no macOS

No macOS, containers Linux rodam dentro de uma **VM Linux** gerenciada pelo Docker Desktop. Há versões para **Apple Silicon (arm64)** e **Intel (amd64)**.

## Instalação

1. Baixe o instalador `.dmg` correspondente ao seu processador no site oficial do Docker.
2. Arraste o Docker para a pasta Aplicativos e abra-o.
3. Aguarde o ícone da baleia indicar que o Docker está em execução.

```bash
# Alternativa via Homebrew
brew install --cask docker-desktop
```

> [!question] Verificar na documentação oficial
> O nome da *cask* do Homebrew para o Docker Desktop mudou ao longo do tempo (`docker` e `docker-desktop`). Execute `brew search docker` para confirmar o nome atual.

```bash
docker version
docker run --rm hello-world
```

## Apple Silicon e arquiteturas

Em Macs com chip M, imagens `linux/arm64` rodam nativamente. Imagens apenas `linux/amd64` rodam por **emulação** (QEMU/Rosetta), mais lenta e às vezes instável.

```bash
# Força uma plataforma específica (emulação se for diferente da nativa)
docker run --rm --platform linux/amd64 alpine uname -m

# Plataforma nativa
docker run --rm alpine uname -m
```

> [!bug] "exec format error" ou aviso de plataforma
> Mensagens como *The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64)* indicam imagem de outra arquitetura. Prefira imagens multiplataforma ou use `--platform`.

## Recursos da VM

Em **Settings → Resources**, ajuste CPUs, memória e disco da VM. Em bind mounts, prefira as opções de compartilhamento de arquivos recomendadas pela versão atual do Docker Desktop.

> [!tip] Alternativas leves
> Colima, OrbStack e Rancher Desktop oferecem runtimes compatíveis. Veja [[Alternativas ao Docker Desktop]].

## Exercício

Rode `docker run --rm alpine uname -m` com e sem `--platform linux/amd64` e explique a diferença no resultado (em Apple Silicon).

## Veja também

- [[Docker Desktop vs Docker Engine]]
- [[Verificando com hello-world]]
- [[Alternativas ao Docker Desktop]]
- [[MOC - Instalação e Configuração]]
