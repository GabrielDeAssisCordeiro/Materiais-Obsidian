---
tags:
  - docker
  - seguranca
aliases: []
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Capabilities Linux]]"
  - "[[Seccomp - Docker]]"
  - "[[AppArmor e SELinux]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Opções security-opt e no-new-privileges

`--security-opt` ajusta recursos de segurança do container.

| Opção | Efeito |
|---|---|
| `no-new-privileges:true` | Impede que o processo (ou filhos) **ganhe mais privilégios** via setuid/setgid ou capabilities de arquivo |
| `seccomp=perfil.json` | Perfil seccomp customizado |
| `seccomp=unconfined` | **Desativa** o filtro de syscalls (evite) |
| `apparmor=perfil` | Perfil AppArmor |
| `label=type:xxx_t` | Rótulo SELinux |

```bash
# Com no-new-privileges, o sudo/setuid não eleva privilégios
docker run --rm --security-opt no-new-privileges:true --user 10001 alpine:3.20 id

# Ver as opções de segurança ativas no daemon
docker info --format '{{.SecurityOptions}}'
```

```yaml
services:
  app:
    image: alpine:3.20
    command: sleep 600
    security_opt:
      - no-new-privileges:true
```

> [!tip] Quase sempre vale ligar
> `no-new-privileges:true` raramente quebra aplicações e bloqueia uma classe inteira de escalonamento de privilégio dentro do container.

> [!warning] Imagens que dependem de setuid
> Imagens que usam `sudo` ou binários setuid (alguns utilitários de rede) deixam de funcionar com essa opção. Reavalie o design da imagem.

## Exercício

Compare o comportamento de um binário setuid (como `su` ou `ping` em algumas imagens) com e sem `no-new-privileges`.

## Veja também

- [[Capabilities Linux]]
- [[Seccomp - Docker]]
- [[AppArmor e SELinux]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Segurança]]
