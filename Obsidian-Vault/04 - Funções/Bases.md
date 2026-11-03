---
tags: [funcoes, bases]
aliases: [Obsidian Bases, Arquivos .base, Base]
tipo: funcao
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Core - Bases]]", "[[Bases avançado]]", "[[Properties]]"]
---

# Bases

**Bases** é a camada de banco de dados nativa do Obsidian: transforma notas e suas [[Properties]] em **visões** dinâmicas (tabela, lista, cartões, mapa). Arquivos têm extensão `.base` e usam YAML ([[Core - Bases]]).

## Estrutura do arquivo
Chaves raiz: `filters`, `formulas`, `properties`, `summaries`, `views`.

```yaml
filters:
  and:
    - file.hasTag("estudo")
formulas:
  rotulo: 'tipo + " - " + nivel'
properties:
  nivel:
    displayName: "Nível"
views:
  - type: table
    name: "Tabela"
    order:
      - file.name
      - tipo
      - nivel
```

## Conceitos
- **Filtros** globais ou por view.
- **Fórmulas** calculam valores.
- **Propriedades** de três tipos: da nota, do arquivo (`file.*`) e fórmulas (`formula.*`).
- **Views** podem ser múltiplas sobre os mesmos dados.

## Criar
1. Paleta de comandos → *Bases: Create new base*.
2. Ou insira em uma nota com um bloco de código de linguagem `base` ou com o embed `![[arquivo.base]]` ([[Embeds]]).
3. Edite filtros e colunas pela interface; o YAML é gerado.

> [!warning] Não confunda com Dataview
> Sintaxes como `FROM` e `WHERE` pertencem ao [[Dataview]]. Em Bases, a ordenação é feita por view.

> [!question] Verificar na documentação oficial
> Confirme funções disponíveis e tipos de view na versão atual: help.obsidian.md/bases/syntax.

## Veja também
- [[Bases avançado]]
- [[Dataview]]
- [[Pastas, tags ou links]]

## Exercício
Crie uma Base listando as notas de `tipo: plugin` com colunas nome e nível.
