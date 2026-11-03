---
tags:
  - docker
  - containers
  - healthcheck
  - resiliencia
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Políticas de restart]]"
  - "[[Comando docker inspect]]"
  - "[[Comando docker run]]"
---

# Healthchecks em containers

Um **healthcheck** é um comando executado periodicamente dentro do container para saber se a **aplicação** (e não apenas o processo) está saudável.

```bash
docker run -d --name web \
  --health-cmd 'curl -fsS http://localhost/ || exit 1' \
  --health-interval 10s \
  --health-timeout 3s \
  --health-retries 3 \
  --health-start-period 15s \
  nginx:1.27
```

| Opção | Significado |
|---|---|
| `--health-cmd` | Comando; código 0 = saudável, 1 = não saudável. |
| `--health-interval` | Intervalo entre execuções (padrão 30 s). |
| `--health-timeout` | Tempo máximo do comando (padrão 30 s). |
| `--health-retries` | Falhas consecutivas até `unhealthy` (padrão 3). |
| `--health-start-period` | Período de carência na inicialização. |

## Estados

`starting` → `healthy` ↔ `unhealthy`

```bash
docker ps --format '{{.Names}}: {{.Status}}'
docker inspect --format '{{json .State.Health}}' web
```

> [!info] O que o Docker faz com `unhealthy`?
> O Docker **apenas marca** o estado. Quem age sobre ele são o Swarm (substitui tarefas), o Compose (`depends_on` com `condition: service_healthy`) e ferramentas externas. Em um Docker isolado, o container não é reiniciado automaticamente.

> [!warning] A imagem precisa ter a ferramenta
> `curl` pode não existir em imagens mínimas. Use `wget`, um binário próprio da aplicação, ou um healthcheck feito na linguagem. Healthchecks pesados ou com efeitos colaterais prejudicam o serviço.

## Exercício

Crie um container com healthcheck que passa e depois remova o arquivo que ele verifica (`docker exec ... rm ...`) para observar a transição para `unhealthy`.

## Veja também

- [[Políticas de restart]]
- [[Comando docker inspect]]
- [[Comando docker run]]
- [[MOC - Containers]]
