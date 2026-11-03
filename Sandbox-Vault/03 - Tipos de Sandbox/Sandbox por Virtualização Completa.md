---
tags:
  - tipos
aliases:
  - "VM sandbox"
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Hipervisores Tipo 1 e Tipo 2]]"
  - "[[Criar Sandbox com VMs]]"
  - "[[Caso - Análise de Malware]]"
---
# Sandbox por Virtualização Completa

Uma **VM** emula um computador completo, com kernel próprio. A fronteira é o hipervisor — bem menor que o kernel inteiro.

**Vantagens:** isolamento forte, *snapshots*, qualquer SO convidado.
**Desvantagens:** mais pesada (memória, disco, tempo de boot), integração ("Guest Additions") pode abrir brechas.

| Ferramenta | SO host | Observação |
|---|---|---|
| VirtualBox | Win/Linux/macOS | Gratuito |
| VMware Workstation/Fusion | Win/Linux/macOS | Verifique licenciamento atual |
| KVM/QEMU/libvirt | Linux | Nativo e flexível |
| Hyper-V | Windows | Integrado ao Windows Pro |

> [!warning] Desative integrações desnecessárias
> Pastas compartilhadas, área de transferência e arrastar-e-soltar criam canais entre convidado e host.

## Exercício

Compare o tempo de boot e o uso de RAM de uma VM Linux mínima com um container Alpine.

## Veja também

- [[Hipervisores Tipo 1 e Tipo 2]]
- [[Criar Sandbox com VMs]]
- [[Fuga de Sandbox]]
- [[MOC - Tipos de Sandbox]]
