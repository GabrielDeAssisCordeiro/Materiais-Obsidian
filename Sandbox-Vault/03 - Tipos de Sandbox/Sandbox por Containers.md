---
tags:
  - tipos
aliases:
  - "Podman"
  - "LXC"
  - "LXD"
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Namespaces do Linux]]"
  - "[[Cgroups]]"
  - "[[Seccomp]]"
  - "[[Criar Sandbox com Docker]]"
  - "[[Criar Sandbox com Podman Rootless]]"
---
# Sandbox por Containers

Containers usam [[Namespaces do Linux]] e [[Cgroups]] para isolar processos **compartilhando o kernel do host**.

| Tecnologia | Característica |
|---|---|
| Docker | Mais popular; daemon (rootless disponível) |
| Podman | Sem daemon; *rootless* por padrão |
| LXC/LXD (Incus) | Containers de sistema, mais próximos de uma VM leve |

**Pontos de endurecimento:** `--read-only`, `--cap-drop=ALL`, `--network none`, `--security-opt no-new-privileges`, limites de recursos, usuário não-root, perfis seccomp/AppArmor.

> [!danger] O kernel é compartilhado
> Vulnerabilidades do kernel afetam todos os containers do host. Para código hostil, considere [[Sandbox por MicroVMs]] ou [[Sandbox por Kernel em Espaço de Usuário]].

## Exercício

Rode um container com todas as restrições acima e confirme com `docker inspect` o que foi aplicado.

## Veja também

- [[Criar Sandbox com Docker]]
- [[Criar Sandbox com Podman Rootless]]
- [[Seccomp]]
- [[Sandbox por Kernel em Espaço de Usuário]]
- [[MOC - Tipos de Sandbox]]
