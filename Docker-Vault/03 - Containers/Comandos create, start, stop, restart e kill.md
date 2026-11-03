---
tags:
  - docker
  - containers
  - comandos
  - ciclo-de-vida
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Ciclo de vida do container]]"
  - "[[Init, PID 1 e sinais]]"
  - "[[Comandos ps e rm]]"
  - "[[Comando docker run]]"
---

# Comandos create, start, stop, restart e kill

```bash
# Cria sem iniciar
docker create --name app -p 8080:80 nginx:1.27

# Inicia (-a anexa saída; -i anexa stdin)
docker start app

# Parada graciosa: SIGTERM e, após o timeout (padrão 10 s), SIGKILL
docker stop app
docker stop -t 30 app          # espera até 30 s

# Reinicia (stop + start)
docker restart app

# Envia SIGKILL imediatamente (ou outro sinal)
docker kill app
docker kill -s SIGHUP app

# Pausa e retoma (congela os processos)
docker pause app
docker unpause app
```

## `stop` vs `kill`

| | `docker stop` | `docker kill` |
|---|---|---|
| Sinal inicial | SIGTERM (ou o `STOPSIGNAL` da imagem) | SIGKILL |
| Chance de encerramento limpo | Sim | Não |
| Quando usar | Normalmente | Container travado |

> [!warning] Demorou 10 segundos para parar?
> Se `docker stop` sempre leva ~10 s, sua aplicação provavelmente **não trata SIGTERM** (muito comum quando o PID 1 é um shell). Use a forma *exec* no `CMD`/`ENTRYPOINT` ou `--init`. Veja [[Init, PID 1 e sinais]].

> [!tip] Várias ao mesmo tempo
> Todos aceitam múltiplos nomes: `docker stop web db cache`. Para parar todos: `docker stop $(docker ps -q)`.

## Exercício

Meça com `time docker stop` quanto leva para parar `alpine sleep 300` e depois `alpine sh -c 'exec sleep 300'`. Qual é mais rápido e por quê?

## Veja também

- [[Ciclo de vida do container]]
- [[Init, PID 1 e sinais]]
- [[Comandos ps e rm]]
- [[Comando docker run]]
- [[MOC - Containers]]
