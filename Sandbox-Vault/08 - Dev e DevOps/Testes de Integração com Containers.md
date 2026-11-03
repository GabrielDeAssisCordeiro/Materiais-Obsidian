---
tags:
  - devops
  - dev
aliases:
  - "Testcontainers"
tipo: devops
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Caso - Testes de Software e QA]]"
  - "[[Sandbox por Containers]]"
---
# Testes de Integração com Containers

Bibliotecas como **Testcontainers** sobem dependências reais (bancos, filas) em containers descartáveis durante os testes.

```python
# pip install testcontainers[postgres] sqlalchemy psycopg2-binary pytest
from testcontainers.postgres import PostgresContainer
import sqlalchemy

def test_consulta_simples():
    with PostgresContainer("postgres:16-alpine") as pg:
        engine = sqlalchemy.create_engine(pg.get_connection_url())
        with engine.connect() as conn:
            assert conn.execute(sqlalchemy.text("select 1")).scalar() == 1
```

> [!tip] Um container por suíte, dados limpos por teste
> Equilibre velocidade (reuso) e isolamento (limpeza entre testes).

> [!question] Verificar na documentação oficial
> A API do Testcontainers varia por linguagem e versão.

## Exercício

Escreva um teste que insere uma linha e a consulta, usando o container acima.

## Veja também

- [[Caso - Testes de Software e QA]]
- [[Dados de Teste e Mocks]]
- [[Sandbox por Containers]]
- [[MOC - Dev e DevOps]]
