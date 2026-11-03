---
tags:
  - docker
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Modo rootless]]"
  - "[[Namespaces]]"
  - "[[Containers não-root]]"
---

# User namespaces e userns-remap

Com **user namespaces**, o UID 0 dentro do container é mapeado para um **UID sem privilégio no host** (por exemplo, 100000). Se um processo escapar, ele não será root do host.

## `userns-remap` (daemon rootful)

```json
{
  "userns-remap": "default"
}
```

```bash
# Após reiniciar o daemon, o Docker cria o usuário dockremap
sudo systemctl restart docker
grep dockremap /etc/subuid /etc/subgid

# O root do container aparece como UID alto no host
docker run -d --name teste alpine:3.20 sleep 300
ps -o user,pid,cmd -C sleep
docker rm -f teste
```

## Comparação

| | `userns-remap` | Modo rootless |
|---|---|---|
| Daemon roda como | root | usuário comum |
| Containers | Mapeados para faixa de subuid | Mapeados para subuid do usuário |
| Impacto de comprometimento do daemon | Alto | Baixo |
| Facilidade | Média (um ajuste global) | Média (instalação separada) |

> [!warning] Limitações do `userns-remap`
> Incompatível com `--privileged`, `--network host` e `--pid host` sem exceção por container (`--userns=host`), e as imagens e volumes passam a ficar em um diretório de dados separado (`/var/lib/docker/<uid>.<gid>`): imagens existentes "somem" ao ativar.

> [!question] Verificar na documentação oficial
> Confirme as restrições atuais e o comportamento de volumes em "Isolate containers with a user namespace".

## Exercício

Em uma VM de laboratório, ative `userns-remap`, execute `sleep` em um container e identifique o UID do processo no host.

## Veja também

- [[Modo rootless]]
- [[Namespaces]]
- [[Containers não-root]]
- [[MOC - Segurança]]
