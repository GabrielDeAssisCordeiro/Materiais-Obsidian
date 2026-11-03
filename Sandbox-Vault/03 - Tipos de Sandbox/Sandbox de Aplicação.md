---
tags:
  - tipos
aliases:
  - "App sandbox"
  - "Flatpak"
  - "Snap"
  - "Sandbox de navegador"
tipo: tipo-de-sandbox
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Sistema Operacional]]"
  - "[[Sandbox de Processo]]"
  - "[[Criar Sandbox com Bubblewrap]]"
---
# Sandbox de Aplicação

Isola **uma aplicação** dos demais programas e dos dados do usuário.

| Exemplo | Como isola |
|---|---|
| Navegadores (Chrome, Firefox) | Processos separados por site/aba, com privilégios reduzidos e filtros de syscalls |
| Flatpak | Bubblewrap + namespaces; acesso a recursos via *portals* e permissões declaradas |
| Snap | Confinamento com AppArmor, seccomp e cgroups |
| Apps móveis | Ver [[Sandbox de Sistema Operacional]] |

```bash
# Flatpak: ver e restringir permissões de um app
flatpak info --show-permissions org.example.App
flatpak override --user --nofilesystem=home org.example.App
```

> [!tip] Revise as permissões dos apps
> Um app com `--filesystem=host` ou acesso total ao `home` tem pouca contenção.

## Exercício

Rode `flatpak info --show-permissions` em um app instalado e identifique a permissão mais ampla.

## Veja também

- [[Sandbox de Sistema Operacional]]
- [[Sandbox de Processo]]
- [[Criar Sandbox com Bubblewrap]]
- [[MOC - Tipos de Sandbox]]
