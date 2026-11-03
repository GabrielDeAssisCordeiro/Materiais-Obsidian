---
tags:
  - docker
  - fundamentos
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O que é Docker]]"
  - "[[Padrão OCI]]"
  - "[[containerd e runc]]"
  - "[[Ecossistema Docker]]"
---

# História do Docker

Containers não nasceram com o Docker. O Docker **popularizou** e **simplificou** tecnologias que já existiam.

## Linha do tempo

| Ano | Marco |
|---|---|
| 1979 | `chroot` (Unix V7) isola o diretório raiz de um processo. |
| 2000 | FreeBSD Jails ampliam o isolamento. |
| 2004 | Solaris Zones. |
| 2002–2008 | O Linux ganha namespaces (a partir de 2002) e cgroups (2007, incorporados ao kernel 2.6.24). |
| 2008 | LXC (Linux Containers) combina namespaces e cgroups. |
| 2013 | **Docker** é apresentado por Solomon Hykes (empresa dotCloud) na PyCon, inicialmente sobre o LXC. |
| 2014 | Docker substitui o LXC pela biblioteca própria `libcontainer`; Google lança o Kubernetes. |
| 2015 | Criação da **Open Container Initiative (OCI)**; `runc` é doado à fundação. |
| 2016 | Docker 1.12 integra o **modo Swarm** ao Engine. |
| 2017 | `containerd` é doado à CNCF; o projeto **Moby** passa a ser a base open source do Docker. |
| 2019 | `containerd` torna-se projeto *graduated* da CNCF. |
| 2023 | O **BuildKit** passa a ser o builder padrão do Engine (versão 23.0). |

> [!info] Fig e Docker Compose
> O Compose descende do projeto **Fig**, adquirido pela Docker em 2014. Hoje o Compose v2 é um plugin da CLI (`docker compose`) escrito em Go.

> [!tip] Por que a história importa
> Entender que Docker = (namespaces + cgroups + union filesystems + boa experiência de uso + formato de imagem portátil) ajuda a compreender por que existem alternativas como Podman e por que o padrão [[Padrão OCI]] foi criado.

## Exercício

Pesquise e escreva em três linhas a diferença entre o projeto Moby e o produto Docker Desktop.

## Veja também

- [[O que é Docker]]
- [[Padrão OCI]]
- [[containerd e runc]]
- [[Ecossistema Docker]]
- [[MOC - Fundamentos - Docker]]
