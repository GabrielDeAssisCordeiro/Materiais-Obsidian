---
tags:
  - referencia
aliases:
  - "Cheat sheet VMs"
tipo: cheatsheet
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Criar Sandbox com VMs]]"
  - "[[Criar Sandbox com Vagrant]]"
---
# Cheat Sheet - VMs

```bash
# VirtualBox
VBoxManage list vms
VBoxManage modifyvm VM --nic1 intnet --intnet1 labnet --clipboard-mode disabled --draganddrop disabled
VBoxManage snapshot VM take limpo
VBoxManage snapshot VM restore limpo
VBoxManage unregistervm VM --delete

# KVM/libvirt
virsh list --all
virsh snapshot-create-as VM limpo
virsh snapshot-revert VM limpo
virsh destroy VM && virsh undefine VM --remove-all-storage

# Vagrant
vagrant up ; vagrant ssh ; vagrant snapshot save limpo ; vagrant snapshot restore limpo ; vagrant destroy -f
```

```powershell
# Hyper-V
Checkpoint-VM -Name Lab03 -SnapshotName limpo
Restore-VMCheckpoint -VMName Lab03 -Name limpo -Confirm:$false
```

## Veja também

- [[Glossário#Sandboxes e isolamento]]
- [[Cheat Sheet - Docker e Podman]]
- [[Cheat Sheet - Isolamento no Linux]]
- [[MOC - Referência - Sandbox]]
