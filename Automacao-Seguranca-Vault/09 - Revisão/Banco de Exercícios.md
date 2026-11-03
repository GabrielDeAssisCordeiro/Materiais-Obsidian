---
titulo: "Banco de Exercícios"
aliases: ["Questões de Prática"]
tags:
  - automacao-seguranca
  - revisao
tipo: revisao
nivel: intermediario
relacionados:
  - "[[MOC - Revisão - Automação]]"
  - "[[Flashcards - Automação]]"
  - "[[Roteiro de Estudos de 8 Semanas]]"
  - "[[Laboratório Guiado]]"
---

# Banco de Exercícios

## Objetivo
Oferecer exercícios conceituais, de projeto e práticos que consolidam o conteúdo do vault, organizados por tema e nível. Mapa: [[MOC - Revisão - Automação]].

## Conceito
Os exercícios exigem **aplicar** o conhecimento: decidir, projetar, escrever e criticar. Responda por escrito antes de consultar as notas indicadas. Os de laboratório devem ser feitos apenas em ambiente próprio e autorizado, com dados sintéticos. Os itens marcados com ⭐ são mais difíceis. Para cartões de memorização, veja os [[Flashcards - Automação]].

### Fundamentos
1. Liste dez tarefas do seu dia de segurança e classifique cada uma (automatizar, semiautomatizar, manter manual) com os critérios de [[O que Automatizar e o que Não Automatizar]].
2. Calcule o ROI de uma automação que economiza 80 horas por mês a R$ 100/h, com custo mensal de R$ 5.000 ([[Métricas - MTTD, MTTR, Falso Positivo e ROI]]).
3. Avalie a maturidade de três processos da sua organização usando [[Níveis de Maturidade da Automação]] e proponha o próximo passo de cada um.
4. ⭐ Monte um mapa das suas automações por função do [[Framework NIST CSF]] e identifique as lacunas.

### Arquitetura
5. Desenhe o fluxo de um alerta do SIEM até um caso no SOAR, incluindo validação do webhook e fila ([[Webhooks, Filas e Integrações]]).
6. Liste cinco ações de API de um EDR e classifique-as por impacto e reversibilidade ([[EDR e XDR]]).
7. Escreva a política de uso de segredos para uma automação de bloqueio ([[Gestão de Segredos]]).
8. ⭐ Compare duas ferramentas de SOAR (uma aberta e uma comercial) com uma matriz ponderada ([[Comparativo de Ferramentas - Automação]]).

### SOC e resposta
9. Escreva um runbook de 8 passos para bloquear um IP malicioso, com verificação e reversão ([[Runbooks]]).
10. Defina um escore de triagem com quatro fatores e pesos, justificando-os ([[Triagem Automática de Alertas]]).
11. Projete a escada de contenção para uma conta comprometida de gestor financeiro ([[Playbook de Conta Comprometida]]).
12. ⭐ Redija o pedido de aprovação ideal para isolar um servidor crítico ([[Human in the Loop - Automação]]).

### Vulnerabilidades e compliance
13. Dadas cinco vulnerabilidades fictícias com CVSS, EPSS, KEV e exposição, ordene-as e justifique ([[Priorização com CVSS, EPSS e KEV]]).
14. Descreva um plano de patch em três ondas para 300 servidores ([[Patch Management Automatizado]]).
15. Traduza o requisito "todo disco deve ser criptografado" em uma regra verificável ([[Compliance as Code]]).
16. ⭐ Projete a coleta de evidências para três controles de acesso ([[Auditoria Contínua]]).

### DevSecOps
17. Monte um pipeline com secret scanning, SAST, SCA, scan de imagem e SBOM, indicando onde falhar o build ([[Segurança em Pipelines CI-CD]]).
18. Escreva uma política Rego que negue contêineres sem `runAsNonRoot` ([[Políticas como Código com OPA]]).
19. ⭐ Explique como um SBOM acelera a resposta a uma biblioteca com falha crítica ([[SBOM]]).

### Threat intel e detecção
20. Defina critérios de expiração para IPs, domínios, URLs e hashes ([[Feeds de Inteligência de Ameaças]]).
21. Escreva uma regra Sigma que detecte muitas falhas de autenticação seguidas de sucesso, com falsos positivos documentados ([[Regras Sigma - Automação]]).
22. Crie logs positivos e negativos para testar a regra anterior ([[Testes de Detecção]]).
23. ⭐ Planeje uma emulação autorizada de três técnicas, com critérios de sucesso e limpeza ([[Emulação de Adversário para Validação Defensiva]]).

### Laboratórios
24. Estenda o [[Lab - Parsing de Logs]] para detectar sucesso após falhas do mesmo IP.
25. Adicione ao [[Lab - Bloqueio Automatizado]] um arquivo de auditoria e um desfazer em lote.
26. ⭐ Escreva testes automatizados para `pode_bloquear`, cobrindo IPv6, privados e valores inválidos.

### IA, governança e legal
27. Liste riscos de usar um LLM para resumir e-mails reportados e proponha uma mitigação para cada ([[Riscos de IA em Segurança]]).
28. Preencha o registro de governança de uma automação sua ([[Governança da Automação]]).
29. Identifique conflitos de função no seu processo de implantação de playbooks ([[Segregação de Funções]]).
30. ⭐ Mapeie, num incidente com dados pessoais, as decisões do jurídico, do encarregado e do SOC ([[Aspectos Legais e LGPD]]).

## Exemplo prático
> [!example] Resolução do exercício 2
> Benefício: 80 × 100 = R$ 8.000. ROI = (8.000 - 5.000) / 5.000 = 0,6, ou 60%. Interprete: cada real investido retorna R$ 0,60 além do custo, sem contar o risco evitado.

## Boas práticas
- Responda por escrito e depois compare com as notas.
- Registre as respostas em notas pessoais ligadas ao exercício.
- Repita os difíceis após uma semana.
- Use um colega para revisar respostas de projeto.

## Erros comuns
- Consultar a nota antes de tentar.
- Dar respostas genéricas, sem critérios nem números.
- Executar laboratórios fora de ambiente autorizado.

## Para revisar
> [!question] Perguntas
> 1. Quais exercícios revelaram lacunas no seu conhecimento?
> 2. Que nota você precisa reler?
> 3. Que exercício poderia virar um projeto real na sua equipe?

## Links relacionados
[[Home - Automação]], [[Glossário#Automação de Segurança]], [[Referências e Certificações]], [[Convenções - Automação]].
