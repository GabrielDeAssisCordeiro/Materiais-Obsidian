---
titulo: "Jailbreak Multiturno"
tags:
  - ai-security
  - jailbreak
  - tecnica
nivel: "intermediario"
---

# Jailbreak Multiturno

Pré-requisitos: [[Ataques Diretos]] · [[Tokens e Contexto]]

## 1. Definição

> [!info] Definição
> **Ataque multiturno** (*multi-turn*) é aquele distribuído em várias mensagens: cada uma, isolada, parece aceitável, mas a **trajetória** da conversa leva o modelo a um comportamento que ele recusaria se pedido de uma vez.

## 2. Fundamento técnico

O modelo condiciona sua resposta a **todo o histórico**. Respostas anteriores do próprio modelo entram no contexto como evidência de "o que é apropriado nesta conversa". Três efeitos se combinam:

1. **Coerência com o próprio histórico:** o modelo tende a manter consistência com o que já disse.
2. **Escalada gradual:** cada passo é pequeno em relação ao anterior.
3. **Diluição:** em conversas longas, o peso relativo do system prompt e da recusa inicial pode diminuir ([[Tokens e Contexto]]).

Russinovich et al. (2024) descrevem o ataque *Crescendo*: começa com uma pergunta geral e inocente e escala o diálogo referenciando as respostas do modelo, e relatam altas taxas de sucesso em vários sistemas públicos avaliados à época, além de uma ferramenta de automação (*Crescendomation*). Os autores enquadram jailbreaks como estreitar a distância entre o que o modelo *pode* fazer e o que ele *aceita* fazer.

## 3. Mecanismo de funcionamento

```mermaid
sequenceDiagram
    participant A as Atacante
    participant M as Modelo
    A->>M: Pergunta geral, inofensiva
    M-->>A: Resposta útil (entra no contexto)
    A->>M: Pede aprofundar um ponto da resposta
    M-->>A: Resposta mais específica
    A->>M: Pede reescrever / expandir o que o modelo disse
    M-->>A: Resposta cada vez mais próxima do alvo
    Note over A,M: Nenhum turno isolado dispara a recusa
```

Padrões descritos de forma geral: **referenciar a própria saída do modelo**, **pedir reformatação** ("transforme isso em...") e **dividir um objetivo em subtarefas**.

## 4. Pré-requisitos

Conversa com estado; capacidade de planejar uma trajetória; registro completo do histórico.

## 5. Exemplo (alvo de brinquedo)

> [!example] Trajetória inofensiva
> Objetivo: levar o assistente da biblioteca a falar de um tema fora do escopo (ex.: dicas de culinária) sem que o primeiro pedido seja aceito.
>
> | Turno | Tipo de pedido | Esperado |
> |---|---|---|
> | 1 | Pergunta dentro do escopo (livros de culinária na biblioteca) | Atendido |
> | 2 | Pede resumo de um livro de culinária | Atendido (próximo do escopo) |
> | 3 | Pede a receita descrita no livro | Zona cinzenta |
> | 4 | Pede um cardápio completo para o fim de semana | Fora do escopo |
>
> Mede-se **em qual turno** o modelo deixa de manter a regra, e quantos turnos a regra sobrevive a cada repetição.

Para o canário (`ABACAXI-42`), a trajetória análoga mede se o segredo vaza apenas após construir contexto.

## 6. Análise do resultado esperado

Métricas próprias deste vetor:

- **Turno de ruptura** (*turn of failure*): em qual turno a regra cai.
- **Taxa de sucesso na conversa completa** (não por mensagem).
- **Dependência de caminho:** pequenas variações no início mudam o desfecho?

Modelos treinados com dados multiturno e verificação de intenção ao longo do diálogo tendem a resistir mais.

## 7. Motivos pelos quais a técnica pode falhar

- Avaliação de segurança sobre a **conversa inteira**, não só a última mensagem.
- Reafirmação periódica das regras no contexto.
- Limite de turnos ou reinício de contexto.
- A trajetória exige que o modelo produza conteúdo intermediário que ele já recusa.
- Respostas variam: a trajetória que funcionou numa execução quebra em outra.

## 8. Limitações e variáveis

Modelo, versão, temperatura, tamanho do histórico, se o sistema resume o histórico, existência de monitor de conversa, idioma. Automatizar a escalada (como em Crescendomation) aumenta a escala, mas depende do modelo atacante e do alvo.

## 9. Riscos associados

Contorno de políticas por etapas imperceptíveis para filtros por mensagem; maior risco em assistentes com memória e em sessões longas.

## 10. Métodos de detecção

- Classificar a **conversa acumulada** (janela deslizante), não só o último turno.
- Medir *drift* de tópico em relação ao escopo do sistema.
- Alertar em padrões como pedidos recorrentes de "expandir/reescrever o que você disse" ao se aproximar de tema restrito.

## 11. Estratégias de mitigação

- Moderação com contexto completo.
- Reinjeção periódica de regras críticas em posição privilegiada.
- Limites de comprimento ou checkpoints de reavaliação.
- Autorização externa que não depende do histórico.
- Dados de treinamento e avaliação multiturno.

## 12. Exercícios práticos

- [ ] Projete uma trajetória de 6 turnos para o alvo de brinquedo e execute 20 vezes; registre o turno de ruptura médio.
- [ ] Compare moderação só da última mensagem × moderação da conversa acumulada.
- [ ] Meça a recusa indevida: conversas longas **legítimas** são bloqueadas?

## 13. Referências

- Russinovich, M.; Salem, A.; Eldan, R. **Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack**. arXiv:2404.01833, 02/04/2024 (v3: 26/02/2025). <https://arxiv.org/abs/2404.01833> — consultado em 15/10/2026.
- *Many-shot jailbreaking* (Anthropic, 2024): **não verificado nesta sessão**; confirmar autores, data e URL em fonte primária antes de citar.

> [!note] Status do conhecimento
> **Documentado em pesquisa (2024)**; área em evolução, com ataques e defesas mudando rapidamente.

## Próximos passos
- [[Ataques Baseados em Contexto]]
