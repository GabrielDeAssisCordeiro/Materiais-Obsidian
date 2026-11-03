---
tags:
  - docker
  - producao
  - monitoramento
  - observabilidade
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Métricas com cAdvisor, Prometheus e Grafana]]"
  - "[[Logs centralizados com Loki]]"
  - "[[Resiliência em produção]]"
---

# Monitoramento em produção

Sem monitoramento, você descobre problemas pelos usuários. Cubra quatro frentes:

| Frente | O que observar | Ferramentas |
|---|---|---|
| **Disponibilidade** | O serviço responde de fora? | Uptime checks externos (UptimeRobot, Healthchecks.io, Blackbox exporter) |
| **Métricas** | CPU, memória, rede, disco, reinícios, latência, erros | cAdvisor, node_exporter, Prometheus |
| **Logs** | Erros e eventos | Loki, ELK, serviços da nuvem |
| **Traços** | Latência entre serviços | OpenTelemetry, Jaeger, Tempo |

## Alertas essenciais

| Alerta | Condição típica |
|---|---|
| Serviço fora do ar | Check externo falha por 2–3 minutos |
| Container reiniciando | `RestartCount` aumenta repetidamente |
| OOM | Eventos `oom` / `OOMKilled=true` |
| Disco | `/var/lib/docker` > 80% |
| Memória/CPU sustentadas | > 85% por 10 minutos |
| Taxa de erros 5xx | Acima de um limite |
| Certificado | Expira em menos de 14 dias |

```yaml
# Exemplo de regra do Prometheus (arquivo de regras)
groups:
  - name: containers
    rules:
      - alert: ContainerMemoriaAlta
        expr: container_memory_working_set_bytes{name!=""} / container_spec_memory_limit_bytes{name!=""} > 0.9
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Container {{ $labels.name }} usando mais de 90% do limite de memória"
```

> [!tip] Alerte sobre sintomas, não só causas
> Priorize alertas ligados à experiência do usuário (erros, latência) e use métricas de recursos para diagnóstico.

> [!info] Nem todo container tem limite
> A regra acima só funciona para containers com limite de memória definido; mais um motivo para [[Limites de recursos - Docker]].

## Exercício

Defina cinco alertas para seu serviço (condição, severidade e quem é acionado) e implemente pelo menos um no Prometheus.

## Veja também

- [[Métricas com cAdvisor, Prometheus e Grafana]]
- [[Logs centralizados com Loki]]
- [[Resiliência em produção]]
- [[MOC - Produção]]
