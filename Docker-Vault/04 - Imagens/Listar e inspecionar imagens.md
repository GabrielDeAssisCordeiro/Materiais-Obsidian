---
tags:
  - docker
  - imagens
  - comandos
  - inspect
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comando docker pull]]"
  - "[[Camadas de uma imagem]]"
  - "[[Limpeza com prune]]"
  - "[[Comando docker inspect]]"
---

# Listar e inspecionar imagens

```bash
docker images                         # ou docker image ls
docker images -a                      # inclui camadas intermediárias
docker images -q                      # apenas IDs
docker images --digests
docker images --filter "dangling=true"
docker images --filter "reference=nginx*"
docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}'

docker history nginx:1.27             # camadas e comandos
docker history --no-trunc nginx:1.27  # comandos completos

docker image inspect nginx:1.27       # JSON completo
docker image inspect nginx:1.27 --format '{{.Config.Cmd}} {{.Config.ExposedPorts}}'
docker system df -v                   # uso de disco detalhado
```

> [!info] Imagens `<none>`
> Aparecem como `<none>:<none>` quando uma tag foi movida para outra imagem (*dangling*) ou são camadas intermediárias. Imagens *dangling* podem ser removidas com `docker image prune`. Veja [[Limpeza com prune]].

> [!tip] Descubra o que a imagem executa
> `docker image inspect --format '{{.Config.Entrypoint}} {{.Config.Cmd}} {{.Config.User}}'` mostra como a imagem inicia e com qual usuário, essencial antes de usá-la.

## Exercício

Para `nginx:1.27`, descubra: arquitetura, portas expostas, ENTRYPOINT, CMD e usuário padrão, usando um único `docker image inspect --format`.

## Veja também

- [[Comando docker pull]]
- [[Camadas de uma imagem]]
- [[Limpeza com prune]]
- [[Comando docker inspect]]
- [[MOC - Imagens]]
