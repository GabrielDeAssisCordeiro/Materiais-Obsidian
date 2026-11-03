---
tags:
  - referencia
aliases:
  - "Cheat sheet Linux"
tipo: cheatsheet
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Namespaces do Linux]]"
  - "[[Capabilities do Linux]]"
  - "[[Cgroups]]"
---
# Cheat Sheet - Isolamento no Linux

```bash
# Namespaces
unshare --user --map-root-user --pid --fork --mount-proc bash
lsns                                   # listar namespaces
ls -l /proc/$$/ns                      # namespaces do processo atual

# Capabilities
capsh --print
grep Cap /proc/self/status
getpcaps $$

# cgroups v2
stat -fc %T /sys/fs/cgroup             # cgroup2fs => v2
cat /proc/self/cgroup
systemd-run --user --scope -p MemoryMax=200M -p TasksMax=64 COMANDO

# Bubblewrap
bwrap --ro-bind /usr /usr --symlink usr/bin /bin --symlink usr/lib /lib --symlink usr/lib64 /lib64 \
      --proc /proc --dev /dev --tmpfs /tmp --unshare-all --die-with-parent COMANDO

# Firejail
firejail --private --net=none --caps.drop=all --seccomp COMANDO
firejail --list

# LSM
sudo aa-status ; getenforce

# Syscalls usadas por um programa
strace -c -f COMANDO
```

## Veja também

- [[Glossário#Sandboxes e isolamento]]
- [[Cheat Sheet - Docker e Podman]]
- [[Cheat Sheet - VMs]]
- [[MOC - Referência - Sandbox]]
