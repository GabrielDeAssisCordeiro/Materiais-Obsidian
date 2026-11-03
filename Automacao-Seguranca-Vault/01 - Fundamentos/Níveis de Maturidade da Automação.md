---
titulo: "Níveis de Maturidade da Automação"
aliases: ["Maturidade", "Modelo de Maturidade"]
tags:
  - automacao-seguranca
  - conceito
  - fundamentos
tipo: conceito
nivel: intermediario
relacionados:
  - "[[MOC - Fundamentos - Automação]]"
  - "[[Ciclo de Vida da Automação]]"
  - "[[Métricas - MTTD, MTTR, Falso Positivo e ROI]]"
  - "[[SOAR]]"
---

# Níveis de Maturidade da Automação

## Objetivo
Avaliar o estágio atual da automação de segurança da organização e definir a próxima evolução realista. Mapa: [[MOC - Fundamentos - Automação]].

## Conceito
Um modelo de maturidade descreve a progressão de processos ad hoc até operação orquestrada, medida e otimizada. Não é competição: o nível adequado depende do risco e do tamanho da equipe. Este vault usa cinco níveis.

| Nível | Nome | Características |
|---|---|---|
| 1 | Manual | Tudo por humanos, conhecimento tácito, sem registro padronizado |
| 2 | Scripts isolados | Scripts individuais, sem versionamento nem dono claro |
| 3 | Padronizado | [[Runbooks]] documentados, repositório Git, ações com aprovação |
| 4 | Orquestrado | [[SOAR]] integrado a [[SIEM]], [[EDR e XDR]] e tickets, métricas contínuas |
| 5 | Adaptativo | Automação guiada por dados, testes contínuos, feedback automático para detecção |

```mermaid
flowchart LR
    N1[1 Manual] --> N2[2 Scripts] --> N3[3 Padronizado] --> N4[4 Orquestrado] --> N5[5 Adaptativo]
```

**Como avaliar:** para cada processo (triagem, vulnerabilidades, resposta, conformidade), classifique o nível. É comum estar no nível 4 em enriquecimento e no nível 2 em resposta a incidentes. O mapa de calor resultante orienta prioridades.

## Exemplo prático
> [!example] Autoavaliação
> Uma equipe constata: triagem de phishing em nível 4 (playbook no SOAR), gestão de vulnerabilidades em nível 2 (scripts do analista), conformidade em nível 1 (planilhas). A prioridade é levar vulnerabilidades ao nível 3, com repositório e [[Priorização com CVSS, EPSS e KEV]] padronizada, antes de comprar nova ferramenta.

## Boas práticas
- Suba um nível por vez; saltar etapas gera automações frágeis.
- Atrele cada transição a métricas ([[Métricas - MTTD, MTTR, Falso Positivo e ROI]]).
- Padronize antes de orquestrar: ferramenta cara sobre processo caótico não resolve.
- Reavalie semestralmente e relacione ao [[Framework NIST CSF]].

## Erros comuns
- Comprar plataforma SOAR no nível 1, sem processos documentados.
- Perseguir o nível 5 sem dados confiáveis para alimentá-lo.
- Medir maturidade apenas por quantidade de playbooks, e não por qualidade e resultado.
- Ignorar a manutenção: playbooks envelhecem.

> [!tip] Foco
> Maturidade alta em tudo é raro e desnecessário. Concentre-se onde o risco é maior.

## Para revisar
> [!question] Perguntas
> 1. Quais as diferenças entre os níveis 2 e 3?
> 2. Por que não se deve saltar níveis?
> 3. Como a maturidade pode variar entre processos da mesma equipe?
> 4. Que métrica evidenciaria a passagem do nível 3 ao 4?

## Links relacionados
[[Ciclo de Vida da Automação]], [[Por que Automatizar Segurança]], [[Comparativo de Ferramentas - Automação]], [[Governança da Automação]].
