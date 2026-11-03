---
tags:
  - docker
  - desenvolvimento
  - testes
  - ci
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Bancos de dados locais]]"
  - "[[Proteção do docker.sock]]"
  - "[[Python em Docker]]"
  - "[[Java em Docker]]"
---

# Testes com Testcontainers

**Testcontainers** é uma biblioteca (Java, Python, Node, Go, .NET e outras) que **sobe containers descartáveis durante os testes**: banco de dados real, fila, cache. Cada teste roda contra dependências reais e limpas, sem mocks frágeis.

## Python (pytest)

```bash
pip install "testcontainers[postgres]" sqlalchemy psycopg2-binary pytest
```

```python
import sqlalchemy
from testcontainers.postgres import PostgresContainer


def test_consulta_basica():
    with PostgresContainer("postgres:16") as pg:
        engine = sqlalchemy.create_engine(pg.get_connection_url())
        with engine.connect() as conn:
            resultado = conn.execute(sqlalchemy.text("SELECT 1")).scalar()
        assert resultado == 1
```

## Java (JUnit 5)

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import static org.junit.jupiter.api.Assertions.assertTrue;

@Testcontainers
class RepositorioIT {

    @Container
    static PostgreSQLContainer<?> pg = new PostgreSQLContainer<>("postgres:16");

    @Test
    void conecta() {
        assertTrue(pg.isRunning());
        // use pg.getJdbcUrl(), pg.getUsername(), pg.getPassword()
    }
}
```

## Como funciona

1. A biblioteca usa a API do Docker (via socket) para criar o container.
2. Aguarda a estratégia de **prontidão** (porta aberta, log, healthcheck).
3. Mapeia uma **porta aleatória** do host e informa a URL.
4. Remove o container ao final (um container auxiliar, o *Ryuk*, garante a limpeza).

## Em CI

| Requisito | Detalhe |
|---|---|
| Acesso ao Docker | Socket do daemon disponível ao job (runner com Docker) |
| Imagens | Use um registry/espelho para evitar limites de pull |
| Desempenho | Reaproveite containers entre testes da mesma suíte |

> [!warning] Dá acesso ao Docker do host
> O processo de teste precisa do socket do Docker; trate o runner como ambiente confiável e isolado. Veja [[Proteção do docker.sock]].

> [!question] Verificar na documentação oficial
> Nomes de pacotes, módulos e a API variam por linguagem e versão; consulte testcontainers.com para a sintaxe atual.

## Exercício

Escreva um teste de integração que insere e consulta uma linha em um PostgreSQL via Testcontainers, na sua linguagem preferida.

## Veja também

- [[Bancos de dados locais]]
- [[Proteção do docker.sock]]
- [[Python em Docker]]
- [[Java em Docker]]
- [[MOC - Desenvolvimento]]
