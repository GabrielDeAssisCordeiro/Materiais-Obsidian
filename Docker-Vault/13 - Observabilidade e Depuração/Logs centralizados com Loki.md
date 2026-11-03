---
tags:
  - docker
  - observabilidade
  - logs
  - grafana
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Logs e logging drivers]]"
  - "[[Métricas com cAdvisor, Prometheus e Grafana]]"
  - "[[Boas práticas de logs em containers]]"
---

# Logs centralizados com Loki

O **Loki** (Grafana Labs) armazena logs indexando apenas **rótulos**, o que o torna leve. Um coletor envia os logs dos containers e o Grafana os consulta com **LogQL**.

## Opção 1: driver de log do Docker para o Loki

```bash
# Instala o plugin (lab)
docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

# Usa por container
docker run -d --name app \
  --log-driver=loki \
  --log-opt loki-url="http://localhost:3100/loki/api/v1/push" \
  --log-opt loki-batch-size=400 \
  nginx:1.27
```

## Servidor Loki e Grafana (laboratório)

```yaml
services:
  loki:
    image: grafana/loki:3.2.0
    command: -config.file=/etc/loki/local-config.yaml
    ports:
      - "127.0.0.1:3100:3100"
    volumes:
      - loki_data:/loki

  grafana:
    image: grafana/grafana:11.3.0
    ports:
      - "127.0.0.1:3000:3000"
    depends_on:
      - loki
    volumes:
      - grafana_data:/var/lib/grafana

volumes:
  loki_data:
  grafana_data:
```

No Grafana: **Connections → Data sources → Loki → URL `http://loki:3100`**. Consultas LogQL:

```text
{container_name="app"}
{container_name="app"} |= "error"
sum(rate({container_name="app"} |= "error" [5m]))
```

## Opção 2: agente coletor

Um agente lê os logs dos containers e envia ao Loki, com rótulos por serviço/ambiente. O **Promtail** foi o coletor tradicional; o **Grafana Alloy** é o sucessor recomendado.

> [!question] Verificar na documentação oficial
> O Promtail foi descontinuado em favor do Grafana Alloy, e o plugin do driver Docker pode ter requisitos próprios de versão. Consulte a documentação do Loki antes de adotar uma opção.

> [!warning] Cuidado com a cardinalidade de rótulos
> Rótulos com valores muito variáveis (IDs de requisição, usuário) degradam o Loki. Use poucos rótulos estáveis e coloque detalhes no corpo do log.

> [!bug] `docker logs` parou de funcionar com o driver Loki?
> Verifique se o *dual logging* está ativo na sua versão do Engine ou mantenha um coletor em vez do driver.

## Exercício

Suba Loki + Grafana, envie logs de um container e crie uma consulta LogQL que conte linhas de erro por minuto.

## Veja também

- [[Logs e logging drivers]]
- [[Métricas com cAdvisor, Prometheus e Grafana]]
- [[Boas práticas de logs em containers]]
- [[MOC - Observabilidade e Depuração]]
