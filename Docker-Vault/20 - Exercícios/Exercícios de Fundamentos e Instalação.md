---
tags:
  - docker
  - exercicios
  - fundamentos
  - instalacao
aliases: []
tipo: exercicio
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O que é Docker]]"
  - "[[Arquitetura do Docker]]"
  - "[[Namespaces]]"
  - "[[Cgroups - Docker]]"
  - "[[Contextos do Docker]]"
  - "[[Arquivo daemon.json]]"
---

# Exercícios de Fundamentos e Instalação

Tente resolver cada item **antes** de ler o gabarito. Execute os comandos em um ambiente de laboratório.

## Questões

1. Explique, em duas frases, a diferença entre **imagem** e **container**.
2. Quais três recursos do kernel Linux sustentam os containers e o que cada um faz?
3. Por que `docker run --rm alpine uname -r` mostra o mesmo kernel do host (no Linux)?
4. Qual componente efetivamente cria o processo isolado do container? E qual gerencia o ciclo de vida?
5. O que é a OCI e quais são suas três especificações?
6. Qual comando mostra a versão do cliente **e** do servidor Docker?
7. Por que pertencer ao grupo `docker` é equivalente a ter acesso root ao host? Dê um exemplo que demonstre isso (em laboratório).
8. Como validar um `daemon.json` sem reiniciar o serviço?
9. Como criar e usar um contexto Docker para um servidor remoto via SSH?
10. Para cada cenário, escolha **Docker Desktop** ou **Docker Engine**: (a) servidor de produção Linux; (b) notebook com Windows; (c) CI em runner Linux efêmero.

## Gabarito

1. A **imagem** é o modelo imutável (camadas somente leitura + metadados); o **container** é a instância em execução (processo isolado) com uma camada gravável sobre a imagem.
2. **Namespaces** (isolam a visão de PID, rede, mount, hostname, IPC, usuários), **cgroups** (limitam e contabilizam recursos) e **union filesystems/OverlayFS** (empilham camadas da imagem com a camada gravável).
3. Porque containers **compartilham o kernel do host**; não há kernel próprio por container.
4. O **runc** cria o processo isolado (runtime de baixo nível, OCI); o **containerd** gerencia o ciclo de vida (runtime de alto nível).
5. *Open Container Initiative*: **Runtime Spec**, **Image Spec** e **Distribution Spec**.
6. `docker version` (a seção *Server* aparece apenas se o daemon responde).
7. Porque o socket do daemon permite criar containers com montagens e privilégios arbitrários. Demonstração (somente laboratório): `docker run --rm -v /etc:/host-etc alpine head -n 3 /host-etc/shadow`.
8. `sudo dockerd --validate --config-file=/etc/docker/daemon.json`.
9. `docker context create producao --docker "host=ssh://usuario@servidor"` e depois `docker context use producao` (ou `docker --context producao ps`).
10. (a) **Engine**; (b) **Docker Desktop** (ou Engine em uma distro WSL2); (c) **Engine**.

## Veja também

- [[O que é Docker]]
- [[Arquitetura do Docker]]
- [[Namespaces]]
- [[Cgroups - Docker]]
- [[Contextos do Docker]]
- [[Arquivo daemon.json]]
- [[MOC - Exercícios - Docker]]
