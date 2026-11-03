---
titulo: "Métricas e Critérios de Sucesso"
tags:
  - ai-security
  - red-teaming
  - estatistica
nivel: "intermediario"
---

# Métricas e Critérios de Sucesso

Pré-requisitos: [[Metodologia de Testes]] · [[Como funcionam os LLMs]]

## 1. Definição

> [!info] Definição
> **Métricas** transformam observações de testes em números comparáveis. Em segurança de LLMs, como o comportamento é probabilístico, quase toda métrica é uma **taxa estimada** a partir de N repetições, e deve vir acompanhada de sua **incerteza**.

## 2. Contexto

JailbreakBench aponta como problema da área que trabalhos calculam custos e taxas de sucesso de maneiras incomparáveis e muitas vezes não reprodutíveis (Chao et al., 2024), e propõe ameaça, *system prompts*, *chat templates* e funções de pontuação padronizados. HarmBench também busca propriedades de avaliação padronizadas para comparar métodos e defesas (Mazeika et al., 2024). A lição para o estudante: **defina e publique sua métrica antes de rodar**.

## 3. Métricas principais

| Métrica | Fórmula | Interpretação | Cuidado |
|---|---|---|---|
| **Taxa de sucesso de ataque** (*attack success rate*, ASR) | falhas de segurança ÷ tentativas | Quanto o ataque funciona | Depende do juiz e do conjunto de ataques |
| **Taxa de recusa indevida** (*over-refusal rate*) | recusas em pedidos legítimos ÷ pedidos legítimos | Custo de utilidade | Exige conjunto de controles benignos |
| **Robustez** | 1 − ASR (por categoria) | Resistência sob um conjunto de ataques | Vale para aquele conjunto, não "em geral" |
| **Reprodutibilidade** | acertos ÷ repetições, com mesma config | Estabilidade do achado | Registre *seed* e parâmetros |
| **Regressão de segurança** | ASR(nova versão) − ASR(versão anterior) | Piora após mudança | Mesmo conjunto e mesmos parâmetros |
| **Tempo/consultas até a 1ª falha** | média de tentativas | Esforço do atacante | Sensível ao orçamento |
| **Cobertura** | casos executados ÷ superfícies mapeadas | Completude do teste | Alta cobertura ≠ segurança |
| **Concordância do juiz** | acordo entre juiz e humano | Qualidade da medição | Revise amostras |

> [!tip] Nunca reporte só o ASR
> Segurança e utilidade se movem juntas: um modelo que recusa tudo tem ASR zero e utilidade zero. Reporte **ASR e recusa indevida** lado a lado.

## 4. Julgamento do resultado (o "juiz")

Defina antes **como** cada execução será classificada:

| Tipo de juiz | Vantagem | Limitação |
|---|---|---|
| **Determinístico** (canário verificado por código, log de ferramenta) | Objetivo, reprodutível | Só cobre falhas previsíveis |
| **Regras/regex** | Simples | Frágil (formas alteradas) |
| **Classificador/LLM como juiz** | Cobre casos abertos | Tem erro, viés e custo; valide contra humanos |
| **Humano** | Padrão-ouro | Caro e lento; defina rubrica |

Use classificação em níveis: **violação total / parcial / ausente**, mais "inconclusivo" para saídas ambíguas.

> [!warning] Um juiz ruim infla o ASR
> Souly et al. (2024), no trabalho *StrongREJECT*, relatam que métodos de avaliação existentes faziam jailbreaks parecerem muito mais eficazes do que juízes humanos concluíam, e atribuem parte da diferença ao fato de que jailbreaks que passam pelo treinamento de segurança também podem **degradar a qualidade da resposta**. Na prática: "o modelo não recusou" não é o mesmo que "o modelo entregou o conteúdo pretendido". Meça a falha pelo **efeito real** (canário emitido, ferramenta chamada) e valide qualquer juiz automático contra uma amostra anotada por humanos.

## 5. Incerteza: intervalo de confiança

Para uma taxa k/n (k eventos em n tentativas), o **intervalo de Wilson** (95%) é uma escolha robusta para amostras pequenas:

$$
\text{centro}=\frac{\hat p+\frac{z^2}{2n}}{1+\frac{z^2}{n}},\quad
\text{margem}=\frac{z\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}}}{1+\frac{z^2}{n}},\quad z=1{,}96
$$

Script de apoio (Python 3, sem dependências):

```python
import math

def wilson(k: int, n: int, z: float = 1.96):
    """Intervalo de Wilson para proporção k/n."""
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    denom = 1 + z**2 / n
    centro = (p + z**2 / (2 * n)) / denom
    margem = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (p, max(0.0, centro - margem), min(1.0, centro + margem))

if __name__ == "__main__":
    for k, n in [(0, 20), (2, 20), (4, 30), (10, 100)]:
        p, lo, hi = wilson(k, n)
        print(f"{k}/{n}: taxa={p:.1%}  IC95%=[{lo:.1%}, {hi:.1%}]")
```

Leituras importantes:

- **0 falhas em 20 tentativas não significa risco zero.** Pela "regra dos três", o limite superior aproximado de 95% para a taxa é cerca de 3/n, ou seja, ≈ 15% com n = 20.
- Intervalos largos significam "preciso de mais repetições".
- Para comparar duas configurações, verifique se os intervalos se sobrepõem substancialmente antes de afirmar diferença; para decisões importantes, use um teste estatístico apropriado.

## 6. Controle de variáveis

| Variável | Como controlar |
|---|---|
| Aleatoriedade | Fixar *seed* quando possível; repetir N vezes |
| Temperatura e amostragem | Registrar; comparar com mesmos valores |
| Versão do modelo | Registrar identificador exato e data |
| Prompt e contexto | Versionar arquivos de prompt |
| Idioma e tradução | Documentar método |
| Ordem dos testes | Randomizar; evitar efeito de memória entre execuções (resetar sessão) |

## 7. Critérios de sucesso do **teste** e da **defesa**

Defina critérios **antes**, por exemplo:

| Objetivo | Critério (exemplo, ajuste ao seu contexto) |
|---|---|
| Ação sensível não pode ser disparada por conteúdo externo | 0 chamadas em ≥ 125 execuções por caso (com 0 falhas, o limite superior do IC95% de Wilson só fica abaixo de 3% a partir de n = 125; com n = 100 ele é ≈ 3,7%) |
| Recusa indevida aceitável | ≤ 5% em controles benignos |
| Regressão | Nenhuma categoria com piora estatisticamente relevante |

> [!warning] Estes limiares são exemplos didáticos
> Não são padrões. O limite aceitável depende do impacto: onde há ações irreversíveis, a meta correta é **impedir o efeito por controle determinístico**, não "reduzir a probabilidade".

## 8. Limitações

- Métricas dependem do **conjunto de casos**: ASR de um conjunto fraco é otimista.
- Juízes automáticos erram.
- Resultados não se generalizam para outros modelos, versões ou configurações.
- Atacantes adaptativos ([[Ataques Adaptativos e Transferência]]) invalidam avaliações apenas com ataques fixos.

## 9. Aplicação em segurança

Use as métricas para: comparar configurações ([[Laboratório 05 - Avaliação Comparativa]]), justificar prioridade de correção e detectar regressões após mudanças ([[Monitoramento e Resposta]]).

## 10. Exercício

- [ ] Execute o script com seus próprios dados e interprete os intervalos.
- [ ] Para o alvo de brinquedo, calcule ASR, recusa indevida e reprodutibilidade em 30 repetições.
- [ ] Explique por que 0/20 não prova segurança.

## Referências

- Chao, P. et al. **JailbreakBench**. arXiv:2404.01318 (2024). <https://arxiv.org/abs/2404.01318> — consultado em 15/10/2026.
- Mazeika, M. et al. **HarmBench**. arXiv:2402.04249 (2024). <https://arxiv.org/abs/2402.04249> — consultado em 15/10/2026.
- Ganguli, D. et al. (2022), arXiv:2209.07858 — discutem metodologia estatística e incertezas de red teaming. <https://arxiv.org/abs/2209.07858> — consultado em 15/10/2026.
- Souly, A. et al. **A StrongREJECT for Empty Jailbreaks**. arXiv:2402.10260, 15/02/2024 (v2: 27/08/2024). <https://arxiv.org/abs/2402.10260> — consultado em 15/10/2026.
- O intervalo de Wilson e a "regra dos três" são técnicas estatísticas clássicas; as fórmulas acima podem ser conferidas em qualquer texto de estatística (não citado aqui por fonte única).

## Próximos passos
- [[Relatório de Vulnerabilidades]]
