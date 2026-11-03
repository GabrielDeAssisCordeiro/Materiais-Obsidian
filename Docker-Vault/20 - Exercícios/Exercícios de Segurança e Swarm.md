---
tags:
  - docker
  - exercicios
  - seguranca
  - swarm
aliases: []
tipo: exercicio
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Riscos do --privileged]]"
  - "[[Proteção do docker.sock]]"
  - "[[Stacks com docker stack deploy]]"
  - "[[Secrets e configs do Swarm]]"
---

# Exercícios de Segurança e Swarm

> [!danger] Laboratório
> Execute apenas em ambiente próprio e descartável.

## Questões

1. Liste cinco opções de `docker run` que aplicam o **menor privilégio**.
2. Mostre, com um comando, a diferença de dispositivos visíveis entre um container normal e um `--privileged`.
3. Por que montar `/var/run/docker.sock` em um container é perigoso e qual mitigação você usaria?
4. Como verificar se há containers privilegiados ou rodando como root no host?
5. Qual a diferença entre `userns-remap` e o modo rootless?
6. Cite três formas **erradas** e uma **correta** de passar uma senha de banco a um container.
7. Como escanear uma imagem em busca de CVEs críticas e fazer o CI falhar se houver?
8. Inicialize um Swarm de um nó e implante `nginx:1.27` com 3 réplicas publicadas na porta 8080.
9. Como fazer uma atualização progressiva que sobe a nova tarefa **antes** de parar a antiga e reverte em caso de falha?
10. O que o Swarm faz quando um nó entra em `drain`?

## Gabarito

1. Por exemplo: `--user 10001:10001`, `--read-only`, `--cap-drop ALL` (+ `--cap-add` mínimo), `--security-opt no-new-privileges:true`, `--pids-limit`, `-m`/`--cpus`, `--network none`/rede interna.
2. `docker run --rm alpine ls /dev | wc -l` vs `docker run --rm --privileged alpine ls /dev | wc -l` (o privilegiado vê muito mais).
3. O socket dá controle total do daemon (criar containers que montam `/`, etc.): na prática, root no host. Mitigações: **proxy de socket** com permissões mínimas, modo rootless, evitar o socket.
4. `docker ps -q | xargs -r docker inspect --format '{{.Name}} priv={{.HostConfig.Privileged}} user="{{.Config.User}}"'` e filtre `priv=true` ou `user=""`.
5. `userns-remap` mapeia o root **dos containers** para UIDs altos, com o daemon ainda root; **rootless** executa também o **daemon** sem root.
6. Errado: `ENV`/`ARG` no Dockerfile, `-e SENHA=...` na linha de comando, arquivo `.env` versionado. Correto: **secret** (arquivo em `/run/secrets`, com `*_FILE`) e cofre de segredos.
7. `trivy image --exit-code 1 --severity CRITICAL --ignore-unfixed IMAGEM` (ou `grype IMAGEM --fail-on critical`).
8.

```bash
docker swarm init
docker service create --name web --replicas 3 --publish published=8080,target=80 nginx:1.27
```

9. `docker service update --image nginx:1.27 --update-order start-first --update-failure-action rollback web`.
10. Para de agendar novas tasks no nó e **reagenda** as existentes em outros nós.

## Veja também

- [[Princípio do menor privilégio - Docker]]
- [[Riscos do --privileged]]
- [[Proteção do docker.sock]]
- [[Stacks com docker stack deploy]]
- [[Secrets e configs do Swarm]]
- [[MOC - Exercícios - Docker]]
