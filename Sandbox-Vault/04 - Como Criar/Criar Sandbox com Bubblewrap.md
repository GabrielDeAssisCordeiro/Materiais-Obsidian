---
tags:
  - como-criar
aliases:
  - "Bubblewrap"
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Aplicação]]"
  - "[[Namespaces do Linux]]"
  - "[[Criar Sandbox com Firejail]]"
---
# Criar Sandbox com Bubblewrap

**Bubblewrap** (`bwrap`) é a ferramenta de baixo nível usada pelo Flatpak. Cria sandboxes com namespaces sem precisar de root (em geral).

```bash
sudo apt install bubblewrap

mkdir -p work
bwrap \
  --ro-bind /usr /usr \
  --symlink usr/bin /bin --symlink usr/lib /lib --symlink usr/lib64 /lib64 \
  --proc /proc --dev /dev --tmpfs /tmp \
  --bind "$PWD/work" /work \
  --unshare-all \
  --die-with-parent --new-session \
  --chdir /work \
  /bin/sh -c 'echo "olá da sandbox"; ls /; id'
```

| Opção | Efeito |
|---|---|
| `--ro-bind` | Monta caminho do host como somente leitura |
| `--bind` | Monta com escrita (use só na pasta de trabalho) |
| `--unshare-all` | Novos namespaces (inclui rede) |
| `--die-with-parent` | Encerra se o pai morrer |
| `--new-session` | Mitiga injeção de teclas via terminal |

> [!tip] Comece de nada e adicione
> Monte apenas o que o programa precisa. Se falhar, descubra o que faltou, em vez de liberar tudo.

## Exercício

Rode `ls /home` dentro da sandbox. O que aparece? Depois adicione `--ro-bind /etc/hostname /etc/hostname` e verifique.

## Veja também

- [[Criar Sandbox com Firejail]]
- [[Sandbox de Aplicação]]
- [[Namespaces do Linux]]
- [[MOC - Como Criar]]
