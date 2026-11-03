---
tags:
  - docker
  - redes
  - isolamento
  - seguranca
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Visão geral das redes Docker]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Rede none

`--network none` entrega ao container apenas a interface de **loopback**. Nenhuma comunicação de entrada ou saída.

```bash
docker run --rm --network none alpine:3.20 ip addr
docker run --rm --network none alpine:3.20 wget -T 3 -qO- http://example.com || echo "sem rede, como esperado"
```

## Usos

- Processamento em lote de dados sensíveis, sem risco de exfiltração.
- Testes de comportamento offline.
- Containers que recebem redes configuradas manualmente por ferramentas externas.

> [!tip] Defesa em profundidade
> Containers que só processam arquivos locais (conversão, compilação) não precisam de rede. Use `none` e monte entradas/saídas por volume.

## Exercício

Execute um container com `--network none` e demonstre que `ping 8.8.8.8` falha mas `ping 127.0.0.1` funciona.

## Veja também

- [[Visão geral das redes Docker]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Redes]]
