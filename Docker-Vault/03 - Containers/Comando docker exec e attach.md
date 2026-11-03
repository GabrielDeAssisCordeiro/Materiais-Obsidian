---
tags:
  - docker
  - containers
  - comandos
  - exec
  - depuracao
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Modos interativo e detached]]"
  - "[[Comando docker logs]]"
  - "[[Comandos cp, diff e commit]]"
  - "[[Comando docker run]]"
---

# Comando docker exec e attach

## `docker exec`: executa um **novo** processo em um container em execução

```bash
docker exec web ls /etc/nginx                 # comando simples
docker exec -it web sh                        # shell interativo
docker exec -u root -it web sh                # como outro usuário
docker exec -w /tmp web pwd                   # diretório de trabalho
docker exec -e DEBUG=1 web env                # variável extra
docker exec -d web touch /tmp/arquivo         # em segundo plano
```

## `docker attach`: conecta ao **processo principal** (PID 1)

```bash
docker run -dit --name sess alpine sh
docker attach sess          # entra no shell principal
# Para sair sem parar: Ctrl+P, Ctrl+Q
```

| | `exec` | `attach` |
|---|---|---|
| Cria novo processo | Sim | Não |
| `exit` encerra o container? | Não | Sim (se for o processo principal) |
| Uso típico | Depuração, manutenção | Ver/controlar o processo principal |

> [!tip] Imagens sem shell
> Imagens *distroless* ou `scratch` não têm `sh`. Use `docker debug` (veja [[Docker Debug]]) ou um container auxiliar compartilhando namespaces:
> ```bash
> docker run -it --rm --pid=container:alvo --network=container:alvo alpine sh
> ```

> [!warning] `Ctrl+C` no `attach`
> Pode enviar SIGINT ao processo principal e encerrar o container. Prefira `docker exec`.

## Exercício

Inicie `nginx:1.27` em segundo plano, abra um shell com `exec`, instale nada, apenas leia `/etc/nginx/nginx.conf` e saia. Confirme que o container continua rodando.

## Veja também

- [[Modos interativo e detached]]
- [[Comando docker logs]]
- [[Comandos cp, diff e commit]]
- [[Comando docker run]]
- [[MOC - Containers]]
