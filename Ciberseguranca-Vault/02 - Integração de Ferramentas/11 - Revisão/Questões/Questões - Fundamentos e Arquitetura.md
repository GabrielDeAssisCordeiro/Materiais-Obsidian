---
titulo: "Questões - Fundamentos e Arquitetura"
aliases: ["Fundamentos e Arquitetura"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - revisao
  - questoes
  - quiz
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Modelo CIA e Princípios de Segurança]]"
  - "[[Modelagem de Ameaças - STRIDE e PASTA]]"
  - "[[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]]"
---

# Questões - Fundamentos e Arquitetura

## Resumo

11 questões de múltipla escolha sobre **Fundamentos e Arquitetura**, com gabarito comentado (clique no callout para expandir).

## Conceitos-chave

- Cada questão tem quatro alternativas e um comentário que explica o raciocínio.
- Conteúdo-fonte: [[Modelo CIA e Princípios de Segurança]], [[Modelagem de Ameaças - STRIDE e PASTA]], [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]], [[Webhooks e Polling]], [[Idempotência]].

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

Um invasor altera um alerta enquanto ele está na fila de mensagens. Qual propriedade da tríade CIA foi violada?

- A) Confidencialidade
- B) Integridade
- C) Disponibilidade
- D) Não repúdio

> [!success]- Gabarito: B
> A alteração não autorizada do conteúdo viola a integridade. Mitigações: HMAC, assinatura, TLS e validação de schema.

### Questão 2

Em STRIDE, qual categoria descreve alguém se passando pelo scanner ao chamar seu endpoint?

- A) Tampering
- B) Repudiation
- C) Spoofing
- D) Elevation of privilege

> [!success]- Gabarito: C
> Spoofing é a falsificação de identidade; a mitigação típica é autenticação forte (mTLS, OAuth) e assinatura de webhook.

### Questão 3

T1059 (Command and Scripting Interpreter) no MITRE ATT&CK é:

- A) Uma tática
- B) Uma técnica
- C) Um grupo de ameaça
- D) Uma ferramenta de defesa

> [!success]- Gabarito: B
> T1059 é uma técnica. Táticas são objetivos (como Execution) e técnicas são os meios.

### Questão 4

Qual padrão especifica requisitos de segurança verificáveis em três níveis?

- A) OWASP Top 10
- B) CIS Controls
- C) OWASP ASVS
- D) MITRE ATT&CK

> [!success]- Gabarito: C
> O ASVS define níveis 1, 2 e 3 de verificação; o Top 10 é de conscientização.

### Questão 5

Qual função foi adicionada ao NIST CSF na versão 2.0?

- A) Identify
- B) Govern
- C) Recover
- D) Detect

> [!success]- Gabarito: B
> A função Govern (GV) foi incluída na versão 2.0, junto das cinco existentes.

### Questão 6

Qual categoria de ferramenta inventaria dependências de terceiros e cruza com CVEs?

- A) DAST
- B) EDR
- C) SCA
- D) WAF

> [!success]- Gabarito: C
> SCA (Software Composition Analysis) analisa componentes de terceiros e vulnerabilidades associadas.

### Questão 7

Qual estilo de integração desacopla produtores e consumidores com um broker?

- A) Point-to-point síncrono
- B) Event-driven
- C) Chamada direta por RPC
- D) Planilha compartilhada

> [!success]- Gabarito: B
> Event-driven usa broker para comunicação assíncrona, com escala e reprocessamento, exigindo tratar duplicatas.

### Questão 8

Qual a melhor prática ao receber um webhook?

- A) Parsear o JSON e depois validar
- B) Validar o HMAC do corpo bruto com timestamp antes de processar
- C) Confiar no IP de origem apenas
- D) Processar de forma síncrona e demorada

> [!success]- Gabarito: B
> Valide a assinatura sobre o corpo bruto, com janela de tempo (anti-replay), e responda rápido.

### Questão 9

A entrega at-least-once de um broker exige que o consumidor seja:

- A) Mais rápido
- B) Idempotente
- C) Stateless apenas
- D) Single-thread

> [!success]- Gabarito: B
> Mensagens podem ser reentregues; sem idempotência haveria efeitos duplicados (por exemplo, tickets repetidos).

### Questão 10

Qual política de retry é mais adequada?

- A) Repetir imediatamente, sem limite
- B) Backoff exponencial com jitter, limitado e só para erros transitórios
- C) Repetir também erros 401
- D) Nunca repetir

> [!success]- Gabarito: B
> Backoff com jitter evita picos; erros permanentes (400, 401, 404) não devem ser repetidos.

### Questão 11

Qual esquema de normalização de eventos é associado ao Elastic?

- A) CEF
- B) STIX
- C) ECS
- D) SARIF

> [!success]- Gabarito: C
> ECS (Elastic Common Schema). CEF é formato do ArcSight, STIX é para inteligência e SARIF para análise estática.

## Veja também

- [[Modelo CIA e Princípios de Segurança]]
- [[Modelagem de Ameaças - STRIDE e PASTA]]
- [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]]
- [[Webhooks e Polling]]
- [[Idempotência]]
- [[MOC - Revisão - Integração]]

#seguranca/revisao/questoes #quiz
