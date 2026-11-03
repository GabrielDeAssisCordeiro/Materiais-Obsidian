---
tags:
  - boas-praticas
  - arquitetura
aliases:
  - "Checklist de auditoria"
tipo: checklist
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Checklist de Criação de Sandbox]]"
  - "[[Fuga de Sandbox]]"
---
# Checklist de Auditoria de Sandbox

- [ ] Sem `--privileged`, `docker.sock`, `--pid=host`, `--network=host`
- [ ] Capabilities mínimas (`docker inspect`)
- [ ] Perfil seccomp/AppArmor/SELinux ativo (não `unconfined`)
- [ ] Imagens atualizadas; vulnerabilidades altas tratadas
- [ ] Hipervisor/kernel/runtime em versões com correções
- [ ] Rede testada (ping, DNS, IPv6) de dentro e de fora
- [ ] Nenhum segredo em variáveis de ambiente, imagens ou logs
- [ ] Limites de recursos efetivos (teste de estresse)
- [ ] Logs íntegros e fora da sandbox
- [ ] Ambientes antigos/órfãos removidos
- [ ] Revisão de acessos e permissões

```bash
docker ps -q | xargs -r docker inspect --format '{{.Name}} priv={{.HostConfig.Privileged}} net={{.HostConfig.NetworkMode}} ro={{.HostConfig.ReadonlyRootfs}} caps={{.HostConfig.CapAdd}}'
```

## Veja também

- [[Checklist de Criação de Sandbox]]
- [[Modelo de Ameaças]]
- [[Erros Comuns em Sandboxes]]
- [[MOC - Boas Práticas]]
