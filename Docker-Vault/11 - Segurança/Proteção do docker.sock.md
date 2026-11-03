---
tags:
  - docker
  - seguranca
  - daemon
  - api
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Riscos do --privileged]]"
  - "[[Docker Daemon dockerd]]"
  - "[[Contextos do Docker]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Proteção do docker.sock

O socket `/var/run/docker.sock` é a porta de entrada da API do daemon. **Quem controla o socket controla o host**: pode criar um container montando `/` e obter acesso root.

> [!danger] Montar o socket em um container = entregar o host
> ```yaml
> # ❌ ALTO RISCO (didático): este container pode controlar todo o Docker do host
> services:
>   ferramenta:
>     image: alguma-ferramenta
>     volumes:
>       - /var/run/docker.sock:/var/run/docker.sock
> ```
> `:ro` **não** protege: a API continua totalmente utilizável pelo socket.

## Quem precisa mesmo do socket?

Proxies reversos com autodescoberta (Traefik), ferramentas de monitoramento e agentes de CI. Reduza o risco:

| Medida | Descrição |
|---|---|
| **Proxy de socket** | `tecnativa/docker-socket-proxy` expõe apenas endpoints permitidos (por exemplo, só `GET containers`) |
| Rootless | O socket pertence a um usuário sem privilégios |
| SSH em vez de TCP | `docker context create ... --docker "host=ssh://..."` |
| TLS mútuo | Obrigatório se o daemon escutar em TCP (porta 2376) |
| Plugins de autorização | Restringem comandos por usuário |
| Grupo `docker` | Controle de quem pode usar o socket (equivale a root) |

```yaml
services:
  socket-proxy:
    image: tecnativa/docker-socket-proxy
    environment:
      CONTAINERS: 1        # permite apenas leitura de containers
      POST: 0              # bloqueia métodos de escrita
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks: [interna]

  traefik:
    image: traefik:v3.6
    command:
      - --providers.docker.endpoint=tcp://socket-proxy:2375
    networks: [interna]

networks:
  interna:
    internal: true
```

```bash
# Auditoria: quais containers montam o socket?
docker ps -q | xargs -r docker inspect --format '{{.Name}}: {{range .Mounts}}{{.Source}} {{end}}' | grep docker.sock
```

> [!question] Verificar na documentação oficial
> Confirme as variáveis suportadas do `docker-socket-proxy` e a tag da imagem na página do projeto.

## Exercício

Audite seu ambiente com o comando de `docker inspect` acima. Para cada container que monta o socket, decida se pode usar um proxy de socket.

## Veja também

- [[Riscos do --privileged]]
- [[Docker Daemon dockerd]]
- [[Contextos do Docker]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Segurança]]
