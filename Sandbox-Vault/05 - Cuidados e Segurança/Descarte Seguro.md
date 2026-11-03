---
tags:
  - seguranca
aliases:
  - "Teardown"
  - "Destruição de ambientes"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Snapshots e Reversão]]"
  - "[[Conformidade e LGPD]]"
---
# Descarte Seguro

Ambientes efêmeros devem ser **destruídos por completo**.

- Remova containers, volumes, redes e imagens temporárias: `docker system prune -a --volumes` (cuidado: remove tudo que não está em uso).
- Apague discos de VMs e snapshots; apague com segurança se contiverem dados sensíveis.
- Revogue tokens e chaves usados na sandbox.
- Registre a destruição (data/responsável) quando houver exigência de conformidade.

```bash
docker rm -f $(docker ps -aq) 2>/dev/null
docker volume prune -f
VBoxManage unregistervm lab01 --delete
```

> [!warning] Discos de VM podem manter dados
> Para dados sensíveis, use criptografia de disco e destrua a chave ao descartar.

## Exercício

Escreva um script de limpeza para o seu laboratório e teste-o.

## Veja também

- [[Snapshots e Reversão]]
- [[Conformidade e LGPD]]
- [[Gerenciamento de Segredos e Credenciais]]
- [[MOC - Cuidados e Segurança]]
