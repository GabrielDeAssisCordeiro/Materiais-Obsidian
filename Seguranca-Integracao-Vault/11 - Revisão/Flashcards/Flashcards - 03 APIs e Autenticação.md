---
titulo: "Flashcards - 03 APIs e Autenticação"
aliases: ["Flashcards 03"]
tags:
  - integracao-seguranca
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[OAuth 2.0 e OIDC]]"
  - "[[JWT]]"
  - "[[mTLS]]"
---

# Flashcards - 03 APIs e Autenticação

## Resumo

Cartões de revisão do módulo **APIs e Autenticação**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[OAuth 2.0 e OIDC]], [[JWT]], [[mTLS]], [[Escopos e Menor Privilégio]].

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

Qual a diferença entre OAuth 2.0 e OIDC?::OAuth 2.0 é autorização delegada; OIDC adiciona autenticação (ID token) sobre OAuth 2.0.
Qual fluxo OAuth usar entre máquinas?::Client credentials.
Para que serve o PKCE?::Proteger o fluxo authorization code contra interceptação do código.
O que validar em um JWT?::Assinatura, algoritmo esperado, exp, iss, aud e escopos.
O payload de um JWT assinado é secreto?::Não; é apenas codificado em Base64URL, não criptografado.
O que é mTLS?::TLS em que o cliente também apresenta certificado e o servidor o valida.
Por que fixar o algoritmo ao validar um JWT?::Para impedir que o token escolha o alg (como none) e burle a validação.
O que é BOLA?::Falha de autorização por objeto: acessar recurso de outro usuário apenas trocando o identificador.
Onde enviar uma API key?::No cabeçalho (Authorization ou X-API-Key), nunca na URL.
Por que preferir paginação por cursor a offset?::O cursor é estável e eficiente em dados que mudam; offset pode perder ou duplicar itens.
Para que serve o OpenAPI?::Descrever APIs REST como contrato, gerando documentação, clientes, validação e testes de contrato.
Quais riscos são típicos do GraphQL?::Consultas profundas ou caras, introspecção aberta em produção e falta de autorização por campo.
Como o gRPC define seu contrato?::Em arquivos .proto (protobuf), sobre HTTP/2, com suporte a streaming.
O que é um escopo OAuth?::Permissão nomeada presente no token que limita o que o cliente pode fazer.

## Veja também

- [[OAuth 2.0 e OIDC]]
- [[JWT]]
- [[mTLS]]
- [[Escopos e Menor Privilégio]]
- [[MOC - Revisão - Integração]]
- [[Como usar este vault - Integração]]

#flashcards #seguranca/revisao/flashcards
