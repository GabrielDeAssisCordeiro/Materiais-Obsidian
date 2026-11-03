---
titulo: "Cheat Sheet - Comandos"
tags:
  - sistemas-operacionais
  - cheatsheet
tipo: cheatsheet
nivel: intermediario
relacionados:
  - "[[Cheat Sheet - Conceitos]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
  - "[[MOC - Ferramentas Nativas do macOS]]"
---

# Cheat Sheet - Comandos

## Equivalências

| Tarefa | Linux | Windows (PowerShell/CMD) | macOS |
|---|---|---|---|
| Listar processos | `ps aux` | `Get-Process` / `tasklist` | `ps aux` |
| Monitor interativo | `top`, `htop` | Gerenciador de Tarefas | `top -o cpu`, Monitor de Atividade |
| Encerrar processo | `kill -15 PID`, `kill -9` | `Stop-Process -Id` / `taskkill /F` | `kill`, `killall` |
| Memória | `free -h`, `vmstat` | `Get-Counter '\Memory\*'` | `vm_stat`, `memory_pressure` |
| Disco (espaço) | `df -h`, `du -sh` | `Get-Volume` / `dir` | `df -h`, `du -sh` |
| Discos/volumes | `lsblk`, `mount` | `Get-Disk`, `diskpart` | `diskutil list` |
| E/S de disco | `iostat -x 1` | Perfmon / Resource Monitor | `iostat`, `fs_usage` |
| Arquivos abertos | `lsof` | `handle.exe` (Sysinternals) | `lsof` |
| Rede (conexões) | `ss -tulpn` | `netstat -ano` / `Get-NetTCPConnection` | `netstat -an`, `lsof -i` |
| IP/interfaces | `ip addr` | `ipconfig /all` | `ifconfig`, `networksetup` |
| Logs | `journalctl -u srv -f` | Event Viewer / `Get-WinEvent` | `log stream`, Console |
| Kernel/boot | `dmesg` | Event Viewer (System) | `dmesg`, `log show` |
| Serviços | `systemctl status X` | `Get-Service`, `sc` | `launchctl list` |
| Agendar | `crontab -e` | `schtasks`, Task Scheduler | `launchd` (plist) |
| Rastrear syscalls | `strace -p PID` | Process Monitor | `dtruss`, `fs_usage` |
| Buscar texto | `grep -rn` | `Select-String` / `findstr` | `grep` (BSD) |
| Permissões | `chmod`, `chown` | `icacls` | `chmod`, `chown`, `chmod +a` |
| Versão do SO | `uname -a`, `cat /etc/os-release` | `winver`, `systeminfo` | `sw_vers`, `uname -a` |
| Reparar sistema | `fsck`, gerenciador de pacotes | `sfc /scannow`, `DISM` | `diskutil verifyVolume`, Recovery |
| Registro/config | `/etc`, `sysctl` | `regedit`, `reg` | `defaults`, plist |

## Linux essencial

```bash
ps -eo pid,ppid,stat,pcpu,pmem,cmd --sort=-pcpu | head      # top CPU
free -h; vmstat 1 5; iostat -xz 1 3                         # memória e disco
ss -ltnp                                                    # portas em escuta
lsof -i :8080                                               # quem usa a porta
journalctl -p err -b                                        # erros desde o boot
systemctl --failed; systemctl status nginx
strace -f -e trace=openat -p 1234                           # arquivos abertos
du -h --max-depth=1 / 2>/dev/null | sort -h | tail
find / -xdev -size +500M 2>/dev/null
chmod 640 arq; chown user:grupo arq; stat arq
```

## Windows essencial

```powershell
Get-Process | Sort CPU -Descending | Select -First 5
Get-NetTCPConnection -State Listen | Select LocalPort, OwningProcess
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2} -MaxEvents 10
Get-Service | Where Status -eq Stopped
sfc /scannow ; DISM /Online /Cleanup-Image /RestoreHealth
```

## macOS essencial

```bash
sudo fs_usage -w -f filesys Safari
log show --last 30m --predicate 'messageType == fault'
launchctl list | grep -v com.apple
diskutil list; diskutil apfs list
vm_stat; memory_pressure
```

## Pontos-chave

- Os conceitos se repetem entre SOs; o que muda é o nome e a sintaxe.
- Detalhes em [[MOC - Ferramentas Nativas do Linux]], [[MOC - Ferramentas Nativas do Windows]] e [[MOC - Ferramentas Nativas do macOS]].

## Veja também

[[Cheat Sheet - Conceitos]] · [[MOC - Extras]]
