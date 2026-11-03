---
tags:
  - casos-de-uso
aliases:
  - "QA em sandbox"
  - "Testes isolados"
tipo: caso-de-uso
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Containers]]"
  - "[[Caso - CI e CD]]"
---
# Caso - Testes de Software e QA

Testes precisam de **ambientes previsíveis e descartáveis**: banco de dados limpo, versões fixas de dependências, sem afetar dados reais.

- Containers sobem bancos e serviços em segundos para testes de integração.
- Cada execução parte do mesmo estado, evitando o "na minha máquina funciona".
- Falhas catastróficas (apagar dados, travar processo) ficam contidas.

```yaml
# docker-compose.test.yml (exemplo mínimo)
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: apenas_para_teste
    tmpfs:
      - /var/lib/postgresql/data   # descartado ao final
```

> [!tip] Dados de teste, nunca dados reais
> Use bases sintéticas ou anonimizadas — ver [[Sandbox de Dados]].

## Exercício

Crie um `docker-compose` com um banco em `tmpfs` e confirme que os dados somem após `docker compose down`.

## Veja também

- [[Sandbox por Containers]]
- [[Sandbox de Dados]]
- [[Caso - CI e CD]]
- [[MOC - Casos de Uso]]
