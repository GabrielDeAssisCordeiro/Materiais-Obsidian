---
titulo: "df e du"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[mount]]"
  - "[[Inodes]]"
  - "[[lsof]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# df e du

## Finalidade

- **`df`** (*disk free*): espaço **por sistema de arquivos montado**.
- **`du`** (*disk usage*): espaço **por arquivos/diretórios**.

## Sintaxe

```bash
df -h                       # legível (G, M)
df -hT                      # com tipo de FS
df -i                       # inodes
df -h /home                 # FS que contém o caminho
df -x tmpfs -x devtmpfs -h  # exclui pseudo-FS
df --output=source,fstype,size,used,avail,pcent,target -h

du -sh pasta                # total da pasta
du -h --max-depth=1 /var | sort -h      # maiores subpastas
du -ah /var/log | sort -rh | head -10   # maiores arquivos/pastas
du -sh * | sort -h                      # no diretório atual
du -x -h --max-depth=1 /                # não cruza outros FS
du --apparent-size -sh arquivo          # tamanho aparente x alocado
ncdu /var                               # navegador interativo (instalar)
```

## Saída comentada

```text
$ df -hT -x tmpfs -x devtmpfs
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda2      ext4  100G   82G   13G  87% /
/dev/sda1      vfat  512M  6.1M  506M   2% /boot/efi
/dev/sdb1      xfs   2.0T  1.1T  0.9T  55% /dados
# "Avail" < Size-Used porque ~5% é reservado ao root em ext4 (tune2fs -m)
```

## Investigação clássica: disco cheio

```mermaid
flowchart TD
    A[df -h: qual FS está cheio?] --> B[df -i: acabaram os inodes?]
    B -->|Sim| C[Muitos arquivos pequenos: find -xdev | cut | sort | uniq -c]
    B -->|Não| D[du -xh --max-depth=1 / | sort -h]
    D --> E{du soma bem menos que df?}
    E -->|Sim| F[lsof +L1: arquivos apagados ainda abertos; snapshots; espaço reservado]
    E -->|Não| G[Limpar maiores diretórios: logs, caches, imagens Docker]
```

```bash
sudo du -xh --max-depth=1 / 2>/dev/null | sort -h | tail
sudo du -xah /var 2>/dev/null | sort -rh | head -15
sudo journalctl --disk-usage; sudo journalctl --vacuum-size=500M
docker system df; docker system prune -a    # contêineres, imagens, volumes
sudo apt clean; sudo dnf clean all
find /var/log -type f -size +100M -exec ls -lh {} \;
find / -xdev -type f -size +1G 2>/dev/null
```

## Por que `df` e `du` discordam?

| Causa | Como identificar |
|---|---|
| Arquivo **apagado mas aberto** | `lsof +L1` ([[lsof]]) |
| **Snapshots**/CoW (Btrfs, ZFS), subvolumes | `btrfs filesystem usage`, `zfs list -t snapshot` |
| Espaço **reservado** (ext4 5%) | `tune2fs -l /dev/sdX \| grep -i reserved` |
| Outro FS montado **por cima** de um diretório com arquivos | Desmontar e conferir (`mount --bind / /mnt/x`) |
| Arquivos esparsos / blocos alocados x tamanho | `du --apparent-size` x `du` |
| Metadados e journal | Inerente ao FS |

> [!tip] Btrfs/ZFS
> `df` engana nesses FS; use `btrfs filesystem usage /` ou `zfs list`/`zpool list`.

## Pontos-chave

- `df` olha o FS; `du` soma arquivos. Diferenças têm explicação.
- `df -i` revela esgotamento de [[Inodes]].
- `du -xh --max-depth=1 | sort -h` é a receita para achar o que ocupa espaço.

## Veja também

[[mount]] · [[lsof]] · [[Inodes]] · [[MOC - Ferramentas Nativas do Linux]]
