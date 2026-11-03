---
tags:
  - docker
  - referencia
  - comparativo
  - podman
aliases: []
tipo: comparativo
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Podman, containerd e nerdctl]]"
  - "[[Modo rootless]]"
  - "[[Alternativas ao Docker Desktop]]"
  - "[[Padrão OCI]]"
---

# Docker vs Podman

| Aspecto | **Docker** | **Podman** |
|---|---|---|
| Arquitetura | Cliente-servidor (daemon `dockerd` + containerd) | **Sem daemon** (fork/exec; cada container é um processo filho) |
| Privilégios | Daemon root por padrão; rootless opcional | **Rootless por padrão** |
| CLI | `docker` | `podman` (compatível; `alias docker=podman`) |
| Compose | `docker compose` (plugin oficial) | `podman compose` (usa um provedor) ou `podman-compose`; também funciona com o Compose via socket do Podman |
| Swarm | Sim | **Não** |
| Pods (agrupar containers) | Não nativo | **Sim** (`podman pod`), compatível com Kubernetes |
| Kubernetes | `kubectl` + Kubernetes no Desktop | `podman kube generate` / `podman kube play` |
| systemd | Via unidades manuais | **Quadlet** (containers como serviços systemd) |
| Build | BuildKit/Buildx | Buildah (Containerfile/Dockerfile) |
| Desktop | Docker Desktop | Podman Desktop |
| macOS/Windows | VM gerenciada pelo Desktop | `podman machine` (VM) |
| Ecossistema e documentação | **Maior** | Crescente (forte em RHEL/Fedora) |
| Extras de produto | Scout, Hub, Model Runner, Offload | Integrações Red Hat |

## Mesmos comandos, pequenas diferenças

```bash
# Docker
docker run -d --name web -p 8080:80 nginx:1.27

# Podman: o registry costuma ser explícito
podman run -d --name web -p 8080:80 docker.io/library/nginx:1.27
```

> [!info] Mesma base de imagens
> Ambos usam imagens **OCI**: o que você constrói em um roda no outro. Veja [[Padrão OCI]].

> [!tip] Quando escolher
> - **Podman**: servidores RHEL/Fedora, segurança rootless e sem daemon, integração com systemd.
> - **Docker**: ecossistema mais amplo, Docker Desktop, Compose e ferramentas de terceiros pensadas para Docker.

> [!question] Verificar na documentação oficial
> Compatibilidade de Compose, redes e rootless no Podman evolui rápido. Confirme detalhes na documentação da versão que você usa.

## Exercício

Execute a mesma stack Compose do seu projeto com Docker e com Podman. Liste três diferenças práticas encontradas.

## Veja também

- [[Podman, containerd e nerdctl]]
- [[Modo rootless]]
- [[Alternativas ao Docker Desktop]]
- [[Padrão OCI]]
- [[MOC - Referência - Docker]]
