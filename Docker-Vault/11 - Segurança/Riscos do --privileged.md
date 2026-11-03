---
tags:
  - docker
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Capabilities Linux]]"
  - "[[Proteção do docker.sock]]"
  - "[[Escape de container]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Riscos do --privileged

`--privileged` entrega ao container **praticamente todos os poderes do host**:

- **Todas as capabilities** do Linux.
- Acesso a **todos os dispositivos** do host (`/dev`).
- **Desativa** seccomp e AppArmor/SELinux restritivos.
- Pode montar sistemas de arquivos e manipular o kernel.

## Veja a diferença (laboratório)

```bash
# Dispositivos visíveis: poucos vs praticamente todos
docker run --rm alpine:3.20 sh -c 'ls /dev | wc -l'
docker run --rm --privileged alpine:3.20 sh -c 'ls /dev | wc -l'

# Capabilities efetivas: padrão vs todas
docker run --rm alpine:3.20 grep CapEff /proc/self/status
docker run --rm --privileged alpine:3.20 grep CapEff /proc/self/status
```

> [!danger] Um container privilegiado comprometido compromete o host
> Se o processo for explorado, o invasor tem um caminho curto para o host. Nunca use `--privileged` em serviços expostos ou com imagens de terceiros.

## Alternativas mais seguras

| Necessidade | Em vez de `--privileged` |
|---|---|
| Acessar um dispositivo (USB, GPU, serial) | `--device /dev/ttyUSB0` ou `--gpus` |
| Operações de rede específicas | `--cap-add NET_ADMIN` |
| Depurar processos | `--cap-add SYS_PTRACE` |
| Docker dentro do Docker | Runners rootless, Sysbox, BuildKit rootless ou um daemon remoto |
| Montar sistemas de arquivos | Volumes e drivers apropriados |

```bash
# Auditoria: containers privilegiados em execução
docker ps -q | xargs -r docker inspect --format '{{.Name}} privileged={{.HostConfig.Privileged}}' | grep "privileged=true"
```

> [!warning] Docker-in-Docker (`dind`)
> Costuma exigir `--privileged`. Em CI compartilhado, prefira alternativas (Kaniko, Buildah, BuildKit rootless) ou runners isolados e descartáveis.

## Exercício

Execute os comandos de comparação, anote as diferenças e liste uma alternativa sem `--privileged` para dar acesso a um dispositivo específico.

## Veja também

- [[Capabilities Linux]]
- [[Proteção do docker.sock]]
- [[Escape de container]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Segurança]]
