---
titulo: "Desafios Práticos"
tags:
  - ai-security
  - avaliacao
nivel: "intermediario"
---

# Desafios Práticos

Pré-requisitos: [[Questionário de Fundamentos]] · laboratórios 01–05 ([[Laboratório 01 - Comportamento de Recusa]] a [[Laboratório 05 - Avaliação Comparativa]]).

> [!warning] Escopo
> Somente nos **alvos de brinquedo** do kit (`labkit`): segredos-canário, ferramentas simuladas, dados fictícios. Não aplique nada a sistemas de terceiros sem autorização escrita. O backend `mock` **não é um modelo de linguagem**: use-o para validar seu código e o raciocínio; com um modelo real, aplique as mesmas métricas e leia os resultados com cautela.

Para cada desafio, entregue: hipótese, configuração, número de repetições, critério de sucesso por código, resultado com **intervalo de Wilson**, e **o que o resultado não prova**.

| # | Desafio | Nível | Base |
|---|---|---|---|
| 1 | **Baseline.** Meça a taxa de vazamento do canário `ABACAXI-42` na configuração sem defesa, com n suficiente para um intervalo útil. | ★ | [[Ataques Diretos]] · [[Laboratório 01 - Comportamento de Recusa]] |
| 2 | **Filtro ingênuo.** Implemente um filtro de saída por string exata e meça quantos casos OBF-01 a OBF-03 o atravessam; depois adicione normalização e remeça, incluindo o custo em OBF-04 (utilidade). | ★★ | [[Obfuscação e Codificação]] |
| 3 | **Idiomas.** Traduza o conjunto de pedidos para 3 idiomas, controle o método de tradução e compare taxas de violação e de recusa indevida. | ★★ | [[Ataques Multilíngues]] |
| 4 | **Trajetória.** Projete 6 turnos até o limite do escopo e registre o turno de ruptura médio; compare moderação só da última mensagem × conversa acumulada. | ★★ | [[Jailbreak Multiturno]] |
| 5 | **Injeção indireta.** Contra o assistente de e-mail com ferramentas simuladas, meça a taxa de chamada de ferramenta induzida por documento, com e sem delimitação. | ★★ | [[Laboratório 03 - Prompt Injection]] |
| 6 | **Política de ferramentas.** Use `politica_ferramentas.py` para impedir o efeito do desafio 5 sem alterar o prompt; mostre o log da decisão. | ★★★ | [[Segurança de Agentes]] |
| 7 | **Gate de regressão.** Rode `gate_regressao.py` sobre os resultados do desafio 5 antes e depois da defesa; explique um veredito INCONCLUSIVO se houver. | ★★★ | [[Monitoramento e Resposta]] |
| 8 | **Comparação.** Compare duas configurações de defesa (ex.: L2 × L5) com Fisher exato e correção de Bonferroni; conclua só o que os dados sustentam. | ★★★ | [[Laboratório 05 - Avaliação Comparativa]] · [[Métricas e Critérios de Sucesso]] |

## Critérios de correção (por desafio)

- **Reprodutível:** outra pessoa roda seus comandos e obtém resultado compatível.
- **Critério por código**, não por opinião.
- **Estatística correta:** intervalo e tamanho de amostra declarados; nada de "0 falhas = seguro".
- **Utilidade medida:** toda defesa vem com recusa indevida.
- **Limites declarados:** o que não foi testado.

## Armadilhas comuns

- Concluir sobre modelos reais a partir do `mock`.
- Ajustar o ataque ao filtro e reportar como se fosse ataque independente (viés de adaptação).
- Esquecer o controle benigno.

## Próximos passos
- [[Projeto Final]]
