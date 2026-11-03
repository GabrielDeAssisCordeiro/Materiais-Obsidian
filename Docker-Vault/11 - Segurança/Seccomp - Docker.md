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
  - "[[Capabilities Linux]]"
  - "[[AppArmor e SELinux]]"
---

# Seccomp - Docker

O **seccomp** (secure computing mode) filtra as **chamadas de sistema (syscalls)** que um processo pode fazer. O Docker aplica por padrão um **perfil seccomp** que bloqueia dezenas de syscalls perigosas ou raramente necessárias (por exemplo, `reboot`, `kexec_load`, `mount` sem capability).

```bash
# Confirma que o seccomp está ativo (campo Seccomp: 2 = filtro)
docker run --rm alpine:3.20 grep Seccomp /proc/self/status

# Sem filtro (SOMENTE para diagnóstico em laboratório)
docker run --rm --security-opt seccomp=unconfined alpine:3.20 grep Seccomp /proc/self/status
```

## Perfil customizado

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [
    {
      "names": ["read", "write", "exit", "exit_group", "futex", "brk", "mmap", "munmap",
                "rt_sigaction", "rt_sigprocmask", "openat", "close", "fstat", "execve",
                "arch_prctl", "set_tid_address", "set_robust_list", "prlimit64", "getrandom",
                "newfstatat", "mprotect", "pread64", "rseq", "clock_nanosleep", "nanosleep"],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

```bash
docker run --rm --security-opt seccomp=./perfil.json alpine:3.20 echo ola
```

> [!question] Verificar na documentação oficial
> A lista mínima de syscalls varia por imagem, arquitetura e versão. O perfil acima é um **ponto de partida ilustrativo** e provavelmente exigirá ajustes. Parta do perfil padrão do Docker (publicado no repositório Moby) e remova o que não precisa.

> [!tip] Como descobrir as syscalls necessárias
> Execute a aplicação sob `strace -c -f` ou use ferramentas que geram perfis a partir de execução. Teste bastante antes de produção, pois uma syscall bloqueada causa erros difíceis de diagnosticar.

> [!danger] Nunca use `seccomp=unconfined` em produção
> Remove uma barreira importante contra exploração do kernel.

## Exercício

Verifique o campo `Seccomp` em `/proc/self/status` com e sem `--security-opt seccomp=unconfined` e explique os valores.

## Veja também

- [[Opções security-opt e no-new-privileges]]
- [[Capabilities Linux]]
- [[AppArmor e SELinux]]
- [[MOC - Segurança]]
