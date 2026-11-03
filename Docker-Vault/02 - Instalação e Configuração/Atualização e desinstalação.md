---
tags:
  - docker
  - instalacao
  - manutencao
  - linux
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Instalação no Linux]]"
  - "[[Arquivo daemon.json]]"
  - "[[Pós-instalação no Linux]]"
  - "[[Docker Daemon dockerd]]"
---

# Atualização e desinstalação

## Atualizando o Docker Engine (Ubuntu/Debian)

```bash
# Verifique a versão atual
docker version --format '{{.Server.Version}}'

# Atualiza índices e pacotes do Docker
sudo apt-get update
sudo apt-get install --only-upgrade -y docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

> [!tip] Reduza o downtime
> Com `live-restore: true` no [[Arquivo daemon.json]], os containers sobrevivem à reinicialização do daemon durante a atualização. Teste em ambiente de homologação antes de atualizar produção e leia as notas de versão (principalmente em mudanças de versão maior).

## Docker Desktop

O Docker Desktop avisa sobre atualizações e as instala pela própria interface. Em Windows e macOS, baixe a versão nova do site oficial se preferir atualizar manualmente.

## Desinstalando o Engine (Ubuntu/Debian)

```bash
# Remove os pacotes
sudo apt-get purge -y docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
sudo apt-get autoremove -y

# Remove repositório e chave
sudo rm -f /etc/apt/sources.list.d/docker.list /etc/apt/keyrings/docker.asc
```

> [!danger] Apagar dados é irreversível
> Os comandos abaixo removem **todas** as imagens, containers e volumes. Faça backup de volumes importantes antes.
> ```bash
> sudo rm -rf /var/lib/docker
> sudo rm -rf /var/lib/containerd
> ```
> Remova também `/etc/docker/` se quiser descartar a configuração.

## Limpeza sem desinstalar

```bash
# Remove containers parados, redes sem uso, imagens sem tag (dangling) e cache de build
docker system prune

# Inclui imagens sem uso e volumes anônimos sem uso (use com cuidado)
docker system prune -a --volumes
```

## Exercício

Em VM de laboratório: anote a versão do Engine, atualize os pacotes, confirme a nova versão e verifique que um container criado antes continua listado em `docker ps -a`.

## Veja também

- [[Instalação no Linux]]
- [[Arquivo daemon.json]]
- [[Pós-instalação no Linux]]
- [[Docker Daemon dockerd]]
- [[MOC - Instalação e Configuração]]
