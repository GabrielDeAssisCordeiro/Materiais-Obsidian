---
tags:
  - docker
  - ia
  - novidades
  - podman
  - containerd
  - comparativo
aliases: []
tipo: comparativo
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker vs Podman]]"
  - "[[containerd e runc]]"
  - "[[Padrão OCI]]"
  - "[[Alternativas ao Docker Desktop]]"
---

# Podman, containerd e nerdctl

Graças ao [[Padrão OCI]], há várias ferramentas compatíveis com imagens e containers Docker.

| Ferramenta | O que é | Destaques |
|---|---|---|
| **Podman** | Engine **sem daemon** (Red Hat) | Rootless por padrão, CLI compatível com Docker, *pods*, integração com systemd (Quadlet) |
| **containerd + nerdctl** | Runtime + CLI compatível com Docker | CLI `nerdctl` estilo Docker sobre o containerd; recursos como *lazy pulling* e imagens criptografadas |
| **CRI-O** | Runtime focado em Kubernetes | Leve, usado principalmente em OpenShift/Kubernetes |
| **Buildah / Skopeo** | Construir imagens / copiar entre registries | Complementam o Podman |

## Compatibilidade de comandos

```bash
# Podman (alias de compatibilidade)
alias docker=podman
podman run -d --name web -p 8080:80 docker.io/library/nginx:1.27
podman ps

# nerdctl (containerd)
nerdctl run -d --name web -p 8080:80 nginx:1.27
nerdctl compose up -d
```

> [!info] Nomes completos no Podman
> O Podman pede o registry nas imagens (`docker.io/library/nginx`) ou configuração de `unqualified-search-registries`.

> [!tip] Quando considerar
> - **Podman**: servidores RHEL/Fedora, segurança rootless e sem daemon.
> - **nerdctl**: ambientes baseados em containerd (inclusive Kubernetes) e laboratórios de runtime.
> - **Docker**: ecossistema mais amplo (Desktop, Compose, Scout, Hub) e a maior base de conhecimento.

Veja a comparação detalhada em [[Docker vs Podman]].

## Exercício

Instale o Podman (ou nerdctl) em uma VM e execute os mesmos três comandos que usou no Docker (`run`, `ps`, `logs`), anotando as diferenças.

## Veja também

- [[Docker vs Podman]]
- [[containerd e runc]]
- [[Padrão OCI]]
- [[Alternativas ao Docker Desktop]]
- [[MOC - IA e Novidades]]
