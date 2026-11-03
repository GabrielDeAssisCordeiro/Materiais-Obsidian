---
tags:
  - como-criar
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Kernel em Espaço de Usuário]]"
  - "[[Criar Sandbox com Docker]]"
---
# Criar Sandbox com gVisor

```bash
# 1) Instale o runsc seguindo a documentação oficial do gVisor para sua distribuição
# 2) Registre o runtime no Docker
sudo runsc install
sudo systemctl restart docker

# 3) Rode um container sob gVisor
docker run --rm --runtime=runsc alpine:3 dmesg
```

Se estiver sob gVisor, o `dmesg` exibirá mensagens do próprio gVisor, não do kernel do host.

Equivalente manual em `/etc/docker/daemon.json`:

```json
{
  "runtimes": {
    "runsc": { "path": "/usr/local/bin/runsc" }
  }
}
```

Combine com as restrições de [[Criar Sandbox com Docker]]:

```bash
docker run --rm --runtime=runsc --network none --read-only --cap-drop=ALL \
  --memory 256m --pids-limit 100 alpine:3 echo seguro
```

> [!question] Verificar na documentação oficial
> Plataforma de interceptação (systrap/KVM), caminho de instalação e compatibilidade variam por versão.

## Exercício

Compare a saída de `dmesg` com e sem `--runtime=runsc`.

## Veja também

- [[Sandbox por Kernel em Espaço de Usuário]]
- [[Criar Sandbox com Docker]]
- [[Sandbox por MicroVMs]]
- [[MOC - Como Criar]]
