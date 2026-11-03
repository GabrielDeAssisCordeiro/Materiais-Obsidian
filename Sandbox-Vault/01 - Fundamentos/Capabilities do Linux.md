---
tags:
  - fundamentos
  - linux
  - kernel
aliases:
  - "Linux capabilities"
  - "CAP_*"
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do Menor Privilégio]]"
  - "[[Namespaces do Linux]]"
  - "[[Cgroups]]"
  - "[[Seccomp]]"
---
# Capabilities do Linux

Tradicionalmente o `root` (UID 0) pode tudo. As **capabilities** dividem esse superpoder em dezenas de permissões independentes, que podem ser concedidas ou retiradas separadamente de um processo.

## Exemplos

| Capability | Permite |
|---|---|
| `CAP_NET_BIND_SERVICE` | Escutar portas abaixo de 1024 |
| `CAP_NET_RAW` | Sockets brutos (ping, sniffers) |
| `CAP_CHOWN` | Alterar dono de arquivos |
| `CAP_SYS_PTRACE` | Depurar/inspecionar outros processos |
| `CAP_NET_ADMIN` | Configurar rede, firewall |
| `CAP_SYS_ADMIN` | Enorme conjunto de operações — "o novo root" |

> [!danger] Evite `CAP_SYS_ADMIN` e `--privileged`
> `--privileged` concede praticamente todas as capabilities e acesso a dispositivos do host. Em sandbox, trate como proibido.

## Inspecionando

```bash
capsh --print                      # capabilities do shell atual
grep Cap /proc/self/status         # máscaras em hexadecimal
capsh --decode=00000000a80425fb    # decodificar uma máscara (exemplo)
```

## Aplicando em containers

```bash
# Remove tudo e devolve só o necessário
docker run --rm --cap-drop=ALL --cap-add=NET_BIND_SERVICE \
  --security-opt no-new-privileges alpine:3 id
```

`no-new-privileges` impede que o processo ganhe privilégios por `setuid`/capabilities de arquivo.

> [!info] Modelo mental
> Capabilities respondem "**o que o root pode fazer**". [[Seccomp]] responde "**quais chamadas de sistema** são aceitas". Use ambos.

## Exercício

Rode `docker run --rm alpine sh -c 'grep Cap /proc/self/status'` com e sem `--cap-drop=ALL` e compare `CapEff`.

## Veja também

- [[Princípio do Menor Privilégio]]
- [[Namespaces do Linux]]
- [[Seccomp]]
- [[Cgroups]]
- [[Sandbox por Containers]]
