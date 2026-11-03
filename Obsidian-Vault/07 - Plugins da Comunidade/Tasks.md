---
tags: [plugins-comunidade, produtividade]
aliases: [Tasks plugin, Gestão de tarefas]
tipo: plugin
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Calendar]]", "[[Fluxo de gestão de projetos]]", "[[Notas diárias]]"]
---

# Tasks

Gerencia tarefas espalhadas pelo vault, com datas, prioridades, recorrência e consultas.

## Sintaxe de uma tarefa
```markdown
- [ ] Revisar capítulo 3 📅 2026-10-30 ⏫
- [ ] Pagar conta 🔁 every month 📅 2026-11-05
```
| Símbolo | Significado |
|---|---|
| 📅 | data de vencimento |
| ⏳ | agendada |
| 🛫 | início |
| 🔁 | recorrência |
| ⏫ 🔼 🔽 | prioridade alta, média, baixa |
| ✅ | concluída |

## Consulta
````markdown
```tasks
not done
due before tomorrow
sort by due
```
````

## Configuração
- Opções de *global filter* (para só tratar certas listas como tarefas).
- Formato de datas e atalhos para criar/editar tarefa (use a paleta).

> [!tip] Uma consulta de revisão
> Crie uma nota "Hoje" com `not done` e `due today` e abra-a na rotina ([[Notas diárias]]).

> [!question] Verificar na documentação oficial
> Confirme a sintaxe atual de consultas e do formato de datas.

## Veja também
- [[Fluxo de gestão de projetos]]
- [[Kanban]]

## Exercício
Crie 5 tarefas com datas diferentes e uma consulta que mostre só as atrasadas.
