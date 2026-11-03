---
tags:
  - docker
  - desenvolvimento
  - hot-reload
  - bind-mount
  - compose
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Bind mounts]]"
  - "[[Compose Watch]]"
  - "[[Node.js em Docker]]"
  - "[[Python em Docker]]"
---

# Hot reload em containers

**Hot reload** reinicia ou recarrega a aplicação ao editar arquivos, sem reconstruir a imagem.

## Duas estratégias

| Estratégia | Como | Observações |
|---|---|---|
| **Bind mount** | Monta o código do host no container | Simples; atenção a desempenho e permissões |
| **Compose Watch** | `develop.watch` sincroniza arquivos | Sem bind mount; `rebuild` automático em dependências |

## Ferramentas por linguagem

| Linguagem | Recarga |
|---|---|
| Node.js | `node --watch`, `nodemon`, Vite/Next dev server |
| Python | `uvicorn --reload`, `flask run --debug` |
| Go | `air` |
| Java | Spring Boot DevTools, `mvn spring-boot:run` |
| PHP | Arquivos montados (Apache/PHP-FPM leem a cada requisição) |
| .NET | `dotnet watch` |
| Rust | `cargo watch` |

## Exemplo (Node.js) com bind mount

```yaml
services:
  web:
    build:
      context: .
      target: dev
    ports:
      - "3000:3000"
    volumes:
      - ./:/app
      - /app/node_modules      # volume anônimo: não deixa o node_modules do host sobrescrever o do container
    environment:
      CHOKIDAR_USEPOLLING: "true"   # necessário em alguns ambientes (macOS/Windows) para detectar mudanças
```

> [!bug] Alterações não são detectadas
> Em macOS/Windows e montagens de rede, eventos de arquivo podem não propagar. Use *polling* (`CHOKIDAR_USEPOLLING`, `--poll`) ou prefira o Compose Watch.

> [!bug] "node_modules" sumiu ou está com binários de outra plataforma
> O bind mount sobrepõe `/app/node_modules`. Use o volume anônimo do exemplo ou instale dependências dentro do container.

> [!tip] Servidores precisam escutar em 0.0.0.0
> Em containers, configure `--host 0.0.0.0` (Vite, Uvicorn, Flask); `127.0.0.1` não é acessível de fora do container.

## Exercício

Configure hot reload em um projeto Node ou Python e demonstre que editar um arquivo reflete no navegador em segundos, sem rebuild.

## Veja também

- [[Bind mounts]]
- [[Compose Watch]]
- [[Node.js em Docker]]
- [[Python em Docker]]
- [[MOC - Desenvolvimento]]
