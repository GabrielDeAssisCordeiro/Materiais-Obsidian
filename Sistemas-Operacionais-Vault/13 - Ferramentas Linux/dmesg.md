---
titulo: "dmesg"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[journalctl]]"
  - "[[Drivers de Dispositivo]]"
  - "[[Processo de Boot]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# dmesg

## Finalidade

Exibe o **buffer de mensagens do kernel** (*kernel ring buffer*): boot, detecção de hardware, drivers, erros de disco, OOM killer, USB, rede, segurança (SELinux/AppArmor), módulos.

## Sintaxe

```bash
dmesg                     # tudo (pode exigir root: kernel.dmesg_restrict)
dmesg -T                  # carimbos de data legíveis (aproximados)
dmesg -H                  # paginado e colorido (legível)
dmesg -w                  # acompanha (follow)
dmesg -l err,warn         # filtra por nível
dmesg -f kern,daemon      # por facilidade
dmesg --since "10 min ago"
dmesg -c                  # lê e limpa o buffer (root)
sudo journalctl -k        # mesmas mensagens via systemd, com histórico entre boots
```

Níveis: `emerg`, `alert`, `crit`, `err`, `warn`, `notice`, `info`, `debug`.

## Saída comentada

```text
[    0.000000] Linux version 6.8.0 ...                       # primeira linha: versão do kernel
[    0.412311] smpboot: CPU0: Intel(R) Core(TM) i7 ...        # CPU detectada
[    1.204117] nvme nvme0: pci function 0000:01:00.0          # disco NVMe
[    2.881002] EXT4-fs (nvme0n1p2): mounted filesystem ...    # raiz montada
[ 4812.330990] usb 1-2: new high-speed USB device number 5    # pen drive conectado
[ 7720.005114] Out of memory: Killed process 2210 (java) total-vm:8123456kB
[ 7720.005120] oom_reaper: reaped process 2210 (java)         # OOM killer encerrou o Java
[ 9001.771220] blk_update_request: I/O error, dev sda, sector 123456   # erro de disco!
[ 9002.100331] audit: type=1400 avc: denied { read } ...      # negativa do SELinux
```

## Receitas de diagnóstico

```bash
sudo dmesg -T -l err,crit,alert,emerg          # só problemas
sudo dmesg | grep -iE "oom|killed process"     # memória
sudo dmesg | grep -iE "I/O error|ata[0-9]|nvme|reset"   # disco
sudo dmesg | grep -iE "usb|firmware|iommu"     # hardware e firmware
sudo dmesg | grep -iE "segfault|general protection"     # falhas de aplicativos
sudo dmesg | grep -iE "link (up|down)|eth|wlan"  # rede
sudo dmesg -w                                   # veja ao plugar um dispositivo
```

> [!warning] Buffer circular
> O *ring buffer* tem tamanho fixo (parâmetro `log_buf_len`); mensagens antigas são sobrescritas. Para histórico persistente use `journalctl -k -b -1` (boot anterior) ou persistência do journal.

## Pontos-chave

- Primeira parada para erros de **hardware, drivers, OOM e disco**.
- `dmesg -T -l err,warn` e `dmesg -w` são os mais úteis.
- Use [[journalctl]] para histórico entre boots.

## Veja também

[[journalctl]] · [[Drivers de Dispositivo]] · [[MOC - Ferramentas Nativas do Linux]]
