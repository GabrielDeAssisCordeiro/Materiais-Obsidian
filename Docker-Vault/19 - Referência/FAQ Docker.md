---
tags:
  - docker
  - referencia
  - faq
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O que é Docker]]"
  - "[[Containers vs Máquinas Virtuais]]"
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Erros comuns e soluções]]"
---

# FAQ Docker

### Docker é gratuito?
O **Docker Engine** é open source e gratuito. O **Docker Desktop** é gratuito para uso pessoal, educação, projetos open source e pequenas empresas; empresas maiores precisam de assinatura. Consulte os termos atuais. Veja [[Docker Desktop vs Docker Engine]].

### Preciso do Docker Desktop no Linux?
Não. No Linux, o **Docker Engine** é o caminho normal (e o de produção).

### Qual a diferença entre imagem e container?
Imagem é o **modelo imutável**; container é a **instância em execução**. Veja [[Imagens vs Containers]].

### Container é uma máquina virtual?
Não: compartilha o kernel do host. Veja [[Containers vs Máquinas Virtuais]].

### Meus dados somem quando removo o container?
Os dados gravados na **camada gravável** sim. Use **volumes** para persistir. Veja [[Volumes nomeados]].

### Como containers se comunicam?
Pela mesma **rede definida pelo usuário**, usando o **nome** do container/serviço. Veja [[Redes bridge]].

### Como acesso um serviço do host a partir do container?
Use `host.docker.internal` (no Linux, `--add-host=host.docker.internal:host-gateway`). Veja [[Comunicação entre containers]].

### Por que meu container sai imediatamente?
O processo principal terminou. Veja [[Ciclo de vida do container]] e [[Erros comuns e soluções]].

### Como atualizo uma aplicação em execução?
Construa/baixe a **nova versão (tag)** e recrie o container (`docker compose pull && docker compose up -d`). Containers são descartáveis; não se atualizam "por dentro". Veja [[Estratégias de rollout]].

### Posso usar a tag `latest`?
Em estudos, sim. Em produção, **não**: fixe versões ou digests. Veja [[Tags e digests de imagens]].

### Como reduzo o tamanho da imagem?
Base menor, **multi-stage**, limpeza no mesmo `RUN`, `.dockerignore`. Veja [[Otimização de tamanho e tempo de build]].

### Posso rodar vários processos em um container?
É possível, mas o recomendado é **um processo principal por container** e vários containers por aplicação.

### Docker ou Kubernetes?
Não são concorrentes diretos: Docker constrói e executa containers; Kubernetes **orquestra** em cluster. Veja [[Compose vs Swarm vs Kubernetes]].

### Docker Compose v1 ou v2?
Use **v2** (`docker compose`). O `docker-compose` (v1) está descontinuado. Veja [[Visão geral do Docker Compose]].

### É seguro usar Docker em produção?
Sim, com boas práticas: usuário não-root, privilégios mínimos, segredos fora da imagem, atualização e varredura. Veja [[Checklist de segurança de containers]].

### Como libero espaço em disco?
`docker system df` e `docker image prune`/`builder prune`. Veja [[Cheat sheet de limpeza Docker]].

### Windows containers ou Linux containers?
A maioria dos casos usa **Linux containers** (inclusive no Windows via WSL2). Windows containers servem a aplicações .NET Framework e afins. Veja [[Instalação no Windows com WSL2]].

### Por que o ufw não bloqueia a porta do meu container?
O Docker manipula o firewall diretamente. Publique em `127.0.0.1` ou use `DOCKER-USER`. Veja [[iptables e firewall com Docker]].

## Veja também

- [[O que é Docker]]
- [[Containers vs Máquinas Virtuais]]
- [[Docker Desktop vs Docker Engine]]
- [[Erros comuns e soluções]]
- [[MOC - Referência - Docker]]
