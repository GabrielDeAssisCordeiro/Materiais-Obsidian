---
tags: [plugins-comunidade, projetos]
aliases: [Kanban plugin, Quadros kanban]
tipo: plugin
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Tasks]]", "[[Fluxo de gestão de projetos]]", "[[Bases]]"]
---

# Kanban

Cria quadros **Kanban** a partir de uma nota Markdown.

## Uso
1. Comando *Create new board*.
2. Adicione listas (colunas) e cartões.
3. Arraste cartões entre listas.

## Estrutura do arquivo
```markdown
---
kanban-plugin: board
---

## A fazer
- [ ] Ler capítulo 1

## Fazendo

## Feito
```
Cartões podem conter links `[[ ]]` e datas.

> [!tip] Arquivos legíveis
> O quadro continua sendo Markdown e funciona mesmo sem o plugin.

> [!question] Verificar na documentação oficial
> Confirme o estado de manutenção e opções de datas e arquivamento.

## Veja também
- [[Tasks]]
- [[Fluxo de gestão de projetos]]

## Exercício
Monte um quadro com 3 colunas para um projeto pessoal.
