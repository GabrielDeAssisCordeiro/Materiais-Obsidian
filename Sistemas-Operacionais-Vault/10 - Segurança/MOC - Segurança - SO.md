---
titulo: "MOC - Segurança - SO"
tags:
  - sistemas-operacionais
  - moc
  - seguranca
tipo: moc
nivel: intermediario
relacionados:
  - "[[Autenticação]]"
  - "[[Controle de Acesso]]"
  - "[[ASLR - Address Space Layout Randomization]]"
  - "[[DEP, NX e Mitigações de Exploração]]"
  - "[[Sandboxing]]"
  - "[[SELinux e AppArmor]]"
---

# MOC - Segurança - SO

> [!info] Escopo
> Como o SO protege recursos e usuários: identificar quem é quem, decidir o que cada um pode fazer e conter o dano de falhas.

## Trilha

1. [[Autenticação]]: provar identidade (senhas, hashes, MFA, PAM)
2. [[Controle de Acesso]]: DAC, MAC, RBAC, capabilities
3. [[ASLR - Address Space Layout Randomization]]: aleatorização do espaço de endereços
4. [[DEP, NX e Mitigações de Exploração]]: memória não executável, canários, CFI
5. [[Sandboxing]]: isolamento de processos (seccomp, app sandbox)
6. [[SELinux e AppArmor]]: controle de acesso obrigatório no Linux

## Princípios

| Princípio | Significado |
|---|---|
| Menor privilégio | Cada entidade recebe só o necessário |
| Defesa em profundidade | Várias camadas independentes |
| Separação de privilégios | Dividir tarefas sensíveis em componentes isolados |
| Falha segura | Em dúvida, negar |
| Mediação completa | Toda requisição é verificada |

## Relacionados

[[Permissões de Arquivos]] · [[Modos de Operação da CPU]] · [[Memória Virtual]] · [[Containers]] · [[BIOS e UEFI]]
