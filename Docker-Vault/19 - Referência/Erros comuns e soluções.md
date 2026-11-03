---
tags:
  - docker
  - referencia
  - erros
  - troubleshooting
  - faq
aliases:
  - Troubleshooting Docker
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Fluxo de diagnóstico de problemas]]"
  - "[[Containers em loop de reinício]]"
  - "[[Depuração de rede]]"
  - "[[Cheat sheet de limpeza Docker]]"
  - "[[Pós-instalação no Linux]]"
---

# Erros comuns e soluções

Procure a mensagem de erro (ou parte dela) na primeira coluna.

## Daemon, instalação e permissões

| Erro | Causa | Solução |
|---|---|---|
| `permission denied while trying to connect to the Docker daemon socket` | Usuário fora do grupo `docker` (ou sessão antiga) | `sudo usermod -aG docker $USER` e novo login/`newgrp docker`. Veja [[Pós-instalação no Linux]] |
| `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?` | Daemon parado, `DOCKER_HOST` errado, contexto errado | `systemctl status docker`; `env \| grep DOCKER`; `docker context ls` |
| Docker Desktop não inicia (Windows) | WSL2/virtualização | `wsl --update`, habilite virtualização na BIOS. Veja [[Instalação no Windows com WSL2]] |
| `error during connect ... pipe/docker_engine` (Windows) | Docker Desktop fechado | Inicie o Docker Desktop |

## Pull, push e registry

| Erro | Causa | Solução |
|---|---|---|
| `manifest unknown` / `not found` | Tag inexistente | Confira a tag no registry |
| `pull access denied ... repository does not exist or may require 'docker login'` | Nome errado ou repositório privado | Verifique o nome; `docker login` |
| `toomanyrequests: You have reached your pull rate limit` | Limite de pulls do Docker Hub | Autentique-se, use espelho ou seu registry |
| `no matching manifest for linux/arm64/v8` | Imagem sem a arquitetura do host | `--platform linux/amd64` (emulação) ou outra imagem |
| `denied: requested access to the resource is denied` (push) | Sem permissão/namespace errado | `docker login`; nome `usuario/repo:tag` correto |
| `unauthorized: incorrect username or password` | Credenciais/token inválidos | Gere novo token; use `--password-stdin` |
| `x509: certificate signed by unknown authority` | Proxy corporativo/CA própria | Instale a CA no host/daemon ou configure o certificado do registry |
| `TLS handshake timeout` / `i/o timeout` | Rede, DNS, proxy | Teste `curl https://registry-1.docker.io/v2/`; configure proxy |
| `invalid reference format` | Nome com maiúsculas ou caracteres inválidos | Repositórios em minúsculas |

## Execução e portas

| Erro | Causa | Solução |
|---|---|---|
| `port is already allocated` / `address already in use` | Porta ocupada no host | `sudo ss -ltnp \| grep :PORTA`; troque a porta publicada |
| `Conflict. The container name "/x" is already in use` | Container com esse nome existe | `docker rm x` ou outro nome |
| Container **sai imediatamente** (exit 0) | Processo principal terminou (sem serviço em primeiro plano) | Verifique `CMD`/`ENTRYPOINT`; use um processo em primeiro plano. Veja [[Ciclo de vida do container]] |
| Container sai com **exit 1** | Erro da aplicação | `docker logs`; variáveis/arquivos ausentes |
| **exit 126 / 127** | Não executável / não encontrado | `chmod +x`, caminho correto, interpretador existe |
| **exit 137** | SIGKILL (inclui OOM) | `docker inspect -f '{{.State.OOMKilled}}'`. Veja [[Análise de OOM kill]] |
| **exit 139** | Segfault | Biblioteca/arquitetura incompatível |
| `exec format error` | Arquitetura errada ou script sem shebang | Imagem multiplataforma, `--platform`; shebang `#!/bin/sh` |
| `exec ./entrypoint.sh: no such file or directory` | CRLF no script, ou interpretador ausente (Alpine sem bash) | Converta para LF; use `sh` ou instale o interpretador |
| `OCI runtime create failed ... permission denied` | Binário sem permissão de execução, `noexec` | `chmod +x`; revise `tmpfs` com `noexec` |
| Aplicação inacessível de fora | Escuta em `127.0.0.1` ou falta `-p` | Escute em `0.0.0.0` e publique a porta |
| `driver failed programming external connectivity` | iptables/serviço de rede | Reinicie o Docker; verifique conflitos de firewall |

## Disco, volumes e redes

| Erro | Causa | Solução |
|---|---|---|
| `no space left on device` | Disco cheio (imagens, cache, logs, volumes) | `docker system df`; [[Limpeza com prune]]; rotação de logs |
| `volume is in use` | Container usa o volume | `docker rm` o container antes |
| `are you trying to mount a directory onto a file (or vice-versa)?` | Caminho do host é arquivo/diretório trocado | Crie o item correto antes de montar |
| `Permission denied` em bind mount (Linux) | UID/GID ou SELinux | `--user`, `chown`, `:z`/`:Z`. Veja [[Permissões e UID GID em volumes]] |
| `network has active endpoints` | Containers conectados | Desconecte/remova antes |
| `Could not resolve host` entre containers | Bridge padrão ou redes diferentes | Rede definida pelo usuário compartilhada |
| `Pool overlaps with other one on this address space` | Sub-rede conflita | Escolha outra faixa; `default-address-pools` |

## Build

| Erro | Causa | Solução |
|---|---|---|
| `COPY failed: file not found in build context` | Caminho fora do contexto ou ignorado no `.dockerignore` | Ajuste contexto/`.dockerignore` |
| `failed to solve: process "/bin/sh -c ..." did not complete successfully: exit code: N` | Falha do comando `RUN` | Veja a saída acima do erro; `--progress=plain` |
| `failed to solve: ... not found` (imagem base) | Tag inexistente | Verifique o `FROM` |
| `unknown instruction` / `dockerfile parse error` | Sintaxe/continuação de linha | Revise o Dockerfile |
| `docker build` demora sempre | Cache invalidado/contexto grande | [[Cache de camadas e ordem das instruções]], `.dockerignore` |
| `failed to read dockerfile: open Dockerfile: no such file` | Diretório/arquivo errado | `-f` e contexto corretos |

## Compose

| Erro | Causa | Solução |
|---|---|---|
| `yaml: line N: mapping values are not allowed here` | Indentação/espaços | Corrija o YAML; `docker compose config` |
| `service "x" refers to undefined network/volume` | Falta declarar em `networks:`/`volumes:` | Declare no nível superior |
| `dependency failed to start: container x is unhealthy` | Healthcheck falhou | `docker compose logs x`; ajuste o healthcheck |
| `the attribute 'version' is obsolete` | Campo obsoleto | Remova a linha `version:` |
| `variable is not set. Defaulting to a blank string` | Variável indefinida | `.env`, `${VAR:?erro}` ou valor padrão |
| `Bind for 0.0.0.0:80 failed: port is already allocated` | Porta ocupada | Troque a porta ou pare o outro serviço |

> [!tip] Método
> Leia a **primeira** mensagem de erro (não a última), reproduza com o menor exemplo possível e consulte [[Fluxo de diagnóstico de problemas]].

## Exercício

Provoque três erros desta tabela de propósito (porta ocupada, nome duplicado, `exec format error` com `--platform`) e resolva cada um sem consultar a nota.

## Veja também

- [[Fluxo de diagnóstico de problemas]]
- [[Containers em loop de reinício]]
- [[Depuração de rede]]
- [[Cheat sheet de limpeza Docker]]
- [[Pós-instalação no Linux]]
- [[MOC - Referência - Docker]]
