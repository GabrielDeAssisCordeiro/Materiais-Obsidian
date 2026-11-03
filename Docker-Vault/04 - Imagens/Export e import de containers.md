---
tags:
  - docker
  - imagens
  - comandos
aliases: []
tipo: comando
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Salvar e carregar imagens]]"
  - "[[Comandos cp, diff e commit]]"
  - "[[Camadas de uma imagem]]"
---

# Export e import de containers

`docker export` produz um `.tar` com o **sistema de arquivos** de um container (camadas achatadas, sem histórico, sem metadados como `CMD`, `ENV` e `EXPOSE`). `docker import` cria uma imagem de uma única camada a partir disso.

```bash
docker run --name origem alpine:3.20 sh -c 'echo ola > /ola.txt'
docker export origem -o origem.tar

# Cria uma imagem a partir do tar, reaplicando metadados manualmente
docker import --change 'CMD ["cat","/ola.txt"]' origem.tar lab/importada:1
docker run --rm lab/importada:1

docker rm origem
```

| | `save`/`load` | `export`/`import` |
|---|---|---|
| Objeto | Imagem | Container |
| Camadas | Preservadas | Achatadas em uma |
| Metadados (CMD, ENV, etc.) | Preservados | Perdidos |
| Uso típico | Backup/transferência de imagens | Criar base a partir de um rootfs, inspeção |

> [!tip] Importar um rootfs mínimo
> `docker import` é usado para criar imagens a partir de um sistema de arquivos arbitrário, por exemplo uma raiz criada com `debootstrap`.

## Exercício

Exporte um container, importe com `CMD` customizado e compare o tamanho e o `docker history` com a imagem original.

## Veja também

- [[Salvar e carregar imagens]]
- [[Comandos cp, diff e commit]]
- [[Camadas de uma imagem]]
- [[MOC - Imagens]]
