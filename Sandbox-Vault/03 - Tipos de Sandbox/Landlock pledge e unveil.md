---
tags:
  - tipos
aliases:
  - "Landlock"
  - "pledge"
  - "unveil"
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Processo]]"
  - "[[Seccomp]]"
---
# Landlock pledge e unveil

Mecanismos de **autorrestrição**: o próprio programa reduz o que poderá fazer, de forma irreversível.

| Mecanismo | SO | Ideia |
|---|---|---|
| **Landlock** | Linux (5.13+) | Processo sem privilégios restringe seu acesso ao sistema de arquivos (e, em versões mais novas, a rede) |
| **pledge** | OpenBSD | Declara categorias de syscalls permitidas (`stdio`, `rpath`, ...) |
| **unveil** | OpenBSD | Declara quais caminhos do sistema de arquivos ficam visíveis |

```c
/* OpenBSD: o programa só lê /var/www e usa stdio/rpath depois disso */
unveil("/var/www", "r");
unveil(NULL, NULL);
pledge("stdio rpath", NULL);
```

> [!question] Verificar na documentação oficial
> Recursos de rede do Landlock dependem da versão do kernel (ABI). Consulte a documentação do kernel.

## Veja também

- [[Sandbox de Processo]]
- [[Seccomp]]
- [[Sandbox de Aplicação]]
