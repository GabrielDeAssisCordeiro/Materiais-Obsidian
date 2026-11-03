---
tags: [configuracoes, editor]
aliases: [Settings Editor, Opções do editor]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Modos de edição e leitura]]", "[[Sintaxe básica]]", "[[Properties]]"]
---

# Configurações do Editor

| Opção | O que faz | Recomendação |
|---|---|---|
| **Default editing mode** | Live Preview ou Source ([[Modos de edição e leitura]]) | Live Preview para a maioria |
| **Default view for new tabs** | Editar ou ler ao abrir | Editar, a menos que goste de ler |
| **Properties in document** | Mostrar properties como campos, texto ou ocultar ([[Properties]]) | Visíveis; texto se editar YAML muito |
| **Fold heading / Fold indent** | Recolher seções e listas | Ligar em notas longas |
| **Show line numbers** | Numeração de linhas | Útil para código |
| **Indentation guides** | Linhas guia em listas | Ligar |
| **Readable line length** | Limita largura do texto | Ligar para leitura; desligar para tabelas largas |
| **Strict line breaks** | Quebra de linha simples vira quebra real | Desligado por padrão; ligar se vem de outros apps |
| **Spellcheck** | Corretor ortográfico | Ligar e escolher idioma |
| **Auto pair brackets / Markdown syntax** | Fecha `()` `[]` `**` sozinho | Ligar |
| **Smart lists** | Continua listas ao dar Enter | Ligar |
| **Indent using tabs** | Tab vs espaços | Padrão; seguir o que usa em listas |
| **Auto convert HTML** | Converte HTML colado em Markdown | Ligar |
| **Vim key bindings** | Atalhos do Vim | Só para quem usa Vim |

> [!warning] Quebras de linha
> Com *Strict line breaks* desligado, duas linhas seguidas viram um parágrafo na leitura. Use linha em branco para separar.

> [!question] Verificar na documentação oficial
> Os nomes e a disponibilidade de opções mudam. Confirme a lista atual na seção *Editor*.

## Veja também
- [[Configurações de Arquivos e links]]
- [[Sintaxe básica]]

## Exercício
Ative *Readable line length* e compare a leitura de uma tabela larga com ele ligado e desligado.
