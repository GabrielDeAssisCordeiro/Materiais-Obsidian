---
tags: [funcoes, diario]
aliases: [Nota do dia]
tipo: funcao
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Core - Notas diárias]]", "[[Templates]]", "[[Periodic Notes]]"]
---

# Notas diárias

Cria uma nota por dia com um clique ([[Core - Notas diárias]]).

## Configurar
- **Formato de data:** padrão `YYYY-MM-DD`.
- **Pasta:** ex. `Diário/`.
- **Template:** arquivo em `Templates/` ([[Templates]]).
- **Abrir ao iniciar:** opcional.

## Template exemplo
```markdown
---
tags: [diario]
criado: {{date:YYYY-MM-DD}}
---
# {{date:dddd, DD [de] MMMM}}

## Prioridades
- [ ]

## Anotações

## Revisão
```

## Uso
- Comando *Open today's daily note*.
- Capture ideias soltas no dia e processe depois ([[Captura, processamento, conexão e saída]]).
- Para notas semanais/mensais: [[Periodic Notes]] e [[Calendar]].

> [!tip] Link para o dia
> Escreva `[[2026-10-23]]` para ligar assuntos a uma data.

## Veja também
- [[Fluxo de diário]]
- [[Core - Templates]]

## Exercício
Configure a nota diária com template e crie as notas de três dias seguidos.
