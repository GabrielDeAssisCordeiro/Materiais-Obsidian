---
titulo: "Framework NIST CSF"
aliases: []
tags:
  - automacao-seguranca
  - conceito
  - fundamentos
tipo: conceito
nivel: intermediario
relacionados:
  - "[[MOC - Fundamentos - Automação]]"
  - "[[Framework MITRE ATT&CK]]"
  - "[[Framework CIS Controls]]"
  - "[[Compliance as Code]]"
---

# Framework NIST CSF

## Objetivo
Usar o NIST Cybersecurity Framework como espinha dorsal para organizar e priorizar automações de segurança. Mapa: [[MOC - Fundamentos - Automação]].

## Conceito
O NIST CSF é um framework voluntário que descreve resultados de segurança em funções de alto nível. A versão 2.0 organiza-se em seis funções:

- **Govern (GV):** estratégia, papéis, políticas e gestão de risco da cadeia de suprimentos.
- **Identify (ID):** inventário de ativos, avaliação de riscos e melhoria.
- **Protect (PR):** controle de acesso, treinamento, proteção de dados e plataforma.
- **Detect (DE):** monitoramento contínuo e análise de eventos adversos.
- **Respond (RS):** gestão de incidentes, análise, comunicação e mitigação.
- **Recover (RC):** execução do plano de recuperação e comunicação.

A utilidade para automação é mapear cada fluxo a um resultado esperado. Isso evidencia lacunas e justifica investimento para a diretoria.

| Função | Exemplos de automação | Notas |
|---|---|---|
| Govern | Evidências de política, relatórios | [[Governança da Automação]] |
| Identify | Descoberta de ativos, varredura | [[Inventário de Ativos]], [[Varredura Contínua de Vulnerabilidades]] |
| Protect | Hardening, rotação de segredos | [[Hardening com CIS Benchmarks]], [[Gestão de Segredos]] |
| Detect | Regras, caça, correlação | [[SIEM]], [[Regras Sigma - Automação]] |
| Respond | Playbooks, contenção | [[Contenção Automatizada]] |
| Recover | Restauração e verificação | [[Rollback]] |

```mermaid
flowchart LR
    GV[Govern] --- ID[Identify]
    ID --> PR[Protect] --> DE[Detect] --> RS[Respond] --> RC[Recover]
    RC --> ID
```

## Exemplo prático
> [!example] Mapa de cobertura
> Uma equipe lista suas 30 automações e as classifica por função. O resultado mostra 18 em Detect e Respond, 2 em Recover e nenhuma em Govern. O plano passa a incluir coleta automática de evidências de conformidade ([[Compliance as Code]]) e testes periódicos de restauração.

## Boas práticas
- Use os Perfis (atual e alvo) para definir o roteiro de melhoria.
- Associe cada automação a uma categoria do framework no frontmatter ou em tags.
- Combine com o [[Framework MITRE ATT&CK]] para cobertura de técnicas e com o [[Framework CIS Controls]] para medidas concretas.
- Revise o mapeamento sempre que houver nova ferramenta.

## Erros comuns
- Tratar o CSF como checklist de certificação; ele descreve resultados, não exige produtos.
- Concentrar toda automação em Detect e Respond, esquecendo Identify e Recover.
- Não ter dono para a função Govern.

> [!tip] Comunicação
> O CSF fornece vocabulário comum para conversar com gestão e auditoria sem entrar em detalhes técnicos.

## Para revisar
> [!question] Perguntas
> 1. Quais são as seis funções do CSF 2.0?
> 2. Qual função foi adicionada na versão 2.0?
> 3. Como o CSF ajuda a revelar lacunas de automação?
> 4. Qual a diferença entre perfil atual e perfil alvo?

## Links relacionados
[[Framework MITRE ATT&CK]], [[Framework CIS Controls]], [[Níveis de Maturidade da Automação]], [[Auditoria Contínua]].
