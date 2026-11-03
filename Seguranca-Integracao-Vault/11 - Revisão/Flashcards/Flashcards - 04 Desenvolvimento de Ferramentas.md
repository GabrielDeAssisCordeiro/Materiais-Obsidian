---
titulo: "Flashcards - 04 Desenvolvimento de Ferramentas"
aliases: ["Flashcards 04"]
tags:
  - integracao-seguranca
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Escolha de Linguagem - Python e Go]]"
  - "[[CLI de Segurança]]"
  - "[[Parsing de Formatos - SARIF JSON e XML]]"
---

# Flashcards - 04 Desenvolvimento de Ferramentas

## Resumo

Cartões de revisão do módulo **Desenvolvimento de Ferramentas**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Escolha de Linguagem - Python e Go]], [[CLI de Segurança]], [[Parsing de Formatos - SARIF JSON e XML]], [[Testes - Unitários Integração e Contratos]].

## Como funciona

Instale o plugin Spaced Repetition e use *Review flashcards*. O algoritmo agenda a próxima revisão conforme sua avaliação (fácil, bom, difícil).

## Exemplo prático

Responda mentalmente antes de virar o cartão. Se errar, releia a nota de origem e reformule o cartão com suas palavras.

## Boas práticas

- Revise um pouco todos os dias.
- Crie cartões próprios para pontos que você errou.
- Mantenha respostas curtas.

## Erros comuns

- Decorar sem entender a razão.
- Acumular revisões atrasadas.
- Cartões longos demais.

## Referências para aprofundar

Plugin Spaced Repetition para Obsidian; veja [[Como usar este vault - Integração]].

## Flashcards

#flashcards

Por que definir timeout em clientes HTTP?::Evita chamadas penduradas; em Go o http.DefaultClient não tem timeout.
Qual a convenção de exit codes de uma CLI de gate?::0 sucesso, 1 achados acima do limiar, 2 erro de uso ou execução.
Por que não passar segredos por argumento de CLI?::Eles aparecem na listagem de processos e no histórico do shell.
Qual o risco de shell=True com dados externos?::Injeção de comando; use lista de argumentos.
O que é SARIF?::Formato JSON padrão (OASIS) para resultados de análise estática.
O que é XXE e como evitar?::Entidades externas em XML podem ler arquivos ou fazer requisições; use defusedxml.
O que são entry points em Python?::Mecanismo de pacotes para descobrir plugins; combine com uma allowlist.
Como é a pirâmide de testes?::Muitos testes unitários, alguns de integração e poucos de ponta a ponta ou contrato.
Qual a vantagem do Dockerfile multi-stage?::Compila em uma etapa e copia só o resultado para uma imagem final mínima.
Por que redigir segredos em logs?::Para evitar vazar tokens, senhas e dados pessoais.
O que é log forging?::Quebras de linha em dados externos que forjam entradas em logs de texto; JSON mitiga.

## Veja também

- [[Escolha de Linguagem - Python e Go]]
- [[CLI de Segurança]]
- [[Parsing de Formatos - SARIF JSON e XML]]
- [[Testes - Unitários Integração e Contratos]]
- [[MOC - Revisão - Integração]]
- [[Como usar este vault - Integração]]

#flashcards #seguranca/revisao/flashcards
