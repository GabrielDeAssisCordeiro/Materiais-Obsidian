---
tags:
  - docker
  - registries
  - registry
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Registries]]"
  - "[[Comando docker tag e push]]"
  - "[[Políticas de retenção e limpeza]]"
  - "[[Volumes nomeados]]"
---

# Registry privado local com registry 2

A imagem `registry:2` (projeto Distribution) permite hospedar seu próprio registry, útil em laboratórios, redes isoladas e como cache.

```bash
# Registry local com persistência
docker run -d --name registry \
  -p 127.0.0.1:5000:5000 \
  -v registry-data:/var/lib/registry \
  --restart unless-stopped \
  registry:2

# Publica uma imagem
docker pull alpine:3.20
docker tag alpine:3.20 localhost:5000/lab/alpine:3.20
docker push localhost:5000/lab/alpine:3.20

# Consulta pela API
curl -s http://localhost:5000/v2/_catalog
curl -s http://localhost:5000/v2/lab/alpine/tags/list

# Baixa de volta
docker rmi localhost:5000/lab/alpine:3.20
docker pull localhost:5000/lab/alpine:3.20
```

> [!info] `localhost:5000` é tratado como seguro
> O Docker aceita HTTP sem TLS apenas para `localhost`/`127.0.0.0/8`. Para outros hosts, use **TLS** (recomendado) ou configure `insecure-registries` no [[Arquivo daemon.json]] (apenas laboratório).

## TLS e autenticação (visão geral)

```bash
# Autenticação básica (htpasswd) — gera o arquivo com bcrypt
mkdir -p auth
docker run --rm --entrypoint htpasswd httpd:2 -Bbn usuario senha-de-laboratorio > auth/htpasswd
```

```yaml
# compose.yaml com autenticação e TLS
services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    environment:
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
      REGISTRY_HTTP_TLS_CERTIFICATE: /certs/fullchain.pem
      REGISTRY_HTTP_TLS_KEY: /certs/privkey.pem
    volumes:
      - registry-data:/var/lib/registry
      - ./auth:/auth:ro
      - ./certs:/certs:ro
volumes:
  registry-data:
```

> [!danger] Registry sem TLS e sem autenticação não deve ser exposto
> Qualquer pessoa na rede poderia enviar e baixar imagens. Em produção, considere soluções com UI, RBAC e varredura, como Harbor.

> [!question] Verificar na documentação oficial
> O projeto Distribution possui uma nova série principal (v3). Confirme na documentação qual tag (`registry:2` ou `registry:3`) é recomendada e as diferenças de configuração.

## Exercício

Suba o registry local, publique duas versões de uma imagem e liste as tags pela API. Remova o container e o volume ao final.

## Veja também

- [[Registries]]
- [[Comando docker tag e push]]
- [[Políticas de retenção e limpeza]]
- [[Volumes nomeados]]
- [[MOC - Registries]]
