---
tags:
  - estudos-de-caso
  - incidentes
aliases: []
tipo: estudo-de-caso
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Sandbox por Containers]]"
---
# Caso Real - Dirty COW

> [!question] Verificar na documentação oficial
> Resumo educativo, sem detalhes de exploração. Confirme datas, versões e CVEs nos avisos oficiais antes de citar.


**O que foi:** falha de condição de corrida no kernel Linux (CVE-2016-5195, 2016) na lógica de copy-on-write, permitindo a usuários locais escrever em mapeamentos somente leitura e escalar privilégios. Em ambientes de containers, como o kernel é compartilhado, a falha afetava o host.

**Lições**
- **Kernel compartilhado = risco compartilhado.**
- Correções de kernel são parte da segurança de containers.
- Para código hostil, prefira fronteiras com kernel próprio.

**Camadas que ajudam:** [[Sandbox por MicroVMs]], [[Sandbox por Kernel em Espaço de Usuário]], [[Atualização e Patching]].

## Veja também

- [[Fuga de Sandbox]]
- [[Sandbox vs VM vs Container vs Jail vs chroot]]
- [[MOC - Exercícios e Casos]]
