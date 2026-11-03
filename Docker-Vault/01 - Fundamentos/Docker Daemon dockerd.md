---
tags:
  - docker
  - fundamentos
  - daemon
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Arquitetura do Docker]]"
  - "[[Arquivo daemon.json]]"
  - "[[containerd e runc]]"
  - "[[Modo rootless]]"
---

# Docker Daemon dockerd

O **daemon** (`dockerd`) é o processo de longa duração que implementa a Engine API e gerencia objetos Docker: **imagens, containers, redes, volumes** e, opcionalmente, o modo Swarm.

## Responsabilidades

- Atender requisições da API (socket Unix, TCP, SSH via cliente).
- Gerenciar redes (bridges, iptables/nftables, DNS interno).
- Gerenciar volumes e o armazenamento de imagens (storage driver / image store).
- Delegar a execução de containers ao **containerd**.
- Aplicar políticas de restart e coletar logs via *logging drivers*.

## Operação no Linux (systemd)

```bash
# Estado do serviço
systemctl status docker

# Iniciar, parar e reiniciar
sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker

# Habilitar na inicialização do sistema
sudo systemctl enable docker.service containerd.service

# Logs do daemon
journalctl -u docker.service -n 100 --no-pager
```

## Diretório de dados

Por padrão o daemon armazena tudo em `/var/lib/docker` (imagens, containers, volumes, redes). Em disco pequeno, mova o `data-root` via [[Arquivo daemon.json]].

> [!tip] live-restore
> Com `"live-restore": true` no `daemon.json`, os containers continuam em execução durante uma reinicialização do daemon (por exemplo, para atualizações). Não é compatível com o modo Swarm.

> [!danger] Exposição do daemon via TCP
> Expor o daemon em `tcp://0.0.0.0:2375` **sem TLS** equivale a entregar acesso root à máquina para qualquer um na rede. Prefira SSH (`ssh://user@host`) ou TLS mútuo. Veja [[Contextos do Docker]].

## Veja também

- [[Arquitetura do Docker]]
- [[Arquivo daemon.json]]
- [[containerd e runc]]
- [[Modo rootless]]
- [[MOC - Fundamentos - Docker]]
