---
tags:
  - ferramentas
aliases:
  - "runsc"
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Kernel em Espaço de Usuário]]"
  - "[[Criar Sandbox com gVisor]]"
---
# Ferramenta - gVisor

Runtime OCI (`runsc`) que fornece um "kernel" em espaço de usuário. Bom equilíbrio entre containers e VMs; custo em desempenho de E/S e compatibilidade parcial.

```bash
docker run --rm --runtime=runsc alpine:3 uname -a
```

## Veja também

- [[Criar Sandbox com gVisor]]
- [[Sandbox por Kernel em Espaço de Usuário]]
- [[Comparativo de Ferramentas]]
- [[MOC - Ferramentas]]
