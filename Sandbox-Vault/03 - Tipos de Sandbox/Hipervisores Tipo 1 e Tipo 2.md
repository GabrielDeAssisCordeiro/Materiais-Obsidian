---
tags:
  - tipos
aliases:
  - "Hypervisor"
  - "KVM"
  - "Hyper-V"
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Virtualização Completa]]"
  - "[[Sandbox por MicroVMs]]"
---
# Hipervisores Tipo 1 e Tipo 2

Hipervisores criam e gerenciam máquinas virtuais.

| Tipo | Roda... | Exemplos |
|---|---|---|
| **Tipo 1** (*bare metal*) | Diretamente sobre o hardware | VMware ESXi, Xen, Microsoft Hyper-V, Proxmox (KVM) |
| **Tipo 2** (*hospedado*) | Como aplicativo em um SO | VirtualBox, VMware Workstation/Fusion, QEMU sem KVM |

> [!info] KVM
> O KVM transforma o kernel Linux em hipervisor; com QEMU como emulador de dispositivos, forma uma pilha de virtualização completa. A fronteira entre os tipos é, na prática, nebulosa.

Veja [[Sandbox por Virtualização Completa]].

## Veja também

- [[Sandbox por Virtualização Completa]]
- [[Sandbox por MicroVMs]]
- [[Criar Sandbox com VMs]]
