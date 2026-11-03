---
titulo: "Questões - APIs e Desenvolvimento"
aliases: ["APIs e Desenvolvimento de Ferramentas"]
tags:
  - integracao-seguranca
  - revisao
  - questoes
  - quiz
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[OAuth 2.0 e OIDC]]"
  - "[[JWT]]"
  - "[[mTLS]]"
---

# Questões - APIs e Desenvolvimento

## Resumo

11 questões de múltipla escolha sobre **APIs e Desenvolvimento de Ferramentas**, com gabarito comentado (clique no callout para expandir).

## Conceitos-chave

- Cada questão tem quatro alternativas e um comentário que explica o raciocínio.
- Conteúdo-fonte: [[OAuth 2.0 e OIDC]], [[JWT]], [[mTLS]], [[CLI de Segurança]], [[Empacotamento e Containers]].

## Como funciona

Responda sem consultar as notas, depois abra o gabarito. Para cada erro, releia a nota de origem e crie um flashcard.

## Exemplo prático

> [!question] Estratégia
> Elimine primeiro as alternativas claramente incorretas; depois justifique a escolhida em uma frase.

## Boas práticas

- Faça as questões em blocos curtos e espaçados.
- Anote o motivo de cada erro.

## Erros comuns

- Marcar por intuição sem justificar.
- Ler o gabarito antes de tentar.

## Referências para aprofundar

Notas de origem listadas em Conceitos-chave.

## Questões

### Questão 1

Qual fluxo OAuth 2.0 é indicado para um conector que roda sem usuário interativo?

- A) Implicit
- B) Password
- C) Client credentials
- D) Device code

> [!success]- Gabarito: C
> Client credentials é o fluxo máquina a máquina. Implicit e password são desaconselhados.

### Questão 2

Qual prática de validação de JWT é INCORRETA?

- A) Verificar exp, iss e aud
- B) Fixar o algoritmo esperado
- C) Aceitar o algoritmo indicado no cabeçalho do token
- D) Usar chave pública do JWKS

> [!success]- Gabarito: C
> Aceitar o alg do token abre brecha (como alg none). O algoritmo esperado deve ser fixado na validação.

### Questão 3

O que diferencia mTLS de TLS comum?

- A) Usa HTTP/3
- B) O cliente também apresenta certificado
- C) Não usa certificados
- D) Dispensa autoridade certificadora

> [!success]- Gabarito: B
> No mTLS ambos se autenticam com certificados.

### Questão 4

Acessar o recurso de outro usuário alterando o ID na URL, mesmo autenticado, é exemplo de:

- A) BOLA
- B) XXE
- C) CSRF apenas
- D) Rate limiting

> [!success]- Gabarito: A
> BOLA (Broken Object Level Authorization): falta autorização por objeto.

### Questão 5

Onde deve trafegar uma API key?

- A) Na query string
- B) Em um cabeçalho HTTP
- C) No caminho da URL
- D) No título do ticket

> [!success]- Gabarito: B
> Cabeçalhos evitam que a chave apareça em logs de URL e históricos.

### Questão 6

Qual paginação é mais robusta para coleções que mudam durante a leitura?

- A) Offset/limit
- B) Cursor (keyset)
- C) Sem paginação
- D) Aleatória

> [!success]- Gabarito: B
> Cursor é estável e eficiente; offset pode perder ou duplicar itens.

### Questão 7

Em uma CLI usada como gate de pipeline, o exit code 1 deve indicar:

- A) Erro de uso
- B) Achados acima do limiar
- C) Sucesso
- D) Timeout

> [!success]- Gabarito: B
> Convenção sugerida: 0 sucesso, 1 achados acima do limiar, 2 erro de uso ou execução.

### Questão 8

Qual biblioteca ajuda a processar XML de fontes externas com segurança em Python?

- A) xml.etree padrão sem cuidados
- B) defusedxml
- C) pickle
- D) eval

> [!success]- Gabarito: B
> defusedxml bloqueia XXE e ataques de expansão de entidades.

### Questão 9

Qual medida reduz o risco de um sistema de plugins?

- A) Carregar qualquer módulo de um diretório gravável
- B) Allowlist de plugins e isolamento
- C) Executar como root
- D) Desativar logs

> [!success]- Gabarito: B
> Plugin é código executado com seus privilégios; só carregue os autorizados.

### Questão 10

Qual prática de Dockerfile é recomendada?

- A) Imagem única com compiladores e executar como root
- B) Multi-stage, imagem mínima e usuário não root
- C) Colocar segredos em ENV
- D) Usar a tag latest

> [!success]- Gabarito: B
> Multi-stage reduz a superfície; não root e imagens mínimas limitam o impacto.

### Questão 11

Qual dado NÃO deve ser registrado em logs?

- A) Resultado da operação
- B) Correlation ID
- C) Cabeçalho Authorization com token
- D) Nome do serviço

> [!success]- Gabarito: C
> Tokens em logs são vazamento de credencial; aplique redação.

## Veja também

- [[OAuth 2.0 e OIDC]]
- [[JWT]]
- [[mTLS]]
- [[CLI de Segurança]]
- [[Empacotamento e Containers]]
- [[MOC - Revisão - Integração]]

#seguranca/revisao/questoes #quiz
