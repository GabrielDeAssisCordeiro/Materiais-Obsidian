---
tags: [markdown]
aliases: [Tabelas Markdown]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Advanced Tables]]", "[[Sintaxe básica]]", "[[Bases]]"]
---

# Tabelas

```markdown
| Nome  | Tipo   | Nível      |
|-------|--------|------------|
| Vault | pasta  | iniciante  |
| Canvas| quadro | intermediario |
```

## Alinhamento
```markdown
| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| a        |   b    |       c |
```

## Dicas
- Pipes dentro de células precisam de escape: `\|`. Isso importa em links com alias: `[[Nota\|alias]]`.
- Para tabelas maiores, o plugin [[Advanced Tables]] formata e navega com `Tab`.
- Para dados vindos de notas, prefira [[Bases]] ou [[Consultas Dataview]] em vez de manter tabelas na mão.
- Quebras de linha dentro de célula: use `<br>`.

> [!warning] Sem células mescladas
> Markdown puro não suporta mesclar células nem listas dentro delas.

## Veja também
- [[Sintaxe estendida]]
- [[Cheat sheet Markdown]]

## Exercício
Crie uma tabela de três plugins que você quer testar, com coluna de alinhamento à direita para prioridade.
