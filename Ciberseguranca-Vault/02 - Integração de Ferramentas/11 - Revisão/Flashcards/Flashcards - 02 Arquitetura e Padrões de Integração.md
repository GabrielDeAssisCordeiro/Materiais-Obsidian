---
titulo: "Flashcards - 02 Arquitetura e Padrões de Integração"
aliases: ["Flashcards 02"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]]"
  - "[[Webhooks e Polling]]"
  - "[[Filas e Streaming - Kafka e RabbitMQ]]"
---

# Flashcards - 02 Arquitetura e Padrões de Integração

## Resumo

Cartões de revisão do módulo **Arquitetura e Padrões de Integração**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]], [[Webhooks e Polling]], [[Filas e Streaming - Kafka e RabbitMQ]], [[Idempotência]].

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

Plugin Spaced Repetition para Obsidian.

## Flashcards

#flashcards

Qual o problema do point-to-point com muitos sistemas?::O número de conexões cresce rápido (até n(n-1)/2), multiplicando autenticações e formatos.
Qual a principal vantagem do event-driven?::Desacopla produtores e consumidores, permitindo escala, reprocessamento e tolerância a falhas.
Qual a diferença entre webhook e polling?::Webhook é push do emissor; polling é o consumidor consultando periodicamente.
Como validar a autenticidade de um webhook?::Verificar o HMAC sobre o corpo bruto, com timestamp para anti-replay, antes de parsear.
Por que um receptor de webhook deve responder 2xx rapidamente?::Para evitar timeout do emissor; o processamento ocorre depois, de forma assíncrona.
O que a entrega at-least-once implica para o consumidor?::Mensagens podem chegar duplicadas; o consumidor deve ser idempotente.
O que é uma dead-letter queue?::Fila para mensagens que esgotaram as tentativas, destinada à análise.
Qual a ideia central do Kafka em comparação ao RabbitMQ?::Kafka é um log distribuído com retenção e reprocessamento; RabbitMQ é um broker com roteamento flexível e ack por mensagem.
O que faz o padrão Adapter?::Traduz a interface de um sistema para a esperada pela aplicação, isolando detalhes do fornecedor.
O que são OCSF e ECS?::Esquemas comuns para normalizar eventos de segurança; OCSF é aberto e ECS é do Elastic.
Qual a relação entre STIX e TAXII?::STIX é a linguagem JSON de objetos de inteligência; TAXII é o protocolo HTTP para compartilhá-los.
O que é idempotência?::Executar a operação várias vezes produz o mesmo efeito que executá-la uma vez.
Por que usar jitter no backoff?::Evita que muitos clientes tentem ao mesmo tempo, gerando picos sincronizados.
Quais erros HTTP costumam valer retry?::Transitórios, como 429, 500, 502, 503 e 504; não se repetem 400, 401 e 404.
O que é um token bucket?::Algoritmo de rate limiting em que tokens são repostos a taxa constante, permitindo rajadas controladas.
Quais são os estados do circuit breaker?::Fechado, aberto e meio-aberto.

## Veja também

- [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]]
- [[Webhooks e Polling]]
- [[Filas e Streaming - Kafka e RabbitMQ]]
- [[Idempotência]]
- [[MOC - Revisão - Integração]]

#flashcards #seguranca/revisao/flashcards
