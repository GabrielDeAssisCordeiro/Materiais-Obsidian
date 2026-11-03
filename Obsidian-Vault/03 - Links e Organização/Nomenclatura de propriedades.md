---
tags: [properties, boas-praticas]
aliases: [Nomes de propriedades, Convenções de properties]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Properties]]", "[[Tipos de properties]]", "[[Bases]]"]
---

# Nomenclatura de propriedades

Nomes consistentes tornam [[Bases]] e [[Consultas Dataview]] confiáveis.

## Boas práticas
- Minúsculas, sem acento e sem espaço: `data_inicio` ou `data-inicio`.
- Escolha **um** padrão e mantenha.
- Nome no singular para valor único (`status`), plural para lista (`autores`).
- Evite sinônimos (`tipo` × `categoria`).
- Reserve nomes de arquivo como `file.*` para o sistema (em Bases).
- Valores padronizados: `status: ativo | pausado | concluido`.

## Exemplo de esquema
| Propriedade | Tipo | Valores |
|---|---|---|
| `tipo` | texto | conceito, guia, plugin... |
| `nivel` | texto | iniciante, intermediario, avancado |
| `criado` | data | AAAA-MM-DD |
| `relacionados` | lista | links entre aspas |

> [!tip] Template
> Coloque o esquema num template ([[Templates]]) para não esquecer campos.

> [!warning] Acentos
> Nomes com acento funcionam, mas dificultam digitar em consultas.

## Veja também
- [[Propriedades padrão]]
- [[Pastas, tags ou links]]

## Exercício
Defina um esquema com 5 propriedades para seu projeto principal e aplique-o em um template.
