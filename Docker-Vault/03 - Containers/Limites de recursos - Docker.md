---
tags:
  - docker
  - containers
  - recursos
  - cgroups
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Cgroups - Docker]]"
  - "[[Comandos stats e top]]"
  - "[[Comando docker run]]"
  - "[[Políticas de restart]]"
---

# Limites de recursos - Docker

Por padrão, um container pode usar **todos os recursos do host**. Defina limites para evitar que um serviço prejudique os demais.

```bash
docker run -d --name app \
  --memory 512m --memory-reservation 256m \
  --cpus 1.5 \
  --pids-limit 200 \
  --ulimit nofile=4096:8192 \
  nginx:1.27

# Ajusta sem recriar (alguns limites)
docker update --memory 768m --memory-swap 768m app

# Confere
docker inspect --format 'mem={{.HostConfig.Memory}} cpus={{.HostConfig.NanoCpus}} pids={{.HostConfig.PidsLimit}}' app
```

| Opção | Efeito |
|---|---|
| `--memory`, `-m` | Limite rígido de memória. Excedê-lo gera OOM kill. |
| `--memory-reservation` | Limite "macio"; só aplicado sob pressão de memória. |
| `--memory-swap` | Memória + swap; igual a `--memory` desabilita swap. |
| `--cpus` | Quantidade de CPUs (fracionária). |
| `--cpuset-cpus` | Fixa em núcleos específicos (`0,1`). |
| `--pids-limit` | Máximo de processos/threads. |
| `--ulimit` | Limites POSIX (arquivos abertos, etc.). |

> [!warning] Aplicações com runtime (JVM, Node.js, Go)
> Configure também o runtime para respeitar o limite. Java moderno detecta cgroups; em Node.js ajuste `--max-old-space-size` conforme a memória disponível.

> [!bug] OOM kill
> Código 137 e `OOMKilled=true` no `docker inspect` indicam estouro de memória. Aumente o limite, corrija vazamentos ou ajuste o runtime.

> [!info] Em Compose
> Use `deploy.resources.limits` (veja [[Visão geral do Docker Compose]]).

## Exercício

Rode `docker run --rm -m 20m alpine sh -c 'tail /dev/zero'` e interprete o resultado (código de saída e mensagem).

## Veja também

- [[Cgroups - Docker]]
- [[Comandos stats e top]]
- [[Comando docker run]]
- [[Políticas de restart]]
- [[MOC - Containers]]
