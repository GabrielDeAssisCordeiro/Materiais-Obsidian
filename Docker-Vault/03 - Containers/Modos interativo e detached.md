---
tags:
  - docker
  - containers
  - run
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comando docker run]]"
  - "[[Comando docker exec e attach]]"
  - "[[Comando docker logs]]"
  - "[[Init, PID 1 e sinais]]"
---

# Modos interativo e detached

## Primeiro plano (padrão)

O terminal fica preso à saída do processo principal. `Ctrl+C` envia SIGINT ao processo.

```bash
docker run --rm nginx:1.27      # logs no terminal; Ctrl+C para parar
```

## Interativo (`-i` e `-t`)

- `-i` (`--interactive`) mantém o **stdin** aberto.
- `-t` (`--tty`) aloca um **pseudo-terminal**.

```bash
docker run --rm -it ubuntu:24.04 bash
# dentro: cat /etc/os-release ; exit
```

> [!tip] Sair sem encerrar
> Dentro de um container iniciado com `-it`, a sequência `Ctrl+P` seguida de `Ctrl+Q` desanexa o terminal **sem parar** o container (se foi iniciado com `-it`).

## Segundo plano (`-d`)

```bash
docker run -d --name web nginx:1.27
docker logs -f web         # acompanha a saída (Ctrl+C sai do logs, não do container)
docker exec -it web sh     # abre um shell no container em execução
docker stop web && docker rm web
```

## Qual usar?

| Cenário | Modo |
|---|---|
| Serviços (web, banco, fila) | `-d` |
| Comandos pontuais, scripts | primeiro plano com `--rm` |
| Depurar ou explorar uma imagem | `-it --rm` |

> [!bug] Container em `-d` que "morre" na hora
> Se o processo principal termina (ex.: `ubuntu` sem comando longo), o container sai. Containers de serviço precisam de um processo em primeiro plano; não use `nohup`, `&` ou `service x start` como comando principal.

## Exercício

Rode `docker run -d ubuntu:24.04` e verifique com `docker ps -a` por que ele saiu. Depois rode `docker run -d ubuntu:24.04 sleep 300` e compare.

## Veja também

- [[Comando docker run]]
- [[Comando docker exec e attach]]
- [[Comando docker logs]]
- [[Init, PID 1 e sinais]]
- [[MOC - Containers]]
