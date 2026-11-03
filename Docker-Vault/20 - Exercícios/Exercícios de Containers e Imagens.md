---
tags:
  - docker
  - exercicios
  - containers
  - imagens
aliases: []
tipo: exercicio
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comando docker run]]"
  - "[[Comando docker inspect]]"
  - "[[Tags e digests de imagens]]"
  - "[[Limpeza com prune]]"
  - "[[Cheat sheet de comandos Docker]]"
---

# Exercícios de Containers e Imagens

## Questões práticas

1. Suba um `nginx:1.27` em segundo plano com o nome `site`, publicando a porta 80 do container na 8081 do host.
2. Mostre as últimas 20 linhas de log com *timestamps*.
3. Abra um shell no container e liste `/usr/share/nginx/html`.
4. Descubra o endereço IP do container usando `docker inspect --format`.
5. Limite a memória a 128 MiB **sem recriar** o container.
6. Defina a política de restart `unless-stopped` no container existente.
7. Execute `alpine sh -c 'exit 7'` com `--name falha` e descubra o código de saída pelo `inspect`.
8. Liste apenas os **IDs** dos containers parados.
9. Crie as tags `lab/alpine:v1` e `lab/alpine:estavel` para `alpine:3.20` e confirme que o IMAGE ID é o mesmo.
10. Salve `alpine:3.20` em um `.tar`, remova a imagem e restaure-a.
11. Qual a diferença entre `docker stop` e `docker kill`?
12. Como descobrir qual instrução criou a maior camada de uma imagem?

## Gabarito

```bash
# 1
docker run -d --name site -p 8081:80 nginx:1.27

# 2
docker logs --tail 20 -t site

# 3
docker exec -it site ls /usr/share/nginx/html

# 4
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' site

# 5
docker update --memory 128m --memory-swap 128m site

# 6
docker update --restart unless-stopped site

# 7
docker run --name falha alpine:3.20 sh -c 'exit 7'
docker inspect -f '{{.State.ExitCode}}' falha          # 7

# 8
docker ps -aq --filter status=exited

# 9
docker tag alpine:3.20 lab/alpine:v1
docker tag alpine:3.20 lab/alpine:estavel
docker images lab/alpine                                # mesmo IMAGE ID

# 10
docker save -o alpine.tar alpine:3.20
docker rmi alpine:3.20 lab/alpine:v1 lab/alpine:estavel
docker load -i alpine.tar
```

11. `docker stop` envia **SIGTERM** (ou o `STOPSIGNAL`) e, após o timeout (padrão 10 s), **SIGKILL**; permite encerramento limpo. `docker kill` envia **SIGKILL** imediatamente.
12. `docker history --human IMAGEM` (ou `--no-trunc` para os comandos completos); a coluna SIZE mostra o tamanho de cada camada.

Limpeza: `docker rm -f site falha; docker rmi lab/alpine:v1 lab/alpine:estavel`.

## Veja também

- [[Comando docker run]]
- [[Comando docker inspect]]
- [[Tags e digests de imagens]]
- [[Limpeza com prune]]
- [[Cheat sheet de comandos Docker]]
- [[MOC - Exercícios - Docker]]
