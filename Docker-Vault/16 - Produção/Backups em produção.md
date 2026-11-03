---
tags:
  - docker
  - producao
  - backup
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Backup e restauração de volumes]]"
  - "[[Persistência de bancos de dados]]"
  - "[[Checklist de produção]]"
---

# Backups em produção

Containers são descartáveis; **os dados não**. Defina **o que**, **com que frequência**, **onde** e **como restaurar**.

## O que fazer backup

| Item | Como |
|---|---|
| Bancos de dados | Dump lógico (`pg_dump`, `mysqldump`) ou backup físico/PITR |
| Volumes de arquivos (uploads) | `tar` de volume, `restic`, `borg` |
| Configuração | `compose.yaml`, `.env.example`, infra em Git |
| Segredos | Cofre com backup próprio (nunca no repositório) |
| Imagens | Reprodutíveis do registry (garanta retenção da versão em produção) |

## Script de backup (exemplo)

```bash
#!/usr/bin/env bash
set -euo pipefail

DEST=/backups/$(date +%F)
mkdir -p "$DEST"

# Banco: dump consistente
docker exec pg pg_dump -U postgres -Fc appdb > "$DEST/appdb.dump"

# Volume de uploads
docker run --rm -v uploads:/dados:ro -v "$DEST":/backup alpine:3.20 \
  tar czf /backup/uploads.tar.gz -C /dados .

# Envio para fora do servidor (exemplo com restic; configure o repositório antes)
restic -r s3:s3.amazonaws.com/meu-bucket/backups backup "$DEST"

# Retenção local
find /backups -mindepth 1 -maxdepth 1 -mtime +7 -exec rm -rf {} +
```

```cron
# crontab: todos os dias às 02:30
30 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```

## Regra 3-2-1

**3** cópias, em **2** mídias diferentes, **1** fora do local (offsite).

> [!danger] Backup não testado é só esperança
> Agende **restaurações de teste** periódicas em ambiente separado e meça RTO/RPO (tempo e perda de dados aceitáveis).

> [!warning] Criptografe e proteja
> Backups contêm dados sensíveis. Criptografe em trânsito e em repouso, restrinja o acesso e proteja contra *ransomware* (cópias imutáveis/versionadas).

## Exercício

Implemente o script acima para um serviço seu, execute-o, destrua o ambiente de laboratório e restaure a partir do backup, cronometrando o processo.

## Veja também

- [[Backup e restauração de volumes]]
- [[Persistência de bancos de dados]]
- [[Checklist de produção]]
- [[MOC - Produção]]
