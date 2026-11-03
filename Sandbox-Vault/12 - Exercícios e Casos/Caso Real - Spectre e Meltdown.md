---
tags:
  - estudos-de-caso
  - incidentes
aliases: []
tipo: estudo-de-caso
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Modelo de Ameaças]]"
---
# Caso Real - Spectre e Meltdown

> [!question] Verificar na documentação oficial
> Resumo educativo, sem detalhes de exploração. Confirme datas, versões e CVEs nos avisos oficiais antes de citar.


**O que foi:** em 2018, classes de ataques de canal lateral de execução especulativa mostraram que processos, containers e VMs que compartilham CPU podem inferir dados uns dos outros.

**Lições**
- Isolamento lógico não elimina canais laterais de hardware.
- Mitigações (microcódigo, kernel, hipervisor) exigem atualizações e podem custar desempenho.
- Para dados muito sensíveis, não compartilhe hardware com inquilinos não confiáveis.

**Camadas que ajudam:** [[Atualização e Patching]], [[Modelo de Ameaças]], [[Defesa em Profundidade]].

## Veja também

- [[Fuga de Sandbox]]
- [[Modelo de Ameaças]]
- [[MOC - Exercícios e Casos]]
