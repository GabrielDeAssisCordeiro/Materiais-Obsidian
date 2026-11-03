---
tags:
  - docker
  - containers
  - configuracao
  - env
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comando docker run]]"
  - "[[Comando docker inspect]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Variáveis de ambiente em containers

Variáveis de ambiente são a forma mais comum de **configurar** aplicações em container (princípio *12-factor*).

```bash
# Uma variável
docker run --rm -e SAUDACAO="Olá" alpine:3.20 sh -c 'echo "$SAUDACAO"'

# Herdar do shell do host (sem valor)
export REGIAO=sa-east-1
docker run --rm -e REGIAO alpine:3.20 printenv REGIAO

# Várias a partir de um arquivo
cat > app.env <<'EOF'
APP_ENV=desenvolvimento
LOG_LEVEL=debug
EOF
docker run --rm --env-file app.env alpine:3.20 env | grep -E 'APP_ENV|LOG_LEVEL'
```

## Regras do `--env-file`

- Uma linha por variável, no formato `CHAVE=valor`.
- Linhas iniciadas por `#` são comentários.
- Não há interpretação de aspas ou de `$VAR` pelo `docker run` (diferente do Compose; veja [[Visão geral do Docker Compose]]).

## Precedência

`-e` na linha de comando sobrescreve `--env-file`, que sobrescreve `ENV` definido na imagem.

> [!danger] Não coloque segredos em variáveis de ambiente se puder evitar
> Variáveis aparecem em `docker inspect`, em `/proc/PID/environ`, e podem vazar em logs de depuração e processos filhos. Para senhas e chaves, prefira **secrets** (arquivos montados em `/run/secrets`) e leia o valor do arquivo. Veja [[Princípio do menor privilégio - Docker]].

> [!tip] Muitas imagens aceitam `VAR_FILE`
> Imagens oficiais como `postgres` e `mysql` suportam `POSTGRES_PASSWORD_FILE`, apontando para um arquivo de secret.

## Exercício

Crie um `.env` com três variáveis, rode um container que as imprime, e depois sobrescreva uma delas com `-e` para comprovar a precedência.

## Veja também

- [[Comando docker run]]
- [[Comando docker inspect]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Containers]]
