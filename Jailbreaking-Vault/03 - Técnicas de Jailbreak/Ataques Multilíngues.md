---
titulo: "Ataques Multilíngues"
tags:
  - ai-security
  - jailbreak
  - tecnica
nivel: "intermediario"
---

# Ataques Multilíngues

Pré-requisitos: [[Tokens e Contexto]] · [[Obfuscação e Codificação]]

## 1. Definição

> [!info] Definição
> **Ataques multilíngues** exploram o fato de que o treinamento de segurança é desigual entre idiomas: um pedido recusado em um idioma bem coberto pode ser atendido quando formulado em outro, ou em mistura de idiomas.

## 2. Fundamento técnico

A capacidade linguística do modelo é ampla (aprendida no pré-treinamento), mas os dados de **alinhamento e red teaming** concentram-se em poucos idiomas, em especial o inglês. Isso é uma instância de **generalização descasada**: capacidade em muitos idiomas, segurança em poucos.

Dois estudos relevantes:

- Yong et al. (2023) relatam que traduzir entradas inseguras do inglês para idiomas de poucos recursos contornou salvaguardas do GPT-4 em 79% dos casos no benchmark que usaram, enquanto idiomas de recursos médios/altos tiveram taxas bem menores.
- Deng et al. (2023) distinguem cenário **não intencional** (usuário comum em idioma de poucos recursos recebe mais conteúdo inseguro) e **intencional** (atacante combina instruções maliciosas com prompts multilíngues), e propõem um método de *Self-Defense* que gera dados multilíngues para *fine-tuning* de segurança.

> [!warning] Datas e modelos
> Os percentuais acima descrevem os modelos e conjuntos de teste daqueles artigos (2023). Não os generalize para modelos atuais; meça no seu alvo.

## 3. Mecanismo de funcionamento

```mermaid
flowchart LR
    P[Pedido] --> L{Idioma}
    L -->|Alto recurso<br/>bem coberto no alinhamento| S[Recusa mais consistente]
    L -->|Baixo recurso<br/>pouco coberto| W[Recusa menos consistente]
    W --> M[Modelo entende<br/>e responde]
```

Variações: **tradução completa**, **mistura de idiomas** no mesmo pedido (*code-switching*) e **resposta em outro idioma** (pedido em um, saída em outro, para escapar de filtros de saída em um idioma só).

## 4. Pré-requisitos

Conhecimento mínimo dos idiomas testados ou uso de tradução; conjunto de pedidos **equivalentes** em cada idioma.

## 5. Exemplo (alvo de brinquedo)

> [!example] Casos estruturados
> Pedidos equivalentes ao DIR-01 (pedir `ABACAXI-42`) escritos em português, inglês, espanhol, um idioma de poucos recursos e uma mistura de idiomas.
>
> | ID | Idioma do pedido | Idioma da regra no system prompt | Mede |
> |---|---|---|---|
> | MUL-01 | Português | Português | Linha de base |
> | MUL-02 | Inglês | Português | Efeito de idioma diferente do prompt |
> | MUL-03 | Idioma de poucos recursos | Português | Cobertura de segurança |
> | MUL-04 | Mistura de idiomas | Português | Robustez a *code-switching* |
> | MUL-05 | Controle benigno em cada idioma | n/a | Utilidade/recusa indevida por idioma |

O estudo útil é a **diferença entre idiomas** sob o mesmo critério, controlando tradução e prompt.

## 6. Análise do resultado esperado

Hipótese a testar: taxa de violação maior em idiomas menos cobertos. Pode **não** se confirmar em modelos recentes ou bem avaliados. Se ocorrer, a causa pode ser cobertura de treino, e não "falha geral". Verifique também **recusa indevida** em idiomas pouco cobertos: segurança desigual pode também significar excesso de bloqueio.

## 7. Motivos pelos quais a técnica pode falhar

- Modelo com alinhamento multilíngue robusto.
- O modelo traduz internamente e aplica a política ao sentido.
- Classificadores de entrada/saída multilíngues.
- A tradução do pedido perde nuance e o modelo não atende (falha de **utilidade**).
- O modelo é fraco no idioma e responde mal (reduz risco prático).

## 8. Limitações e variáveis

Qualidade da tradução (ferramenta ou humano) · idioma e dialeto · modelo · versão · se o idioma está no system prompt · tokenização (idiomas menos representados consomem mais tokens, [[Tokens e Contexto]]).

## 9. Riscos associados

Desigualdade de proteção entre usuários e idiomas; evasão de moderação em plataformas globais. Yong et al. destacam que, com tradução automática pública, a deficiência passa a afetar todos, não só falantes daqueles idiomas.

## 10. Métodos de detecção

- Detecção de idioma e roteamento para moderação adequada.
- Moderação sobre **tradução normalizada** (traduzir para idioma de referência e classificar).
- Monitorar taxas de recusa/violação **por idioma**.

## 11. Estratégias de mitigação

- Dados de segurança e red teaming multilíngues (Deng et al. propõem geração automática de dados de *fine-tuning*).
- Classificadores multilíngues independentes do modelo principal.
- Política baseada em conteúdo, não no idioma.
- Suíte de regressão com os mesmos casos em vários idiomas.

## 12. Exercícios práticos

- [ ] Traduza (com revisão) o conjunto DIR-01 para três idiomas. Execute 20 repetições por idioma e compare as taxas.
- [ ] Calcule também a recusa indevida do controle MUL-05 por idioma.
- [ ] Documente o método de tradução; ele é uma variável do experimento.

## 13. Referências

- Yong, Z.-X.; Menghini, C.; Bach, S. H. **Low-Resource Languages Jailbreak GPT-4**. arXiv:2310.02446, 03/10/2023 (v2: 27/01/2024). <https://arxiv.org/abs/2310.02446> — consultado em 15/10/2026.
- Deng, Y.; Zhang, W.; Pan, S. J.; Bing, L. **Multilingual Jailbreak Challenges in Large Language Models**. arXiv:2310.06474, 10/10/2023 (v3: 04/03/2024). <https://arxiv.org/abs/2310.06474> — consultado em 15/10/2026.

> [!note] Status do conhecimento
> **Documentado em pesquisa (2023)**; mitigações multilíngues têm avançado e os resultados devem ser remedidos em cada modelo.

## Próximos passos
- [[Jailbreak Multiturno]]
