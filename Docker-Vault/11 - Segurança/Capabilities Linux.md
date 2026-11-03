---
tags:
  - docker
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Riscos do --privileged]]"
  - "[[Opções security-opt e no-new-privileges]]"
---

# Capabilities Linux

O poder do root no Linux é dividido em **capabilities** (ex.: `NET_BIND_SERVICE`, `CHOWN`, `SYS_ADMIN`). O Docker concede aos containers um **subconjunto padrão** e permite ajustar.

## Capabilities concedidas por padrão

`CHOWN`, `DAC_OVERRIDE`, `FSETID`, `FOWNER`, `MKNOD`, `NET_RAW`, `SETGID`, `SETUID`, `SETFCAP`, `SETPCAP`, `NET_BIND_SERVICE`, `SYS_CHROOT`, `KILL`, `AUDIT_WRITE`.

```bash
# Ver as capabilities (campo CapEff em hexadecimal)
docker run --rm alpine:3.20 grep Cap /proc/self/status

# Sem nenhuma capability
docker run --rm --cap-drop ALL alpine:3.20 grep CapEff /proc/self/status

# Remove tudo e concede apenas o necessário (bind em porta baixa)
docker run -d --name web --cap-drop ALL --cap-add NET_BIND_SERVICE \
  -p 8080:80 nginx:1.27
```

```bash
# Decodificar um valor em hexadecimal (pacote libcap, no host)
capsh --decode=00000000a80425fb
```

| Capability | Risco |
|---|---|
| `SYS_ADMIN` | Muito ampla ("quase root"); evite |
| `NET_ADMIN` | Altera rede/firewall do namespace |
| `SYS_PTRACE` | Depurar outros processos |
| `NET_RAW` | Criar sockets *raw* (spoofing/ARP); considere remover |

> [!tip] Padrão recomendado
> `--cap-drop ALL` e `--cap-add` somente das necessárias. Muitas aplicações web não precisam de nenhuma.

> [!danger] `--cap-add SYS_ADMIN` e `--privileged`
> Concedem capacidade suficiente para quebrar o isolamento em vários cenários. Trate como exceção justificada. Veja [[Riscos do --privileged]].

## Exercício

Rode o Nginx com `--cap-drop ALL`; veja o erro, adicione `CHOWN`, `SETUID`, `SETGID` e `NET_BIND_SERVICE` conforme necessário e documente o conjunto mínimo.

## Veja também

- [[Princípio do menor privilégio - Docker]]
- [[Riscos do --privileged]]
- [[Opções security-opt e no-new-privileges]]
- [[MOC - Segurança]]
