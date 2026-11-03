---
tags:
  - docker
  - producao
  - compose
  - hospedagem
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Deploy com Compose via SSH]]"
  - "[[Proxy reverso com Caddy]]"
  - "[[Hardening do host Docker]]"
  - "[[Checklist de produção]]"
---

# Hospedagem em VPS com Compose

Uma **VPS** (DigitalOcean, Hetzner, Linode, Oracle Cloud, EC2 etc.) com **Docker + Compose** é a hospedagem mais simples e barata para muitos projetos.

## Roteiro

```bash
# 1) Acesso e atualização
ssh root@IP
apt-get update && apt-get -y upgrade
adduser deploy && usermod -aG sudo deploy

# 2) SSH por chave; desabilitar login por senha e root (edite /etc/ssh/sshd_config.d/)
#    PasswordAuthentication no ; PermitRootLogin no
systemctl restart ssh

# 3) Firewall (atenção: portas publicadas pelo Docker contornam o ufw; veja a nota de firewall)
ufw allow OpenSSH && ufw allow 80,443/tcp && ufw enable

# 4) Instalar o Docker (veja a nota de instalação) e adicionar o usuário deploy ao grupo docker

# 5) Atualizações de segurança automáticas
apt-get install -y unattended-upgrades
```

## Stack mínima de produção

```yaml
services:
  caddy:                      # HTTPS automático
    image: caddy:2
    restart: unless-stopped
    ports: ["80:80", "443:443"]
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data
      - caddy_config:/config
    depends_on: [app]

  app:
    image: ghcr.io/org/app:1.4.2
    restart: unless-stopped
    env_file: .env
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:8080/health || exit 1"]
      interval: 15s
      retries: 3
    deploy:
      resources:
        limits: { cpus: "1.0", memory: 512M }

  db:
    image: postgres:16
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets: [db_password]
    volumes:
      - pg_data:/var/lib/postgresql/data

secrets:
  db_password:
    file: ./secrets/db_password.txt

volumes:
  caddy_data:
  caddy_config:
  pg_data:
```

`Caddyfile`:

```text
app.seudominio.com {
    reverse_proxy app:8080
}
```

> [!danger] `ufw` e Docker
> Não confie no `ufw` para bloquear portas publicadas por containers. Publique apenas 80/443 (do proxy) e deixe o restante só na rede interna. Veja [[iptables e firewall com Docker]].

> [!tip] Rotina
> Backups agendados ([[Backups em produção]]), monitoramento externo ([[Monitoramento em produção]]) e atualização periódica de imagens e do sistema.

## Exercício

Contrate (ou simule com uma VM) uma VPS, aplique o roteiro e coloque uma aplicação de teste com HTTPS em um subdomínio seu.

## Veja também

- [[Deploy com Compose via SSH]]
- [[Proxy reverso com Caddy]]
- [[Hardening do host Docker]]
- [[Checklist de produção]]
- [[MOC - Produção]]
