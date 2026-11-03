---
tags: [properties]
aliases: [YAML, Frontmatter YAML]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Properties]]", "[[Tipos de properties]]", "[[Solução de problemas]]"]
---

# Sintaxe YAML do frontmatter

O frontmatter fica **no início do arquivo**, entre duas linhas `---`.

```yaml
---
titulo: Exemplo
tags: [a, b]
aliases:
  - Nome 1
  - Nome 2
paginas: 120
lido: false
criado: 2026-10-23
relacionados: ["[[Nota X]]"]
---
```

## Regras
- Formato `chave: valor` (espaço após os dois-pontos).
- Listas: `[a, b]` ou itens com `-`.
- Textos com `:`, `#` ou começando com `[`, `{`, `"` devem ir entre aspas.
- Indentação com espaços, nunca tabs.
- Comece a nota com `---` na **primeira linha**.

> [!warning] Erros comuns
> Dois-pontos sem aspas (`titulo: Parte 1: Início`) quebram a leitura. Use `titulo: "Parte 1: Início"`.

## Veja também
- [[Propriedades padrão]]
- [[Erros comuns]]

## Exercício
Escreva um frontmatter com texto com dois-pontos, lista e data. Confirme que o painel de properties lê tudo.
