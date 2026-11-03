---
tags:
  - docker
  - imagens
  - comandos
  - manutencao
  - prune
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Listar e inspecionar imagens]]"
  - "[[Comandos ps e rm]]"
  - "[[Camada gravável do container]]"
---

# Limpeza com prune

Com o tempo, imagens, containers parados, redes e cache de build ocupam muito disco. Veja o consumo e limpe com critério.

```bash
docker system df                 # resumo de uso de disco
docker system df -v              # detalhado

docker container prune           # containers parados
docker image prune               # imagens dangling (<none>)
docker image prune -a            # TODAS as imagens sem container associado
docker image prune -a --filter "until=168h"   # mais velhas que 7 dias
docker network prune             # redes sem uso
docker volume prune              # volumes anônimos sem uso
docker builder prune             # cache de build
docker system prune              # containers, redes, dangling e cache
docker system prune -a --volumes # agressivo: inclui imagens sem uso e volumes
```

> [!danger] `--volumes` pode apagar dados
> `docker volume prune` e `docker system prune --volumes` removem volumes que **nenhum container usa naquele momento**, inclusive um volume de banco de dados cujo container está parado. Faça backup antes e prefira listar (`docker volume ls`) para decidir.

> [!tip] Automação segura
> Em servidores, agende `docker image prune -af --filter "until=720h"` e `docker builder prune -f --keep-storage 10GB` em vez de `system prune -a --volumes`.

> [!bug] "no space left on device"
> Verifique `docker system df` e `df -h /var/lib/docker`. Logs sem rotação costumam ser a causa oculta; veja [[Comando docker logs]].

## Exercício

Execute `docker system df`, faça um `docker image prune` e compare o "RECLAIMABLE" antes e depois.

## Veja também

- [[Listar e inspecionar imagens]]
- [[Comandos ps e rm]]
- [[Camada gravável do container]]
- [[MOC - Imagens]]
