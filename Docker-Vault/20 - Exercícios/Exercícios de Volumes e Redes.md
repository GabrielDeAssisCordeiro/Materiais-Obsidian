---
tags:
  - docker
  - exercicios
  - volumes
  - redes
aliases: []
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Volumes nomeados]]"
  - "[[Bind mounts]]"
  - "[[Redes bridge]]"
  - "[[Comunicação entre containers]]"
  - "[[Publicação de portas]]"
---

# Exercícios de Volumes e Redes

## Questões

1. Crie um volume `dados`, grave um arquivo nele com um container `alpine`, remova o container e leia o arquivo com outro.
2. Sirva uma pasta local `site/` com Nginx por **bind mount somente leitura**, na porta 8082.
3. Execute um container `--read-only` que ainda consegue escrever em `/tmp`.
4. Crie uma rede `lab-net` e prove que dois containers se comunicam **por nome**.
5. Por que dois containers na bridge **padrão** não resolvem nomes? Como corrigir?
6. Monte a topologia `proxy` → `api` → `db` com duas redes, de modo que `proxy` **não** alcance `db`.
7. Publique a porta 80 do Nginx **apenas no loopback** (porta 8083).
8. Faça backup do volume `dados` em um `.tar.gz` e restaure em um volume novo.
9. Um container criou arquivos como `root` no seu bind mount. Como evitar?
10. Dois containers com o mesmo `--network-alias web`: o que `nslookup web` retorna?

## Gabarito

```bash
# 1
docker volume create dados
docker run --rm -v dados:/d alpine:3.20 sh -c 'echo ola > /d/arquivo.txt'
docker run --rm -v dados:/d alpine:3.20 cat /d/arquivo.txt

# 2
docker run -d --name site -p 8082:80 -v "$PWD/site":/usr/share/nginx/html:ro nginx:1.27

# 3
docker run --rm --read-only --tmpfs /tmp alpine:3.20 sh -c 'touch /tmp/ok && echo escreveu'

# 4
docker network create lab-net
docker run -d --name api --network lab-net nginx:1.27
docker run --rm --network lab-net alpine:3.20 wget -qO- http://api | head -n 3

# 6
docker network create frontend
docker network create --internal backend
docker run -d --name db  --network backend -e POSTGRES_PASSWORD=lab postgres:16
docker run -d --name api --network backend nginx:1.27
docker network connect frontend api
docker run -d --name proxy --network frontend nginx:1.27
docker exec proxy getent hosts api || true     # resolve
docker exec proxy getent hosts db  || echo "proxy não alcança db"

# 7
docker run -d --name loop -p 127.0.0.1:8083:80 nginx:1.27

# 8
docker run --rm -v dados:/d:ro -v "$PWD":/b alpine:3.20 tar czf /b/dados.tgz -C /d .
docker volume create dados2
docker run --rm -v dados2:/d -v "$PWD":/b:ro alpine:3.20 sh -c 'cd /d && tar xzf /b/dados.tgz'

# 9
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD":/app alpine:3.20 touch /app/meu-arquivo

# 10
docker network create rr
docker run -d --name w1 --network rr --network-alias web nginx:1.27
docker run -d --name w2 --network rr --network-alias web nginx:1.27
docker run --rm --network rr alpine:3.20 nslookup web      # dois IPs
```

5. A bridge padrão **não tem DNS embutido** para nomes de containers; crie uma rede **definida pelo usuário** e conecte os containers a ela.
10. Retorna os **dois endereços IP** (round-robin por DNS).

## Veja também

- [[Volumes nomeados]]
- [[Bind mounts]]
- [[Redes bridge]]
- [[Comunicação entre containers]]
- [[Publicação de portas]]
- [[MOC - Exercícios - Docker]]
