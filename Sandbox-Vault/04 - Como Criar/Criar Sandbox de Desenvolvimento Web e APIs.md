---
tags:
  - como-criar
aliases:
  - "Dev web isolado"
  - "Mock de APIs"
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Caso - Sandbox de APIs e Pagamentos]]"
  - "[[Criar Sandbox com Docker]]"
---
# Criar Sandbox de Desenvolvimento Web e APIs

Ambiente local com aplicação, banco e **API simulada**, em rede interna.

```yaml
# compose.yaml
services:
  app:
    build: .
    ports: ["3000:3000"]
    environment:
      PAYMENT_API_URL: http://mock-pagamentos:8080
    networks: [frontend, backend]
    depends_on: [db, mock-pagamentos]
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: somente_dev
    tmpfs: [/var/lib/postgresql/data]
    networks: [backend]
  mock-pagamentos:
    image: wiremock/wiremock:latest
    volumes:
      - ./mocks:/home/wiremock/mappings:ro
    networks: [backend]

networks:
  frontend: {}
  backend:
    internal: true     # sem saída para a internet
```

Mapeamento de exemplo em `mocks/pagamento-ok.json`:

```json
{
  "request": { "method": "POST", "url": "/v1/cobrancas" },
  "response": { "status": 201, "jsonBody": { "id": "cb_teste_1", "status": "aprovado" } }
}
```

> [!tip] Simule falhas
> Crie mapeamentos com status `402`, `500` e atrasos (`fixedDelayMilliseconds`) para testar a resiliência.

> [!warning] Chaves reais nunca entram no repositório
> Use arquivos `.env` fora do controle de versão e chaves de teste dos provedores.

## Exercício

Suba o compose e faça uma chamada `curl` ao mock a partir do container `app`.

## Veja também

- [[Caso - Sandbox de APIs e Pagamentos]]
- [[Criar Sandbox com Docker]]
- [[Caso - Homologação e Staging]]
- [[MOC - Como Criar]]
