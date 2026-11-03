---
tags:
  - docker
  - instalacao
  - seguranca
  - linux
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Pós-instalação no Linux]]"
  - "[[Namespaces]]"
  - "[[Docker Daemon dockerd]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Modo rootless

No **modo rootless**, tanto o daemon quanto os containers rodam **sem privilégios de root** no host, usando *user namespaces*. Um escape de container resulta apenas em acesso como usuário comum, o que reduz muito o impacto.

## Pré-requisitos (Ubuntu/Debian)

```bash
sudo apt-get install -y uidmap dbus-user-session

# Confirme que seu usuário tem faixas em /etc/subuid e /etc/subgid
grep "^$USER:" /etc/subuid /etc/subgid
```

O pacote `docker-ce-rootless-extras` (instalado junto com o Engine ou separadamente) fornece o script de configuração.

## Instalação

```bash
# Se o daemon "rootful" estiver rodando e você quiser apenas o rootless, desabilite-o:
sudo systemctl disable --now docker.service docker.socket

# Configura o daemon rootless para o usuário atual
dockerd-rootless-setuptool.sh install

# Inicia e habilita como serviço de usuário
systemctl --user start docker
systemctl --user enable docker

# Mantém o serviço ativo sem login ativo
sudo loginctl enable-linger $(whoami)

# Aponta o cliente para o socket do usuário
export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock
docker run --rm hello-world
```

## Limitações importantes

| Limitação | Alternativa |
|---|---|
| Portas abaixo de 1024 não podem ser publicadas por usuários comuns | `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=0` ou publicar portas altas atrás de um proxy |
| Algumas redes (macvlan, overlay) e storage drivers não são suportados | Usar bridge padrão |
| Limites de recursos (cgroups) exigem cgroup v2 e delegação via systemd | Verificar `docker info` |
| Desempenho de rede ligeiramente menor (rootlesskit / slirp4netns / pasta) | Aceitável para a maioria dos casos |

> [!tip] Rootless vs userns-remap
> `userns-remap` mantém o daemon como root e mapeia apenas os containers. Rootless coloca **também o daemon** sem privilégios, sendo mais restritivo. Veja [[Namespaces]].

> [!question] Verificar na documentação oficial
> Detalhes de rede rootless (slirp4netns vs pasta), suporte a AppArmor e requisitos de kernel variam por versão. Consulte "Rootless mode" na documentação do Engine.

## Exercício

Em uma VM de laboratório, instale o modo rootless, execute `docker info` e identifique no campo *Security Options* a presença de `rootless`.

## Veja também

- [[Pós-instalação no Linux]]
- [[Namespaces]]
- [[Docker Daemon dockerd]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Instalação e Configuração]]
