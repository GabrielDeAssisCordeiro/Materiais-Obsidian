---
tags:
  - seguranca
aliases:
  - "Patching"
  - "Atualizações"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Endurecimento (Hardening)]]"
---
# Atualização e Patching

Sandboxes são tão seguras quanto suas camadas atualizadas: **kernel, runtime de containers, hipervisor, imagens base e dependências**.

| Componente | Prática |
|---|---|
| Kernel e hipervisor | Aplicar correções de segurança com regularidade |
| Docker/Podman/runc/containerd | Acompanhar *release notes* e avisos |
| Imagens base | Reconstruir com frequência; escanear vulnerabilidades |
| Dependências | Automatizar (ex.: Dependabot/Renovate) |
| VMs de laboratório | Atualizar **antes** de criar o snapshot limpo |

```bash
docker pull alpine:3 && docker image ls
# Escaneamento (exemplo com Trivy, se instalado)
trivy image alpine:3
```

> [!warning] Imagens "congeladas" envelhecem
> Fixar por digest dá reprodutibilidade, mas exige rotina de atualização.

## Exercício

Escaneie uma imagem que você usa e liste as vulnerabilidades de severidade alta.

## Veja também

- [[Fuga de Sandbox]]
- [[Endurecimento (Hardening)]]
- [[MOC - Cuidados e Segurança]]
