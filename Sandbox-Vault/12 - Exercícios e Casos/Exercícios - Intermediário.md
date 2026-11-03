---
tags:
  - exercicios
aliases: []
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Namespaces do Linux]]"
  - "[[Cgroups]]"
  - "[[Seccomp]]"
---
# Exercícios - Intermediário

1. **Namespaces:** use `unshare` para criar um PID namespace e explique por que `$$` vale 1 ([[Namespaces do Linux]]).
2. **Limites:** execute um container com `--memory 64m` e provoque OOM de forma controlada ([[Cgroups]]).
3. **Capabilities:** compare `CapEff` com e sem `--cap-drop=ALL` ([[Capabilities do Linux]]).
4. **Seccomp:** gere a lista de syscalls de um programa com `strace -c` e proponha um perfil mínimo ([[Seccomp]]).
5. **Rede:** monte uma VM em rede interna e comprove o isolamento com o teste da nota [[Vazamento por Rede e DNS]].
6. **Compose:** crie o ambiente de [[Criar Sandbox de Desenvolvimento Web e APIs]] com rede `internal`.
7. **Auditoria:** use [[Checklist de Auditoria de Sandbox]] em um container seu.

## Veja também

- [[Exercícios - Avançado]]
- [[Exercícios - Iniciante]]
- [[MOC - Exercícios e Casos]]
