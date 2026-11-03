---
tags:
  - docker
  - desenvolvimento
  - compose
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Bancos de dados locais]]"
  - "[[Depuração de rede]]"
  - "[[Ambientes de desenvolvimento reproduzíveis]]"
---

# Filas e mensageria com RabbitMQ e Kafka

## RabbitMQ

```yaml
services:
  rabbitmq:
    image: rabbitmq:3-management
    environment:
      RABBITMQ_DEFAULT_USER: app
      RABBITMQ_DEFAULT_PASS: senha-de-laboratorio
    ports:
      - "127.0.0.1:5672:5672"      # AMQP
      - "127.0.0.1:15672:15672"    # painel de gerenciamento
    volumes:
      - rabbit_data:/var/lib/rabbitmq
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "ping"]
      interval: 15s
      timeout: 10s
      retries: 10

volumes:
  rabbit_data:
```

Painel: `http://localhost:15672`.

> [!info] Usuário `guest`
> O usuário padrão `guest` só aceita conexões **de localhost dentro do container**. Por isso o exemplo define outro usuário.

## Kafka (modo KRaft, um nó, desenvolvimento)

```yaml
services:
  kafka:
    image: apache/kafka:3.8.0
    ports:
      - "127.0.0.1:9092:9092"
    volumes:
      - kafka_data:/var/lib/kafka/data

volumes:
  kafka_data:
```

```bash
docker compose up -d kafka
# Criar um tópico e produzir/consumir com as ferramentas da própria imagem
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic pedidos \
  --bootstrap-server localhost:9092
docker compose exec -T kafka /opt/kafka/bin/kafka-console-producer.sh \
  --topic pedidos --bootstrap-server localhost:9092 <<< "pedido-1"
docker compose exec kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --topic pedidos --from-beginning --max-messages 1 --bootstrap-server localhost:9092
```

> [!question] Verificar na documentação oficial
> A imagem oficial `apache/kafka` e suas variáveis de listeners (*advertised listeners*) variam por versão. Para acesso de **outros containers** (não do host), é necessário configurar um segundo listener com o nome do serviço; consulte a página da imagem.

> [!warning] Dev, não produção
> Um único nó sem replicação não oferece durabilidade. Em produção, use clusters gerenciados ou configurações com replicação.

## Exercício

Suba o RabbitMQ, publique uma mensagem no painel e consuma-a com um script. Depois repita o conceito com um tópico Kafka.

## Veja também

- [[Bancos de dados locais]]
- [[Depuração de rede]]
- [[Ambientes de desenvolvimento reproduzíveis]]
- [[MOC - Desenvolvimento]]
