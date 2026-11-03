---
titulo: "mount"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[VFS - Virtual File System]]"
  - "[[df e du]]"
  - "[[Sistemas de Arquivos - Conceitos]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# mount

## Finalidade

**Anexa** um sistema de arquivos (de uma partição, imagem, rede ou pseudo-FS) a um **ponto de montagem** da árvore de diretórios ([[VFS - Virtual File System]]). Sem argumentos, lista as montagens. `umount` desfaz.

## Sintaxe

```bash
mount                                   # lista (prefira findmnt)
findmnt                                 # árvore de montagens, legível
findmnt -t ext4,xfs,btrfs
findmnt /home                           # detalhes de um ponto
sudo mount /dev/sdb1 /mnt/dados         # detecta o tipo
sudo mount -t ext4 -o ro,noatime /dev/sdb1 /mnt/dados
sudo mount -o remount,rw /              # altera opções de FS já montado
sudo mount -t tmpfs -o size=512M tmpfs /mnt/ram
sudo mount --bind /origem /destino      # espelha um diretório em outro lugar
sudo mount -o loop imagem.iso /mnt/iso  # monta arquivo-imagem
sudo mount -t nfs servidor:/export /mnt/nfs
sudo mount -t cifs //srv/share /mnt/smb -o username=ana
sudo umount /mnt/dados                  # desmonta;  -l lazy  -f força
mount -a                                # monta tudo de /etc/fstab
lsblk -f; blkid                         # UUIDs e tipos para identificar
```

## `/etc/fstab`

```text
# <dispositivo>      <ponto>   <tipo> <opções>                   <dump> <pass>
UUID=3f9c-...        /         ext4   defaults,noatime,errors=remount-ro  0  1
UUID=A1B2-C3D4       /boot/efi vfat   umask=0077                 0  2
UUID=7d88-...        /dados    xfs    defaults,nofail            0  2
/swapfile            none      swap   sw                         0  0
servidor:/export     /mnt/nfs  nfs    _netdev,noauto,x-systemd.automount  0 0
tmpfs                /tmp      tmpfs  size=2G,mode=1777          0  0
```

| Opção | Efeito |
|---|---|
| `defaults` | `rw,suid,dev,exec,auto,nouser,async` |
| `noatime` / `relatime` | Não atualiza (ou atualiza menos) o tempo de acesso |
| `ro` / `rw` | Somente leitura / leitura-escrita |
| `noexec`, `nosuid`, `nodev` | **Endurecimento**: impede executar, setuid e dispositivos (`/tmp`, mídia externa) |
| `nofail` | Não trava o boot se o dispositivo faltar |
| `_netdev` | Espera a rede |
| `x-systemd.automount` | Monta sob demanda |
| `discard` | TRIM contínuo em SSD |
| `uid=,gid=,umask=` | Permissões em FAT/NTFS/exFAT |

> [!warning] Erros em `fstab` podem impedir o boot
> Use UUID (não `/dev/sdX`, que pode mudar), `nofail` em discos externos, e **teste** antes de reiniciar: `sudo mount -a` e `sudo findmnt --verify`.

## Saída comentada

```text
$ findmnt -t ext4,vfat,tmpfs
TARGET        SOURCE      FSTYPE OPTIONS
/             /dev/sda2   ext4   rw,noatime,errors=remount-ro
├─/boot/efi   /dev/sda1   vfat   rw,relatime,fmask=0077
└─/tmp        tmpfs       tmpfs  rw,nosuid,nodev,size=2097152k
```

## Problemas comuns

```bash
umount: /mnt/usb: target is busy.
sudo lsof +f -- /mnt/usb           # quem usa?   (veja [[lsof]])
sudo fuser -vmk /mnt/usb           # mostrar/encerrar (cuidado)
cd /                               # saia do diretório montado
sudo umount -l /mnt/usb            # desmonta "preguiçosamente"

sudo mount /dev/sdb1 /mnt          # wrong fs type / bad superblock
sudo fsck -n /dev/sdb1             # verifica sem alterar (desmontado)
dmesg | tail                       # mensagens do kernel
```

## Namespaces de montagem

Cada [[Namespaces do Linux - SO|namespace]] de montagem tem sua visão: contêineres montam seu próprio `/`; `unshare -m` permite experimentar. `mount --make-private/shared` controla a propagação.

## Pontos-chave

- `findmnt` para ver, `mount`/`umount` para operar, `fstab` para persistir.
- Use UUID, `nofail`, e `noexec,nosuid,nodev` onde cabe.
- "Target is busy" → `lsof`/`fuser`.

## Veja também

[[df e du]] · [[VFS - Virtual File System]] · [[MOC - Ferramentas Nativas do Linux]]
