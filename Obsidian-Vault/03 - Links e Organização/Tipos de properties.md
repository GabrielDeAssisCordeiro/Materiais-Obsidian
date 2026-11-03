---
tags: [properties, tipos]
aliases: [Property types, Tipos de propriedades]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Properties]]", "[[Sintaxe YAML do frontmatter]]", "[[Bases]]"]
---

# Tipos de properties

| Tipo | Exemplo YAML | Uso |
|---|---|---|
| Texto | `autor: Maria` | valores livres |
| Lista | `aliases: [a, b]` | múltiplos valores |
| Número | `paginas: 320` | cálculos em [[Bases]] |
| Caixa de seleção | `lido: true` | sim/não |
| Data | `criado: 2026-10-23` | datas |
| Data e hora | `inicio: 2026-10-23T14:30` | agendamento |
| Tags | `tags: [estudo]` | tipo especial para tags |

## Regras
- O tipo é associado ao **nome** da propriedade em todo o vault (guardado em `.obsidian/types.json`, ver [[Pasta .obsidian]]).
- Mudar o tipo de `prazo` muda para todas as notas.
- Valores incompatíveis aparecem com aviso.

> [!question] Verificar na documentação oficial
> Confirme se há tipos adicionais na versão atual e como links em properties (`"[[Nota]]"`) são tratados.

> [!example] Link em property
> ```yaml
> relacionados: ["[[Vault]]", "[[Interface]]"]
> ```
> Links em properties devem estar entre aspas.

## Veja também
- [[Properties]]
- [[Nomenclatura de propriedades]]

## Exercício
Crie propriedades de cada tipo em uma nota de teste e observe como a interface muda.
