---
tags:
  - docker
  - volumes
  - armazenamento
  - drivers
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Volumes nomeados]]"
  - "[[Persistência de bancos de dados]]"
  - "[[Visão geral do Swarm]]"
---

# Drivers de volume

O driver padrão é `local`, mas ele aceita opções para montar sistemas diferentes, e há plugins de terceiros.

## Driver `local` com NFS

```bash
docker volume create \
  --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.10,rw,nfsvers=4 \
  --opt device=:/exportacao/dados \
  dados-nfs

docker run --rm -v dados-nfs:/dados alpine:3.20 ls /dados
```

## Driver `local` como bind (diretório do host gerenciado como volume)

```bash
docker volume create --driver local \
  --opt type=none --opt o=bind \
  --opt device=/srv/dados dados-host
```

## Em Compose

```yaml
services:
  app:
    image: alpine:3.20
    command: sleep 300
    volumes:
      - dados-nfs:/dados

volumes:
  dados-nfs:
    driver: local
    driver_opts:
      type: nfs
      o: addr=192.168.1.10,rw,nfsvers=4
      device: ":/exportacao/dados"
```

| Opção | Uso |
|---|---|
| Driver `local` + NFS/CIFS | Armazenamento em rede simples |
| Plugins de terceiros (nuvem, SAN, REX-Ray, etc.) | Armazenamento gerenciado |
| Volumes em Swarm | Precisam de driver compartilhado ou *placement constraints* |

> [!warning] Bancos de dados em NFS
> Muitos bancos de dados têm problemas de desempenho e de *locking* sobre NFS. Avalie ou use armazenamento em bloco.

> [!question] Verificar na documentação oficial
> Os plugins de volume disponíveis e mantidos mudam com o tempo. Consulte a documentação oficial de "Volume plugins" antes de escolher um.

## Exercício

Se tiver um servidor NFS de laboratório, crie um volume NFS e monte-o em dois containers para compartilhar arquivos.

## Veja também

- [[Volumes nomeados]]
- [[Persistência de bancos de dados]]
- [[Visão geral do Swarm]]
- [[MOC - Volumes e Armazenamento]]
