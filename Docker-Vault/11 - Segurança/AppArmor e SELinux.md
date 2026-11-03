---
tags:
  - docker
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Opções security-opt e no-new-privileges]]"
  - "[[Seccomp - Docker]]"
  - "[[Bind mounts]]"
---

# AppArmor e SELinux

Ambos são sistemas de **controle de acesso obrigatório (MAC)** do Linux, que restringem o que processos podem acessar **mesmo sendo root**.

| | AppArmor | SELinux |
|---|---|---|
| Distribuições típicas | Ubuntu, Debian, SUSE | Fedora, RHEL, CentOS, Rocky |
| Modelo | Perfis por caminho | Rótulos por tipo/contexto |
| Perfil padrão do Docker | `docker-default` | `container_t` (com política de containers) |

## AppArmor

```bash
# Verifica se está ativo
docker info --format '{{.SecurityOptions}}'
sudo aa-status | head

# Usa um perfil específico
docker run --rm --security-opt apparmor=docker-default alpine:3.20 echo ok
```

## SELinux

```bash
# Habilitar no daemon (daemon.json): "selinux-enabled": true

# Rotular montagens de volume
docker run --rm -v "$PWD/dados":/dados:z alpine:3.20 ls /dados   # :z compartilhado
docker run --rm -v "$PWD/dados":/dados:Z alpine:3.20 ls /dados   # :Z privado
```

> [!bug] "Permission denied" em bind mount no Fedora/RHEL
> Quase sempre SELinux bloqueando. Use `:z`/`:Z` no volume em vez de desativar o SELinux.

> [!danger] Não desative o MAC para "fazer funcionar"
> `setenforce 0` ou `--security-opt apparmor=unconfined` removem uma camada valiosa. Investigue o log (`ausearch -m avc`, `journalctl`) e ajuste rótulos ou perfis.

> [!tip] `:Z` com cuidado
> Nunca use `:Z` em diretórios do sistema (`/home`, `/etc`): o rótulo muda para um tipo de uso exclusivo do container.

## Exercício

Se você usa Fedora/RHEL, provoque um erro de acesso com bind mount e resolva usando `:z`. Se usa Ubuntu, liste os perfis com `aa-status` e identifique o do Docker.

## Veja também

- [[Opções security-opt e no-new-privileges]]
- [[Seccomp - Docker]]
- [[Bind mounts]]
- [[MOC - Segurança]]
