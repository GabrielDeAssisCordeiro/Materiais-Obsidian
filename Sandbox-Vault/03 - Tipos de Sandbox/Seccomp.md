---
tags:
  - tipos
aliases:
  - "seccomp-bpf"
  - "Filtro de syscalls"
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Processo]]"
  - "[[Capabilities do Linux]]"
  - "[[Sandbox por Containers]]"
---
# Seccomp

**Seccomp** é um recurso do kernel Linux que restringe as **chamadas de sistema** (syscalls) que um processo pode fazer.

- **Modo estrito:** só permite `read`, `write`, `_exit` e `sigreturn` (uso muito limitado).
- **Modo filtro (seccomp-bpf):** um programa BPF decide, por syscall e argumentos, se **permite**, **bloqueia** (com erro), **mata** o processo ou **registra**.

O Docker aplica um perfil seccomp padrão que bloqueia dezenas de syscalls perigosas.

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "syscalls": [
    {
      "names": ["read","write","exit","exit_group","futex","brk","mmap","munmap","rt_sigreturn","close","fstat","openat"],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

```bash
# Uso com Docker (perfil restritivo próprio; ajuste a lista conforme o programa)
docker run --rm --security-opt seccomp=perfil.json alpine:3 echo ola
```

> [!warning] Perfis restritivos exigem teste
> Um perfil mínimo quebra a maioria dos programas (faltam syscalls como `execve`). Gere o perfil observando o programa (ex.: com `strace -c`) e itere.

> [!danger] Nunca use `seccomp=unconfined` em sandbox
> Isso desliga o filtro e aumenta muito a superfície de ataque.

## Exercício

Use `strace -c -f ls` e anote as syscalls usadas. Quais você precisaria liberar em um perfil mínimo?

## Veja também

- [[Sandbox de Processo]]
- [[Capabilities do Linux]]
- [[Sandbox por Containers]]
- [[Criar Sandbox com Docker]]
