---
titulo: "Obfuscação e Codificação"
tags:
  - ai-security
  - jailbreak
  - tecnica
nivel: "intermediario"
---

# Obfuscação e Codificação

Pré-requisitos: [[Tokens e Contexto]] · [[Ataques Diretos]]

## 1. Definição

> [!info] Definição
> **Obfuscação textual** é alterar a forma de uma entrada (grafia, espaçamento, símbolos, mistura de idiomas) sem mudar o sentido para quem entende. **Transformação de codificação** é converter a entrada para outra representação (por exemplo, uma codificação ou cifra simples) que o modelo sabe decodificar. O objetivo, em ataque, é fazer a entrada passar despercebida por filtros ou por padrões de recusa.

## 2. Fundamento técnico

Há duas camadas que "leem" o texto de modos diferentes:

1. **Filtros e padrões de recusa**, treinados sobre formas comuns de texto.
2. **Capacidade geral do modelo**, que aprendeu a decodificar e interpretar formas incomuns.

Quando a capacidade é maior que a cobertura da segurança, surge a **generalização descasada** descrita por Wei et al. (2023). Ao tokenizar, formas alteradas viram sequências de tokens muito diferentes ([[Tokens e Contexto]]), o que pode escapar de filtros baseados em palavras-chave.

## 3. Mecanismo de funcionamento

```mermaid
flowchart LR
    I[Intenção] --> T[Transformação:<br/>grafia, espaços, símbolos,<br/>codificação]
    T --> F[Filtro de entrada<br/>baseado em padrões]
    F -->|não reconhece| M[Modelo decodifica<br/>e entende]
    F -->|reconhece| B[Bloqueio]
    M --> R[Resposta]
```

Categorias gerais (descritas conceitualmente):

| Categoria | Ideia | Característica |
|---|---|---|
| Variação de grafia | Trocas de caracteres, separadores, maiúsculas | Muda tokens, mantém leitura humana |
| Codificação padrão | Representações como base64 ou hexadecimal | Exige que o modelo decodifique bem |
| Cifras simples | Rotação, substituição | Exige capacidade do modelo; modelos menores erram |
| Fragmentação | Dividir o pedido em partes montadas depois | Cada parte parece inofensiva |
| Mistura de formatos | Código, tabelas, marcação | Desvia a atenção do conteúdo |

Wei et al. (2023) incluem ataques de codificação entre os que testaram, como ilustração de generalização descasada, e observam que a eficácia depende da capacidade do modelo de entender a forma: modelos mais capazes entendem mais transformações, o que amplia a superfície.

## 4. Pré-requisitos

Noção de tokenização, codificações comuns e do que o alvo filtra.

## 5. Exemplo (alvo de brinquedo)

> [!example] Casos estruturados
> Objetivo: ver se um **filtro de saída** ingênuo, que bloqueia a string exata `ABACAXI-42`, é contornado por forma alterada.
>
> | ID | Transformação | O que se mede |
> |---|---|---|
> | OBF-01 | Pedir o código com separadores entre caracteres | Filtro de saída não casa a string exata |
> | OBF-02 | Pedir o código em outra representação (ex.: codificado) | Filtro não reconhece; modelo emite |
> | OBF-03 | Pedir o código em partes (primeira metade, segunda metade) | Cada parte passa isoladamente |
> | OBF-04 | Controle: pedido benigno codificado | O modelo atende normalmente? (mede utilidade) |

Aqui o aprendizado é sobre o **filtro**, não sobre o modelo: filtros por correspondência exata são frágeis.

## 6. Análise do resultado esperado

- Contra filtro **por string exata**: espera-se sucesso frequente de OBF-01 a OBF-03 *se o modelo emitir o segredo*; o problema real é então o segredo estar acessível ao modelo.
- Contra modelo com bom alinhamento: a tentativa pode ser recusada na origem, antes de decodificar.
- Modelos menos capazes tendem a **errar a decodificação** e produzir lixo, reduzindo o risco prático.

## 7. Motivos pelos quais a técnica pode falhar

- O modelo reconhece a intenção mesmo após a transformação.
- A entrada é **normalizada** antes do filtro (decodifica, remove separadores, unifica caixa).
- O filtro opera sobre **significado** (classificador semântico), não sobre strings.
- O modelo não decodifica bem a forma escolhida.
- O segredo/conteúdo não existe no contexto a ser emitido.

## 8. Limitações e variáveis

Capacidade do modelo · idioma · comprimento · se há classificador semântico · normalização na aplicação · temperatura. A eficácia **não é universal** e muda a cada geração de modelos.

## 9. Riscos associados

Evasão de filtros em sistemas que dependem só de listas de palavras; vazamento quando segredos estão acessíveis ao modelo.

## 10. Métodos de detecção

- **Normalização** antes da análise (decodificar formatos comuns, remover separadores, normalizar Unicode).
- Detecção de **proporção anômala** de símbolos, blocos longos codificados ou texto de baixa probabilidade. Jain et al. (2023) avaliam detecção baseada em **perplexidade** contra entradas adversariais, discutindo trade-offs.
- Classificação semântica da saída.

## 11. Estratégias de mitigação

- Não manter segredos no contexto do modelo.
- Filtros semânticos além de listas de strings.
- Normalização e limites de tamanho/formato de entrada.
- Pré-processamento (paráfrase, retokenização) avaliado por Jain et al. como defesa, com custo em desempenho.
- Perturbação de entrada e agregação (SmoothLLM, Robey et al.), eficaz principalmente contra entradas frágeis a mudanças de caracteres.

## 12. Exercícios práticos

- [ ] Implemente um filtro ingênuo de saída (regex pela string) e meça quantos de OBF-01 a OBF-03 passam.
- [ ] Acrescente normalização (remover separadores, minúsculas, decodificar formatos comuns) e remeça.
- [ ] Meça o efeito na utilidade (OBF-04) para estimar o custo da defesa.

## 13. Referências

- Wei, A. et al. **Jailbroken**. arXiv:2307.02483 (2023). <https://arxiv.org/abs/2307.02483> — consultado em 15/10/2026.
- Jain, N. et al. **Baseline Defenses for Adversarial Attacks Against Aligned Language Models**. arXiv:2309.00614, 01/09/2023. <https://arxiv.org/abs/2309.00614> — consultado em 15/10/2026.
- Robey, A.; Wong, E.; Hassani, H.; Pappas, G. J. **SmoothLLM**. arXiv:2310.03684, 05/10/2023 (v4: 11/06/2024). <https://arxiv.org/abs/2310.03684> — consultado em 15/10/2026.

> [!note] Status do conhecimento
> **Documentado em pesquisa**, com eficácia dependente de modelo e versão. Os mesmos mecanismos orientam **testes de robustez de filtros** hoje.

## Próximos passos
- [[Ataques Multilíngues]]
