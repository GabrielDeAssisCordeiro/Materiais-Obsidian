---
tags:
  - docker
  - volumes
  - armazenamento
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Union filesystems e OverlayFS]]"
  - "[[Camada gravável do container]]"
  - "[[containerd e runc]]"
---

# Storage drivers e overlay2

O **storage driver** (ou *snapshotter*, com o containerd image store) define como camadas de imagem e a camada gravável são armazenadas e combinadas.

| Driver | Observações |
|---|---|
| `overlay2` | **Padrão e recomendado** no Linux moderno; baseado em OverlayFS |
| `btrfs`, `zfs` | Usam recursos nativos do sistema de arquivos; casos específicos |
| `fuse-overlayfs` | Alternativa para modo rootless em kernels sem suporte |
| `vfs` | Sem CoW; lento e ocupa muito espaço; só para depuração |

```bash
# Driver em uso
docker info --format '{{.Driver}}'
docker info | grep -iE "storage driver|backing filesystem|supports d_type"
```

## Requisitos do `overlay2`

- Kernel Linux atual (4.0+; recomendado 5.x ou superior).
- Sistema de arquivos de suporte: `ext4` ou `xfs` com `d_type` habilitado (em XFS, `ftype=1`).

```bash
# Verificar d_type no XFS
xfs_info /var/lib/docker | grep ftype
```

## Containerd image store

Em instalações novas do Engine 29 o armazenamento de imagens é feito pelo **containerd**, usando *snapshotters* (por padrão o `overlayfs`). Isso habilita imagens multiplataforma no daemon local e outros recursos, e muda a saída de `docker info`.

> [!question] Verificar na documentação oficial
> A forma como `docker info` apresenta o driver com o containerd image store (campo `driver-type`) e os passos de migração do image store clássico variam entre versões. Consulte "containerd image store" na documentação.

> [!warning] Não troque o driver com dados existentes
> Alterar `storage-driver` no [[Arquivo daemon.json]] faz o Docker "perder" as imagens e containers do driver anterior (os dados continuam em disco, mas ficam invisíveis). Planeje a migração com exportação (`save`) e backup.

> [!tip] Disco dedicado
> Em produção, use um disco ou partição dedicados para `/var/lib/docker` (via `data-root`) para evitar que o crescimento derrube o sistema.

## Exercício

Em um host Linux, identifique driver, sistema de arquivos de suporte e `d_type` com `docker info`. Verifique também o tamanho de `/var/lib/docker`.

## Veja também

- [[Union filesystems e OverlayFS]]
- [[Camada gravável do container]]
- [[containerd e runc]]
- [[MOC - Volumes e Armazenamento]]
