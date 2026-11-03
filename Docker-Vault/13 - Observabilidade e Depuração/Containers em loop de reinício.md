---
tags:
  - docker
  - observabilidade
  - depuracao
  - restart
  - troubleshooting
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Políticas de restart]]"
  - "[[Comando docker logs]]"
  - "[[Comando docker inspect]]"
  - "[[Erros comuns e soluções]]"
---

# Containers em loop de reinício

Sintoma: `docker ps` mostra `Restarting (1) 5 seconds ago`. Um container em loop de reinício falha logo ao iniciar, e a política de restart o relança.

## Roteiro de diagnóstico

```bash
# 1) Estado e código de saída
docker ps -a --filter name=app
docker inspect --format 'status={{.State.Status}} exit={{.State.ExitCode}} oom={{.State.OOMKilled}} restarts={{.RestartCount}} erro="{{.State.Error}}"' app

# 2) Logs (inclusive da execução anterior)
docker logs --tail 100 app

# 3) Pare o loop para investigar
docker update --restart=no app && docker stop app

# 4) Rode a imagem com um shell no lugar do comando
docker run -it --rm --entrypoint sh MINHA_IMAGEM

# 5) Reproduza exatamente (mesmas variáveis, volumes e redes) e rode o comando manualmente
docker run -it --rm --env-file app.env -v dados:/dados --entrypoint sh MINHA_IMAGEM
```

## Causas frequentes

| Código/mensagem | Causa provável | Ação |
|---|---|---|
| 1 | Erro da aplicação (configuração ausente, exceção) | Ler logs; conferir variáveis |
| 126 / 127 | Comando não executável / não encontrado | Verificar `CMD`, `ENTRYPOINT`, permissões (`chmod +x`), finais de linha CRLF |
| 137 | SIGKILL / OOM | Ver [[Análise de OOM kill]] |
| 139 | Falha de segmentação | Incompatibilidade de arquitetura/biblioteca |
| `exec format error` | Arquitetura errada | Reconstruir para a plataforma correta |
| `permission denied` | Usuário não-root sem acesso | Ajustar donos/permissões |
| `address already in use` | Porta ocupada | Mudar porta ou liberar |
| Falha de conexão com banco | Dependência não pronta | `depends_on` com `service_healthy` e *retry* |

> [!bug] Scripts com finais de linha do Windows
> `exec ./entrypoint.sh: no such file or directory` pode vir de CRLF no shebang. Converta para LF (`dos2unix`) e configure `.gitattributes` com `*.sh text eol=lf`.

> [!tip] Backoff
> O Docker aumenta o intervalo entre reinícios; use `docker events` para ver a sequência `die` → `start`.

## Exercício

Crie um container que falha por falta de variável obrigatória, observe o loop, e siga o roteiro até encontrar e corrigir a causa.

## Veja também

- [[Políticas de restart]]
- [[Comando docker logs]]
- [[Comando docker inspect]]
- [[Erros comuns e soluções]]
- [[MOC - Observabilidade e Depuração]]
