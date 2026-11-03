---
tags:
  - como-criar
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Sandbox por MicroVMs]]"
  - "[[Sandbox por Virtualização Completa]]"
---
# Criar Sandbox com Firecracker

**Pré-requisitos:** Linux com KVM (`ls /dev/kvm`), binário do Firecracker, imagem de kernel (`vmlinux`) e *rootfs* (`.ext4`).

```bash
ls -l /dev/kvm                      # deve existir
# Baixe o binário na página oficial de releases e kernel/rootfs conforme o guia 'getting started'
```

## Configuração por arquivo (`vmconfig.json`)

```json
{
  "boot-source": {
    "kernel_image_path": "vmlinux",
    "boot_args": "console=ttyS0 reboot=k panic=1 pci=off"
  },
  "drives": [
    {
      "drive_id": "rootfs",
      "path_on_host": "rootfs.ext4",
      "is_root_device": true,
      "is_read_only": false
    }
  ],
  "machine-config": {
    "vcpu_count": 1,
    "mem_size_mib": 256
  }
}
```

```bash
rm -f /tmp/fc.sock
./firecracker --api-sock /tmp/fc.sock --config-file vmconfig.json
```

Sem interface de rede configurada, a microVM **não tem rede**, o que é ótimo para código não confiável.

> [!info] Jailer
> Em produção, use o `jailer`: ele aplica chroot, namespaces, cgroups e seccomp ao próprio processo do Firecracker.

> [!question] Verificar na documentação oficial
> Parâmetros de boot, formatos de imagem e endpoints da API mudam entre versões; siga o guia oficial da versão instalada.

## Exercício

Inicie a microVM, rode `uname -a` e `ip a` no guest e confirme a ausência de interface de rede.

## Veja também

- [[Sandbox por MicroVMs]]
- [[Sandbox em Nuvem]]
- [[Criar Sandbox para Código de IA]]
- [[MOC - Como Criar]]
