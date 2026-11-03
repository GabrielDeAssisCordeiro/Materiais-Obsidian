---
tags:
  - docker
  - imagens
  - comandos
  - backup
aliases: []
tipo: comando
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Export e import de containers]]"
  - "[[Comando docker pull]]"
  - "[[Comando docker tag e push]]"
---

# Salvar e carregar imagens

`save` e `load` movem **imagens** (com camadas, tags e histórico) por arquivo `.tar`, útil em ambientes **sem acesso a registry** (*air-gapped*) ou para backup.

```bash
# Salva uma ou mais imagens
docker save -o imagens.tar nginx:1.27 alpine:3.20

# Com compressão
docker save nginx:1.27 | gzip > nginx-1.27.tar.gz

# Carrega no outro host
docker load -i imagens.tar
gunzip -c nginx-1.27.tar.gz | docker load

# Transferência direta por SSH
docker save nginx:1.27 | ssh usuario@servidor 'docker load'
```

> [!info] `save`/`load` vs `export`/`import`
> `save/load` trabalham com **imagens** e preservam camadas e metadados. `export/import` trabalham com o **sistema de arquivos achatado de um container** e perdem histórico. Veja [[Export e import de containers]].

> [!tip] Imagens multiplataforma
> Dependendo do image store, `docker save` pode exportar apenas a plataforma do host. Use `--platform` quando precisar de uma arquitetura específica.

> [!question] Verificar na documentação oficial
> O suporte a `--platform` em `docker save/load` depende da versão da CLI e do image store (containerd). Confirme em `docker save --help`.

## Exercício

Salve `alpine:3.20` em um tar, remova a imagem local com `docker rmi` e restaure com `docker load`. Confirme com `docker images`.

## Veja também

- [[Export e import de containers]]
- [[Comando docker pull]]
- [[Comando docker tag e push]]
- [[MOC - Imagens]]
