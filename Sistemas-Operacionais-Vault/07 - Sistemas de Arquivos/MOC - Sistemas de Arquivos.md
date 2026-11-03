---
titulo: "MOC - Sistemas de Arquivos"
tags:
  - sistemas-operacionais
  - moc
  - sistemas-de-arquivos
tipo: moc
nivel: intermediario
relacionados:
  - "[[Sistemas de Arquivos - Conceitos]]"
  - "[[VFS - Virtual File System]]"
  - "[[Inodes]]"
  - "[[Journaling e Copy-on-Write]]"
---

# MOC - Sistemas de Arquivos

> [!info] Escopo
> Como o SO organiza dados persistentes: nomes, hierarquia, metadados, permissões, consistência e desempenho.

## Conceitos

1. [[Sistemas de Arquivos - Conceitos]]: arquivos, diretórios, alocação, links
2. [[VFS - Virtual File System]]: camada de abstração do kernel
3. [[Inodes]]: metadados e estrutura de dados do UNIX
4. [[Permissões de Arquivos]]: modo rwx, ACLs, setuid
5. [[Journaling e Copy-on-Write]]: consistência após falhas, copy-on-write

## Sistemas de arquivos específicos

| Nota | SO / uso | Destaque |
|---|---|---|
| [[ext4]] | Linux | Padrão da maioria das distribuições; journaling e extents |
| [[NTFS]] | Windows | MFT, ACLs, compressão, criptografia (EFS), journaling |
| [[APFS]] | macOS, iOS | Copy-on-write, snapshots, clones, criptografia nativa |
| [[Btrfs]] | Linux | CoW, snapshots, subvolumes, checksums |
| [[ZFS]] | Solaris, FreeBSD, Linux | Pool de armazenamento, integridade ponta a ponta, RAID-Z |

## Ferramentas relacionadas

[[mount]] · [[df e du]] · [[chmod e chown]]

## Pré-requisitos

[[System Calls]] · [[Processos]] · [[Drivers de Dispositivo]]
