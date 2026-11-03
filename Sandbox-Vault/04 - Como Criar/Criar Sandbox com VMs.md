---
tags:
  - como-criar
aliases:
  - "VirtualBox"
  - "QEMU"
  - "VMware"
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Virtualização Completa]]"
  - "[[Hipervisores Tipo 1 e Tipo 2]]"
  - "[[Criar Laboratório de Malware Seguro]]"
---
# Criar Sandbox com VMs

## VirtualBox (linha de comando)

```bash
VBoxManage createvm --name lab01 --ostype Ubuntu_64 --register
VBoxManage modifyvm lab01 --memory 4096 --cpus 2 --nic1 intnet --intnet1 labnet \
  --clipboard-mode disabled --draganddrop disabled
VBoxManage createmedium disk --filename ~/VMs/lab01.vdi --size 30000
VBoxManage storagectl lab01 --name SATA --add sata
VBoxManage storageattach lab01 --storagectl SATA --port 0 --device 0 --type hdd --medium ~/VMs/lab01.vdi
VBoxManage storageattach lab01 --storagectl SATA --port 1 --device 0 --type dvddrive --medium ~/ISOs/ubuntu.iso

VBoxManage snapshot lab01 take "limpo"      # após instalar e atualizar
VBoxManage snapshot lab01 restore "limpo"   # reverter ao estado limpo
```

`--nic1 intnet` coloca a VM em **rede interna** (sem acesso ao host nem à internet).

## KVM/libvirt (Linux)

```bash
sudo apt install qemu-kvm libvirt-daemon-system virtinst
virt-install --name lab02 --memory 4096 --vcpus 2 \
  --disk size=30 --cdrom ~/ISOs/ubuntu.iso \
  --os-variant ubuntu22.04 --network none --graphics spice
virsh snapshot-create-as lab02 limpo
virsh snapshot-revert lab02 limpo
```

## Hyper-V (PowerShell)

```powershell
New-VM -Name Lab03 -MemoryStartupBytes 4GB -Generation 2 -NewVHDPath C:\VMs\Lab03.vhdx -NewVHDSizeBytes 40GB
Set-VM -Name Lab03 -CheckpointType Standard
Checkpoint-VM -Name Lab03 -SnapshotName limpo
Restore-VMCheckpoint -VMName Lab03 -Name limpo -Confirm:$false
```

> [!danger] Guest Additions, pastas compartilhadas e USB
> Cada integração é um canal para o host. Desative o que não for essencial e nunca conecte USB do host a VMs de análise.

> [!question] Verificar na documentação oficial
> Nomes de opções do `VBoxManage` e do `virt-install` mudam entre versões (`--os-variant`, `--clipboard-mode`). Use `--help` e a documentação.

## Exercício

Crie uma VM com rede interna, tire um snapshot, instale um pacote qualquer e volte ao snapshot. O pacote sumiu?

## Veja também

- [[Sandbox por Virtualização Completa]]
- [[Hipervisores Tipo 1 e Tipo 2]]
- [[Criar Sandbox com Vagrant]]
- [[Fuga de Sandbox]]
- [[MOC - Como Criar]]
