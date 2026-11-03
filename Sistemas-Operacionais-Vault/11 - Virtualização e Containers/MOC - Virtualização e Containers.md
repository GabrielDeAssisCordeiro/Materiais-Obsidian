---
titulo: "MOC - Virtualização e Containers"
tags:
  - sistemas-operacionais
  - moc
  - virtualizacao
tipo: moc
nivel: intermediario
relacionados:
  - "[[Virtualização]]"
  - "[[Hypervisors]]"
  - "[[Containers]]"
  - "[[Docker]]"
---

# MOC - Virtualização e Containers

> [!info] Escopo
> Como um único hardware ou kernel é dividido em vários ambientes isolados: máquinas virtuais (hypervisors) e contêineres (isolamento no nível do SO).

## Trilha

1. [[Virtualização]]: conceitos e técnicas (emulação, paravirtualização, suporte de hardware)
2. [[Hypervisors]]: tipo 1 x tipo 2, KVM, Xen, Hyper-V, VMware
3. [[Containers]]: isolamento por kernel compartilhado
4. [[Namespaces do Linux - SO]]: o que o contêiner enxerga
5. [[cgroups - SO]]: quanto o contêiner pode usar
6. [[Docker]]: imagens, camadas, execução, boas práticas

## Comparação rápida

| | Processo | Contêiner | MicroVM | VM completa |
|---|---|---|---|---|
| Kernel | Compartilhado | Compartilhado | Próprio | Próprio |
| Isolamento | Fraco | Médio | Forte | Forte |
| Inicialização | ms | ~100 ms-1 s | ~125 ms | segundos |
| Sobrecarga | Mínima | Baixa | Baixa | Alta |

## Relacionados

[[Sandboxing]] · [[Unikernel]] · [[Memória Virtual]] · [[DMA - Acesso Direto à Memória]] · [[Modos de Operação da CPU]]
