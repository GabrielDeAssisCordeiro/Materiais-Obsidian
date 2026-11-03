---
tags:
  - docker
  - observabilidade
  - logs
  - boas-praticas
  - 12-factor
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Logs e logging drivers]]"
  - "[[Logs centralizados com Loki]]"
  - "[[Comando docker logs]]"
  - "[[Gerenciamento de segredos]]"
---

# Boas práticas de logs em containers

Seguem o princípio **12-factor**: logs são um **fluxo de eventos** escrito na saída padrão; a plataforma cuida do roteamento.

| Prática | Motivo |
|---|---|
| Escrever em **stdout/stderr** | `docker logs`, coletores e orquestradores já sabem lê-los |
| **Não** gravar em arquivos dentro do container | Enche a camada gravável e complica a coleta |
| Logs **estruturados** (JSON) | Pesquisa e métricas |
| Um evento por linha | Evita quebra de eventos multilinha |
| Níveis (`debug`, `info`, `warn`, `error`) configuráveis por variável | Controle em produção |
| **UTC** e formato ISO-8601 | Correlação entre serviços |
| ID de correlação por requisição | Rastrear fluxos entre serviços |
| **Nunca** logar segredos, tokens ou dados pessoais | Segurança e LGPD/GDPR |
| Rotação/retenção no driver | Evita disco cheio |

Exemplo de linha estruturada:

```json
{"ts":"2026-10-24T12:00:00Z","level":"error","service":"api","trace_id":"abc123","msg":"falha ao conectar ao banco","err":"timeout"}
```

## Quando a aplicação insiste em gravar arquivos

```dockerfile
# Redireciona os arquivos de log para os fluxos padrão (padrão usado em imagens oficiais)
RUN ln -sf /dev/stdout /var/log/app/access.log \
 && ln -sf /dev/stderr /var/log/app/error.log
```

> [!tip] Encerramento limpo
> Trate **SIGTERM** e descarregue (*flush*) os logs antes de sair; veja [[Init, PID 1 e sinais]].

> [!warning] Python e saída com buffer
> Defina `PYTHONUNBUFFERED=1`, ou os logs aparecem atrasados ou não aparecem em `docker logs`.

## Exercício

Converta o log de uma aplicação sua para JSON estruturado em stdout e remova qualquer gravação em arquivo.

## Veja também

- [[Logs e logging drivers]]
- [[Logs centralizados com Loki]]
- [[Comando docker logs]]
- [[Gerenciamento de segredos]]
- [[MOC - Observabilidade e Depuração]]
