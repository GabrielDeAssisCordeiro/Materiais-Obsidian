---
tags:
  - ferramentas
aliases:
  - "LSM"
  - "MAC"
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Endurecimento (Hardening)]]"
  - "[[Sandbox de Processo]]"
---
# Ferramenta - AppArmor e SELinux

Módulos de segurança do Linux (LSM) com **controle de acesso obrigatório** (MAC): definem o que cada programa pode acessar, independentemente do usuário.

| | AppArmor | SELinux |
|---|---|---|
| Modelo | Perfis por caminho | Rótulos (contextos) por objeto |
| Comum em | Ubuntu, Debian, SUSE | RHEL, Fedora |
| Complexidade | Menor | Maior, mais granular |

```bash
sudo aa-status               # AppArmor
getenforce; sestatus         # SELinux
docker run --security-opt apparmor=docker-default alpine:3 true
```

> [!danger] Não desligue o LSM para "fazer funcionar"
> `--security-opt apparmor=unconfined` ou `label=disable` removem uma camada importante. Ajuste o perfil.

## Exercício

Verifique o status do LSM na sua distribuição e identifique o perfil aplicado ao Docker/Podman.

## Veja também

- [[Endurecimento (Hardening)]]
- [[Sandbox de Processo]]
- [[Seccomp]]
- [[MOC - Ferramentas]]
