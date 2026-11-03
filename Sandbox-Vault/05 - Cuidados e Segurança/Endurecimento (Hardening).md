---
tags:
  - seguranca
aliases: []
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do Menor Privilégio]]"
  - "[[Ferramenta - AppArmor e SELinux]]"
  - "[[Criar Sandbox com Docker]]"
---
# Endurecimento (Hardening)

*Hardening* é reduzir a superfície de ataque do host, do hipervisor e da própria sandbox.

## Checklist por camada

**Host**
- Sistema mínimo, sem serviços desnecessários; disco criptografado.
- Firewall com *default deny*.
- LSM ativo (AppArmor/SELinux) — ver [[Ferramenta - AppArmor e SELinux]].

**Container**
- Imagem mínima, fixada por *digest*; usuário não-root.
- `--read-only`, `--cap-drop=ALL`, `no-new-privileges`, seccomp padrão ou mais restrito.
- Sem `--privileged`, sem socket do Docker, sem `--network=host`.

**VM**
- Integrações desativadas; recursos limitados; firmware e hipervisor atualizados.

```bash
# Auditoria rápida de um container em execução
docker inspect <id> --format 'Priv={{.HostConfig.Privileged}} Caps={{.HostConfig.CapAdd}}/{{.HostConfig.CapDrop}} RO={{.HostConfig.ReadonlyRootfs}}'
```

> [!tip] Ferramentas de apoio
> Benchmarks CIS (Docker, Linux) e utilitários como `docker-bench-security` ajudam a auditar configurações.

## Exercício

Execute uma auditoria (`docker inspect` ou docker-bench-security) em um container seu e corrija os achados.

## Veja também

- [[Princípio do Menor Privilégio]]
- [[Ferramenta - AppArmor e SELinux]]
- [[Atualização e Patching]]
- [[Defesa em Profundidade]]
- [[MOC - Cuidados e Segurança]]
