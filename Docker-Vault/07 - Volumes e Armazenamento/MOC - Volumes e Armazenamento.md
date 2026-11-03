---
tags:
  - docker
  - moc
aliases:
  - Volumes e Armazenamento
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Volumes e Armazenamento

Como persistir, compartilhar e proteger dados: volumes, bind mounts, tmpfs, drivers, bancos de dados, backups, permissões e o funcionamento interno do armazenamento (camada gravável, overlay2).

> [!tip] Resumo
> Dados da aplicação → volume nomeado. Código em desenvolvimento → bind mount. Temporário/sensível → tmpfs. Veja [[Volume vs bind mount vs tmpfs]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Volumes nomeados]] — Persistência gerenciada pelo Docker
- [[Bind mounts]] — Montar diretórios do host
- [[tmpfs mounts]] — Armazenamento em memória
- [[Volume vs bind mount vs tmpfs]] — Tabela de decisão entre os três tipos
- [[Sintaxe -v vs --mount]] — Equivalências e diferenças
- [[Drivers de volume]] — local, NFS e plugins
- [[Persistência de bancos de dados]] — PostgreSQL com volume nomeado e cuidados
- [[Backup e restauração de volumes]] — tar, dump lógico e restauração
- [[Permissões e UID GID em volumes]] — UID/GID, chown, SELinux
- [[Camada gravável do container]] — Camada efêmera sobre a imagem
- [[Storage drivers e overlay2]] — overlay2, snapshotters e requisitos

## Veja também

- [[Home - Docker]]
