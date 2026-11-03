---
tags:
  - docker
  - swarm
  - init
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Swarm]]"
  - "[[Rede overlay]]"
  - "[[Nodes, services, tasks e stacks]]"
---

# Inicializando um Swarm

## Cluster de um nó (laboratório)

```bash
docker swarm init
docker node ls
```

## Cluster com vários nós

No primeiro nó (será manager):

```bash
docker swarm init --advertise-addr 192.168.1.10
```

Saída: um comando `docker swarm join --token ... 192.168.1.10:2377`. Para recuperar o token a qualquer momento:

```bash
docker swarm join-token worker
docker swarm join-token manager
```

Nos demais nós:

```bash
docker swarm join --token <TOKEN> 192.168.1.10:2377
```

## Gerenciando nós

```bash
docker node ls
docker node inspect --pretty NOME_DO_NO
docker node promote NOME_DO_NO           # worker → manager
docker node demote NOME_DO_NO
docker node update --availability drain NOME_DO_NO   # manutenção
docker node update --availability active NOME_DO_NO
docker node update --label-add zona=a NOME_DO_NO     # rótulos para placement
docker swarm leave                       # no nó que sai (worker)
docker node rm NOME_DO_NO                # no manager, após sair
docker swarm leave --force               # em um manager (cuidado com o quórum)
```

## Portas entre os nós

`2377/tcp` (gerência), `7946/tcp+udp` (comunicação), `4789/udp` (overlay). Veja [[Rede overlay]].

> [!danger] Tokens são credenciais
> Quem possui o token de manager pode assumir o cluster. Não os registre em repositórios e rotacione-os com `docker swarm join-token --rotate manager`.

> [!tip] Autolock
> `docker swarm init --autolock` exige uma chave para destravar os managers após reiniciar, protegendo as chaves de criptografia do Raft em disco.

## Exercício

Inicialize um Swarm de um nó, adicione um rótulo ao nó e liste com `docker node inspect --pretty`. Depois saia com `docker swarm leave --force`.

## Veja também

- [[Visão geral do Swarm]]
- [[Rede overlay]]
- [[Nodes, services, tasks e stacks]]
- [[MOC - Swarm e Orquestração]]
