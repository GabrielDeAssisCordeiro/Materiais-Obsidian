---
tags:
  - ia
  - agentes
aliases:
  - "Egress allowlist"
  - "Rede de agentes"
tipo: ia
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Sandbox para Código Gerado por IA]]"
  - "[[Vazamento por Rede e DNS]]"
---
# Limites de Rede e Sistema de Arquivos para Agentes

## Rede: negar por padrão, liberar por lista

Se o agente precisa instalar pacotes, force o tráfego por um **proxy de saída com lista de permissão**.

```yaml
# compose.yaml
services:
  sandbox:
    image: python:3.12-alpine
    command: ["sleep", "3600"]
    environment:
      HTTPS_PROXY: http://proxy:3128
      HTTP_PROXY: http://proxy:3128
    networks: [interna]
    read_only: true
    cap_drop: [ALL]
  proxy:
    image: ubuntu/squid
    volumes:
      - ./squid.conf:/etc/squid/squid.conf:ro
    networks: [interna, externa]

networks:
  interna:
    internal: true
  externa: {}
```

```
# squid.conf
http_port 3128
acl SSL_ports port 443
acl CONNECT method CONNECT
acl permitidos dstdomain .pypi.org .files.pythonhosted.org
http_access deny CONNECT !SSL_ports
http_access allow permitidos
http_access deny all
```

> [!warning] Proxy não é à prova de contornos
> Código que ignore as variáveis de proxy não alcança a internet (rede `internal`), o que é o comportamento desejado. Mesmo domínios permitidos podem servir para exfiltração (ex.: enviar dados como pacote); por isso, prefira **sem rede** sempre que possível.

## Sistema de arquivos

- Raiz somente leitura; um diretório de trabalho gravável com quota.
- Entrada e saída por **diretórios explícitos**, nunca o `home` do usuário.
- Não monte repositórios com segredos (`.env`, chaves).
- Valide o que sai da sandbox (tamanho, tipo, conteúdo) antes de entregá-lo ao usuário ou a outro sistema.

## Exercício

Suba o compose acima e teste: `pip download requests` funciona? `curl https://exemplo.com` funciona?

## Veja também

- [[Sandbox para Código Gerado por IA]]
- [[Vazamento por Rede e DNS]]
- [[Criar Sandbox com Docker]]
- [[MOC - IA e Agentes]]
