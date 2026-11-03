---
tags:
  - como-criar
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Aplicação]]"
  - "[[Seccomp]]"
  - "[[Criar Sandbox com Bubblewrap]]"
---
# Criar Sandbox com Firejail

O **Firejail** é um utilitário SUID para Linux que usa namespaces, seccomp e capabilities para confinar programas.

```bash
sudo apt install firejail

# Shell isolado: home temporário, sem rede, sem capabilities, com seccomp
firejail --private --net=none --caps.drop=all --seccomp --nonewprivs --noroot \
         --private-dev --nosound --no3d bash

firejail --list      # sandboxes ativas
firejail --tree      # árvore de processos
```

Perfis prontos ficam em `/etc/firejail/*.profile`.

```bash
# Restringir um aplicativo com perfil existente
firejail --net=none --private=~/sandbox-home firefox
```

> [!warning] O Firejail é SUID-root
> Isso aumenta a superfície de ataque do próprio utilitário (houve vulnerabilidades históricas). Mantenha-o atualizado e avalie [[Criar Sandbox com Bubblewrap]] como alternativa.

## Exercício

Execute um navegador com `--private --net=none` e confirme que ele não carrega páginas nem enxerga seu `home`.

## Veja também

- [[Criar Sandbox com Bubblewrap]]
- [[Sandbox de Aplicação]]
- [[Seccomp]]
- [[MOC - Como Criar]]
