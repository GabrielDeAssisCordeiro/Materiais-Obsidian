---
tags:
  - docker
  - instalacao
  - linux
  - permissoes
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Instalação no Linux]]"
  - "[[Modo rootless]]"
  - "[[Verificando com hello-world]]"
  - "[[Docker Daemon dockerd]]"
---

# Pós-instalação no Linux

Depois de instalar o Engine no Linux, o socket do Docker pertence ao usuário `root` e ao grupo `docker`. Por isso, sem ajustes, comandos exigem `sudo`.

## Usar Docker sem sudo

```bash
# Cria o grupo (normalmente já existe)
sudo groupadd docker 2>/dev/null || true

# Adiciona o usuário atual ao grupo
sudo usermod -aG docker $USER

# Aplica o novo grupo na sessão atual (ou faça logout/login)
newgrp docker

# Teste sem sudo
docker run --rm hello-world
```

> [!danger] O grupo docker equivale a root
> Qualquer membro do grupo `docker` pode montar o sistema de arquivos do host em um container e obter privilégios de root no host. Adicione apenas usuários confiáveis ou use o [[Modo rootless]].
> ```bash
> # Demonstração do risco (em máquina de laboratório!)
> docker run --rm -v /etc:/host-etc alpine head -n 3 /host-etc/shadow
> ```

## Iniciar o Docker na inicialização

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# Para desabilitar
sudo systemctl disable docker.service docker.socket containerd.service
```

## Limitar o crescimento dos logs

Por padrão o driver `json-file` não rotaciona logs. Configure no [[Arquivo daemon.json]]:

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m", "max-file": "3" }
}
```

> [!bug] "permission denied while trying to connect to the Docker daemon socket"
> Causas comuns: usuário fora do grupo `docker` (ou sessão sem relogin), ou daemon parado. Confira `id`, `systemctl status docker` e `ls -l /var/run/docker.sock`.

## Exercício

Adicione seu usuário ao grupo `docker`, faça logout/login e confirme com `id` e `docker ps`. Em seguida, explique por que isso não é seguro em servidores compartilhados.

## Veja também

- [[Instalação no Linux]]
- [[Modo rootless]]
- [[Verificando com hello-world]]
- [[Docker Daemon dockerd]]
- [[MOC - Instalação e Configuração]]
