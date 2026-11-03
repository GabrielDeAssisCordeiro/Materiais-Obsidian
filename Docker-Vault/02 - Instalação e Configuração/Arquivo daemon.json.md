---
tags:
  - docker
  - instalacao
  - configuracao
  - daemon
  - json
aliases:
  - daemon.json
  - Configuração do daemon
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Daemon dockerd]]"
  - "[[Pós-instalação no Linux]]"
  - "[[Contextos do Docker]]"
  - "[[Modo rootless]]"
---

# Arquivo daemon.json

O `daemon.json` configura o daemon `dockerd` de forma persistente.

## Localização

| Ambiente | Caminho |
|---|---|
| Linux (Engine) | `/etc/docker/daemon.json` |
| Linux (rootless) | `~/.config/docker/daemon.json` |
| Windows (Engine) | `C:\ProgramData\docker\config\daemon.json` |
| Docker Desktop | **Settings → Docker Engine** (editor JSON na interface) |

## Exemplo comentado (JSON não aceita comentários; as explicações estão abaixo)

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m", "max-file": "3" },
  "live-restore": true,
  "default-address-pools": [
    { "base": "10.200.0.0/16", "size": 24 }
  ],
  "data-root": "/var/lib/docker",
  "features": { "buildkit": true }
}
```

| Chave | Efeito |
|---|---|
| `log-driver` / `log-opts` | Driver de log padrão e rotação de arquivos. |
| `live-restore` | Mantém containers rodando enquanto o daemon reinicia (incompatível com Swarm). |
| `default-address-pools` | Faixas de IP usadas pelas redes criadas; útil para evitar conflito com VPNs. |
| `data-root` | Diretório de dados do Docker (imagens, volumes, etc.). |
| `features.buildkit` | Define o uso do BuildKit no builder clássico. |

## Validar e aplicar

```bash
# Valida o arquivo sem iniciar o daemon
sudo dockerd --validate --config-file=/etc/docker/daemon.json

# Aplica (a maioria das chaves exige reinício do serviço)
sudo systemctl restart docker

# Confirma
docker info | grep -E "Logging Driver|Docker Root Dir|Live Restore"
```

> [!warning] Cuidado com conflitos
> Se a mesma opção é passada como flag no serviço systemd **e** no `daemon.json`, o daemon não inicia (erro de configuração duplicada). Mantenha uma única fonte.

> [!danger] Não exponha o daemon sem TLS
> A chave `hosts` com `tcp://0.0.0.0:2375` sem TLS dá acesso root remoto. Veja [[Docker Daemon dockerd]].

> [!question] Verificar na documentação oficial
> A lista completa de chaves e quais dependem de reinício está na referência `dockerd` da documentação oficial.

## Exercício

Configure rotação de logs (`max-size` e `max-file`), valide com `dockerd --validate`, reinicie o serviço e confirme o resultado com `docker info`.

## Veja também

- [[Docker Daemon dockerd]]
- [[Pós-instalação no Linux]]
- [[Contextos do Docker]]
- [[Modo rootless]]
- [[MOC - Instalação e Configuração]]
