---
tags:
  - docker
  - seguranca
  - host
  - hardening
aliases: []
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[CIS Docker Benchmark e Docker Bench for Security]]"
  - "[[Arquivo daemon.json]]"
  - "[[Docker Daemon dockerd]]"
  - "[[iptables e firewall com Docker]]"
---

# Hardening do host Docker

A segurança dos containers depende do **host** que os executa.

## Lista de medidas

| Área | Medida |
|---|---|
| Sistema | Kernel e pacotes atualizados; SO mínimo (Flatcar, Bottlerocket, Talos, ou distro enxuta) |
| Acesso | SSH com chave, sem root; restringir o grupo `docker` |
| Disco | Partição dedicada a `/var/lib/docker` |
| Firewall | Políticas de borda; regras em `DOCKER-USER`; publicar o mínimo |
| Daemon | TLS/SSH se remoto; `live-restore`; logs rotacionados; rootless quando possível |
| MAC | AppArmor/SELinux **ativos** |
| Auditoria | `auditd` monitorando `/usr/bin/dockerd`, `/var/lib/docker`, `/etc/docker`, `docker.sock` |
| Rede | Considerar `icc=false` na bridge padrão e usar redes definidas pelo usuário |
| Monitoramento | Logs centralizados e alertas |

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m", "max-file": "5" },
  "live-restore": true,
  "no-new-privileges": true,
  "userland-proxy": false
}
```

```bash
# Regras de auditoria (exemplo; persista em /etc/audit/rules.d/)
sudo auditctl -w /usr/bin/dockerd -k docker
sudo auditctl -w /var/lib/docker -k docker
sudo auditctl -w /etc/docker -k docker
sudo auditctl -w /run/docker.sock -k docker
```

> [!question] Verificar na documentação oficial
> A chave `no-new-privileges` no `daemon.json` e a opção `userland-proxy` dependem da versão do Engine; valide com `dockerd --validate`.

> [!tip] Menos é mais
> Evite rodar outros serviços no mesmo host. Um host dedicado a containers, com acesso restrito, simplifica a defesa.

## Exercício

Aplique ao menos cinco medidas da tabela em uma VM de laboratório e rode o Docker Bench antes e depois.

## Veja também

- [[CIS Docker Benchmark e Docker Bench for Security]]
- [[Arquivo daemon.json]]
- [[Docker Daemon dockerd]]
- [[iptables e firewall com Docker]]
- [[MOC - Segurança]]
