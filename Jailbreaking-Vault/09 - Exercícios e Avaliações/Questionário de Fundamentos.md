---
titulo: "Questionário de Fundamentos"
tags:
  - ai-security
  - avaliacao
nivel: "intermediario"
---

# Questionário de Fundamentos

Pré-requisitos: módulos 1 a 7. Responda **antes** de abrir os gabaritos (callouts recolhidos). Meta: 80% para seguir ao [[Projeto Final]]; abaixo disso, releia as notas indicadas em cada gabarito.

## Parte A — Conceitos (módulos 1–2)

**1.** Qual a diferença de alvo entre jailbreak e prompt injection?
> [!success]- Gabarito
> Jailbreak mira a **política de comportamento do modelo**; prompt injection mira a **tarefa e os controles da aplicação**. Veja [[Jailbreak vs Prompt Injection]].

**2.** Por que "o modelo é bem alinhado" não implica "o sistema é seguro contra injeção"?
> [!success]- Gabarito
> A injeção não exige violar política de conteúdo: o modelo apenas segue o que parece instrução. O dano vem de ferramentas com privilégio excessivo, falta de autorização externa e de separação de conteúdo confiável. [[Conceitos Fundamentais]].

**3.** Cite os três vértices do triângulo de risco e diga qual remover num assistente que só resume páginas.
> [!success]- Gabarito
> Conteúdo não confiável, dados privados e ação/saída externa. Resposta aceitável: remover a ação externa (sem ferramentas), pois o pior efeito vira texto no resumo.

**4.** Por que SQL parametrizado não tem equivalente direto em prompts?
> [!success]- Gabarito
> Em SQL, código e dados vão por canais distintos por construção. Em LLMs, instruções e dados são concatenados num único fluxo de tokens. [[Tokens e Contexto]].

**5.** O que é a hierarquia de instruções e por que ela é estatística, não garantia?
> [!success]- Gabarito
> Prioridade entre system prompt, usuário e conteúdo de ferramentas; é aprendida no treino (Wallace et al., 2024), logo o modelo pode errar. [[System Prompt e Hierarquia de Instruções]].

## Parte B — Técnicas (módulo 3–4)

**6.** Por que um filtro de saída por string exata é frágil contra obfuscação?
> [!success]- Gabarito
> O modelo decodifica formas alteradas (separadores, codificações) que o filtro não reconhece. O problema de fundo é o segredo estar acessível ao modelo. [[Obfuscação e Codificação]].

**7.** Que hipótese mede um experimento multilíngue e que controle é indispensável?
> [!success]- Gabarito
> Que a taxa de violação é maior em idiomas menos cobertos pelo treino de segurança; o controle é o pedido **benigno equivalente** por idioma (recusa indevida) e registrar o método de tradução. [[Ataques Multilíngues]].

**8.** Quais métricas são próprias de ataques multiturno?
> [!success]- Gabarito
> Turno de ruptura, taxa de sucesso na conversa completa e dependência de caminho. [[Jailbreak Multiturno]].

**9.** Qual a diferença entre ataque baseado em contexto e injeção indireta?
> [!success]- Gabarito
> O primeiro foca em como o contexto molda o comportamento em geral; o segundo, num terceiro que planta conteúdo para atacar outro usuário ou agente. [[Ataques Baseados em Contexto]] · [[Injeção Indireta]].

**10.** Por que ataques adaptativos importam ao avaliar uma defesa?
> [!success]- Gabarito
> Uma defesa testada só contra ataques fixos pode parecer forte; o atacante real se ajusta a ela. [[Ataques Adaptativos e Transferência]].

## Parte C — Defesa (módulo 7)

**11.** Ordene por robustez: instrução no prompt, política de ferramentas em código, remover o segredo do contexto.
> [!success]- Gabarito
> Mais robusto: **remover o segredo do contexto**; depois política em código (fora do modelo); por último a instrução no prompt (estatística). [[Defesa em Camadas]].

**12.** O que é um contrato de saída e o que ele impede?
> [!success]- Gabarito
> Formato obrigatório validado por código; rejeita saídas fora do formato (campos extras, texto livre), limitando o que a saída pode carregar. [[Validação de Entradas e Saídas]].

**13.** Por que a autorização de uma ação sensível deve ficar fora do modelo?
> [!success]- Gabarito
> Porque o modelo pode ser induzido; uma decisão determinística independente não depende do texto do contexto. [[Segurança de Agentes]].

**14.** Que padrão de alerta detecta o risco do triângulo em tempo de execução?
> [!success]- Gabarito
> Leitura de conteúdo externo seguida de ação sensível na mesma sessão. [[Monitoramento e Resposta]].

## Parte D — Medição (módulo 5)

**15.** 0 falhas em 100 tentativas prova que a taxa é menor que 3%?
> [!success]- Gabarito
> Não. A regra dos três dá ~3% de limite superior, mas o intervalo de Wilson a 95% dá ~3,7%; com 0 falhas, são necessários cerca de 125 testes para limite abaixo de 3%. [[Métricas e Critérios de Sucesso]].

**16.** Por que julgar sucesso por código (canário ou log de ferramenta) e não por opinião?
> [!success]- Gabarito
> É reprodutível e não depende do avaliador. [[Metodologia de Testes]].

**17.** Ao comparar duas configurações de defesa, que cuidado estatístico tomar?
> [!success]- Gabarito
> Mesmos casos e repetições, teste adequado (ex.: Fisher exato), correção por comparações múltiplas (Bonferroni) e relatar intervalos, não só taxas. [[Laboratório 05 - Avaliação Comparativa]].

**18.** O backend `mock` do kit serve para quê?
> [!success]- Gabarito
> Só para validar o kit e treinar leitura de saídas; **não é um modelo de linguagem**, e seus números não dizem nada sobre robustez real. [[Laboratório 01 - Comportamento de Recusa]].

## Parte E — Ética e escopo

**19.** Quais condições definem um teste aceitável neste curso?
> [!success]- Gabarito
> Alvo próprio ou autorizado, escopo escrito, dados fictícios, canários inofensivos, ferramentas simuladas e divulgação responsável. [[Metodologia de Testes]] · [[Planejamento de Avaliações]].

**20.** Um achado exige relato mesmo sem exploração dramática? O que ele deve conter?
> [!success]- Gabarito
> Sim, se há falha de controle. Deve ter reprodução, evidência, impacto, categoria (OWASP/ATLAS), mitigação e limitações. [[Relatório de Vulnerabilidades]] · [[OWASP para Aplicações de LLM]] · [[MITRE ATLAS]].

## Autoavaliação

| Parte | Acertos | Notas a rever |
|---|---|---|
| A | /5 | |
| B | /5 | |
| C | /4 | |
| D | /4 | |
| E | /2 | |

## Próximos passos
- [[Desafios Práticos]]
