---
tags:
  - seguranca
aliases:
  - "Snapshot"
  - "Checkpoint"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Criar Sandbox com VMs]]"
  - "[[Descarte Seguro]]"
---
# Snapshots e Reversão

*Snapshots* capturam o estado de uma VM para reversão rápida.

| Boa prática | Motivo |
|---|---|
| Criar um snapshot "limpo" após instalar e atualizar | Estado conhecido e seguro |
| Reverter após **cada** análise | Evita contaminação entre amostras |
| Não confiar em snapshots como backup | Dependem do disco base |
| Evitar cadeias longas de snapshots | Desempenho e corrupção |
| Snapshots com memória podem conter segredos | Proteger e descartar |

```bash
virsh snapshot-list lab02
virsh snapshot-revert lab02 limpo
```

> [!warning] Reverter não cura o host
> Se houve fuga, o snapshot da VM não desfaz o dano no host.

## Exercício

Crie uma cadeia de 3 snapshots, meça o desempenho e consolide. Que diferença você observou?

## Veja também

- [[Criar Sandbox com VMs]]
- [[Descarte Seguro]]
- [[MOC - Cuidados e Segurança]]
