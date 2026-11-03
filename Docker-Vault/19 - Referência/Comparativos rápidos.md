---
tags:
  - docker
  - referencia
  - comparativo
aliases: []
tipo: comparativo
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Instruções COPY e ADD]]"
  - "[[Instruções CMD e ENTRYPOINT]]"
  - "[[Volume vs bind mount vs tmpfs]]"
  - "[[Compose vs Swarm vs Kubernetes]]"
  - "[[Docker vs Podman]]"
  - "[[Containers vs Máquinas Virtuais]]"
---

# Comparativos rápidos

Resumo dos comparativos mais cobrados. Cada um tem uma nota completa.

## COPY vs ADD

| | `COPY` | `ADD` |
|---|---|---|
| Copia do contexto | Sim | Sim |
| URLs | Não | Sim |
| Extrai `.tar` local | Não | Sim |
| Recomendação | **Preferir** | Só quando necessário |

Detalhes: [[Instruções COPY e ADD]].

## CMD vs ENTRYPOINT

| | `CMD` | `ENTRYPOINT` |
|---|---|---|
| Papel | Comando/argumentos **padrão** | Executável **fixo** |
| Substituído por `docker run IMAGEM x` | **Sim** (por completo) | Não (`x` vira argumento) |
| Juntos | `CMD` fornece argumentos padrão ao `ENTRYPOINT` | |

Detalhes: [[Instruções CMD e ENTRYPOINT]].

## Volume vs bind mount

| | Volume | Bind mount |
|---|---|---|
| Gerenciado por | Docker | Você (caminho do host) |
| Uso ideal | Dados de produção | Código em desenvolvimento, configs |
| Portabilidade | Alta | Baixa |
| Populado pela imagem | Sim (novo) | Não (sobrepõe) |

Detalhes: [[Volume vs bind mount vs tmpfs]].

## ARG vs ENV

| | `ARG` | `ENV` |
|---|---|---|
| Disponível no build | Sim | Sim |
| Disponível ao executar | **Não** | **Sim** |

Detalhes: [[Instruções ENV e ARG]].

## Forma shell vs exec

| | Shell | Exec |
|---|---|---|
| PID 1 | Shell | **Aplicação** |
| Recebe SIGTERM | Geralmente não | **Sim** |

Detalhes: [[Forma shell vs forma exec]].

## Container vs VM

| | Container | VM |
|---|---|---|
| Kernel | Compartilhado | Próprio |
| Inicialização | Segundos | Minutos |

Detalhes: [[Containers vs Máquinas Virtuais]].

## Compose vs Swarm vs Kubernetes

| | Compose | Swarm | Kubernetes |
|---|---|---|---|
| Escopo | 1 host | Cluster pequeno | Qualquer escala |

Detalhes: [[Compose vs Swarm vs Kubernetes]].

## Docker vs Podman

Detalhes: [[Docker vs Podman]].

## Veja também

- [[Instruções COPY e ADD]]
- [[Instruções CMD e ENTRYPOINT]]
- [[Volume vs bind mount vs tmpfs]]
- [[Compose vs Swarm vs Kubernetes]]
- [[Docker vs Podman]]
- [[Containers vs Máquinas Virtuais]]
- [[MOC - Referência - Docker]]
