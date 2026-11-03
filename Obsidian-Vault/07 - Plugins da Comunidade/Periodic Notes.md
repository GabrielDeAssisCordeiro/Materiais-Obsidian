---
tags: [plugins-comunidade, produtividade]
aliases: [Notas periódicas, Notas semanais, Notas mensais]
tipo: plugin
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Calendar]]", "[[Notas diárias]]", "[[Templater]]"]
---

# Periodic Notes

Estende as notas diárias com notas **semanais, mensais, trimestrais e anuais**.

## Configuração
Para cada período, defina:
| Campo | Exemplo |
|---|---|
| Formato | `gggg-[W]ww` para semana |
| Pasta | `Diário/Semanal` |
| Template | `Templates/semanal` |

Funciona junto ao [[Calendar]], que mostra número da semana.

## Uso
- Comandos *Open weekly note*, *Open monthly note*, etc.
- Template semanal com resumo, metas e links para as notas diárias.

> [!example] Template semanal
> ```markdown
> # Semana {{date:gggg-[W]ww}}
> ## Metas
> - [ ]
> ## Revisão
> ```

> [!question] Verificar na documentação oficial
> Confirme os formatos de data e o estado de manutenção do plugin; as notas diárias do core podem coexistir ou ser substituídas, conforme configuração.

## Veja também
- [[Notas diárias]]
- [[Fluxo de diário]]

## Exercício
Configure a nota semanal com template e crie a da semana atual.
