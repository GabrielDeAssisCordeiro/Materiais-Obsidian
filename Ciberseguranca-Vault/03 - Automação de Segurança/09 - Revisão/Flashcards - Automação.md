---
titulo: "Flashcards - Automação"
aliases: ["Spaced Repetition"]
tags:
  - ciberseguranca
  - automacao-de-seguranca
  - revisao
  - flashcards
tipo: revisao
nivel: iniciante
relacionados:
  - "[[MOC - Revisão - Automação]]"
  - "[[Glossário#Cibersegurança]]"
  - "[[Banco de Exercícios]]"
  - "[[Template de Flashcard - Automação]]"
---

# Flashcards - Automação

## Objetivo
Fixar conceitos centrais por recordação ativa e repetição espaçada, usando cartões de uma linha no formato `pergunta::resposta`, compatível com o plugin Spaced Repetition do Obsidian. Mapa: [[MOC - Revisão - Automação]].

## Conceito
A recordação ativa (tentar lembrar antes de ver a resposta) e a repetição espaçada (revisar em intervalos crescentes) são as técnicas de estudo com melhor evidência. Cada cartão testa **um fato**. Para criar novos cartões, use o [[Template de Flashcard - Automação]]. Para definições formais, consulte o [[Glossário#Cibersegurança]].

Para ativar, instale o plugin Spaced Repetition e adicione a tag `#flashcards` às notas desejadas; este arquivo já a possui.

### Fundamentos
Quais os quatro vetores de motivação para automatizar segurança?::Volume e velocidade, escassez de profissionais, consistência e redução do tempo de exposição.
Que critérios guiam a decisão de automatizar uma tarefa?::Frequência, previsibilidade, impacto do erro e reversibilidade.
O que é o modo "somente recomendar"?::Fase em que a automação sugere a ação, mas não a executa, até medir os falsos positivos.
Quais as fases do ciclo de vida da automação?::Identificar, documentar, projetar, desenvolver, testar, implantar, monitorar, revisar e aposentar.
Qual o primeiro passo antes de automatizar um processo?::Documentá-lo como runbook.
O que significa MTTD?::Tempo médio entre o início do evento malicioso e sua detecção.
Como se calcula a taxa de falso positivo?::FP / (FP + TP) entre os alertas fechados.
Como se calcula o ROI?::(benefício - custo) / custo.
Por que usar mediana e P90 além da média?::Porque outliers distorcem a média.
Quais as seis funções do NIST CSF 2.0?::Govern, Identify, Protect, Detect, Respond e Recover.
O que são IG1, IG2 e IG3 nos CIS Controls?::Grupos de implementação que escalam conforme porte e maturidade; IG1 é a higiene básica.
Qual a diferença entre tática e técnica no ATT&CK?::Tática é o objetivo do adversário; técnica é como ele o alcança.

### Arquitetura
O que o SIEM faz?::Coleta, normaliza, correlaciona e alerta sobre eventos de várias fontes.
O que é um playbook de SOAR?::Fluxo automatizado com ações, condições e tratamento de erro.
Qual a diferença entre EDR e CSPM?::EDR observa comportamento em endpoints; CSPM avalia configuração em nuvem via API.
Para que serve a fila de mensagens mortas (DLQ)?::Reter eventos que falharam repetidamente, para análise.
Como validar a autenticidade de um webhook?::Verificando a assinatura HMAC do corpo da requisição.
O que é idempotência?::Propriedade de uma operação que, repetida, não gera efeito adicional.
O que é deriva (drift) em IaC?::Divergência entre o estado real e o estado declarado no código.
Por que apagar um segredo do Git não basta?::Porque o histórico o preserva; é preciso revogar e rotacionar.
Qual a melhor forma de autenticar uma automação sem guardar outro segredo?::Usar identidade de carga de trabalho com tokens de curta duração.

### SOC e resposta
Quais as etapas da triagem automática?::Normalizar, deduplicar, enriquecer, pontuar e rotear.
Por que o escore de triagem deve ser explicável?::Para o analista auditar e ajustar a decisão.
"Sem evidência" equivale a "benigno"?::Não; significa apenas que nenhuma fonte tinha informação.
O que fazer após clique em phishing?::Acionar o playbook de conta comprometida para as pessoas afetadas.
Por que revogar tokens além da senha?::Porque sessões e tokens de atualização podem continuar válidos.
O que é proporcionalidade na contenção?::Ações mais drásticas exigem mais confiança e mais aprovação.
Para que serve o TTL em um bloqueio?::Fazer o bloqueio expirar sozinho, exigindo renovação explícita.
O que é um kill switch?::Interruptor que pausa todas as ações automáticas.
Diferencie in-the-loop e on-the-loop.::No in-the-loop o humano aprova cada ação; no on-the-loop ele supervisiona e pode intervir.
O que deve acontecer se uma aprovação expirar sem resposta?::Escalar ou não agir, nunca executar por padrão.

### Vulnerabilidades e compliance
O que o CVSS mede?::A severidade técnica, sem considerar probabilidade nem contexto.
O que é o EPSS?::Estimativa da probabilidade de exploração nos próximos 30 dias.
O que indica a presença de uma falha no KEV?::Exploração comprovada na prática.
Por que implantar patches em ondas?::Para limitar o impacto de falhas e permitir parar cedo.
O que é compliance as code?::Traduzir requisitos em verificações executáveis, versionadas e geradoras de evidência.
Como tratar "sem evidência" na auditoria contínua?::Como desvio, nunca como conformidade.
Qual a diferença entre CIS Controls e CIS Benchmarks?::Controls são práticas de alto nível; Benchmarks são guias de configuração por tecnologia.
Por que o inventário de ativos vem primeiro?::Porque não se protege o que não se conhece.

### DevSecOps
O que é taint analysis?::Rastrear dados não confiáveis das fontes até operações perigosas.
Que classe de falha o DAST encontra melhor que o SAST?::Problemas de configuração e comportamento em tempo de execução.
O que são dependências transitivas?::Pacotes trazidos por outras dependências.
Quais os dois formatos principais de SBOM?::CycloneDX e SPDX.
Para que serve o VEX?::Indicar se uma vulnerabilidade afeta de fato o produto.
Por que fixar ações de CI por hash?::Porque tags são mutáveis e executam código de terceiros no pipeline.
O que é fail-closed em uma política?::Negar por padrão quando o motor de políticas está indisponível.
O que significa shift left?::Antecipar atividades de segurança para as fases iniciais do desenvolvimento.

### Threat intel e detecção
Quais os quatro níveis de inteligência de ameaças?::Estratégico, operacional, tático e técnico.
Qual a diferença entre STIX e TAXII?::STIX é o formato; TAXII é o protocolo de transporte.
O que significa a flag to_ids no MISP?::Que o atributo é adequado para detecção automática.
O que é Sigma?::Formato aberto, em YAML, para regras de detecção sobre logs.
Por que preferir comportamento a valores fixos em regras?::Valores fixos são facilmente alterados pelo adversário.
Quais as três seções de uma regra YARA?::meta, strings e condition.
Quais as três camadas de teste de detecção?::Unitário da regra, integração do pipeline de log e validação com emulação autorizada.
Que três perguntas se faz a cada técnica emulada?::Houve telemetria? Houve alerta? Houve resposta?
Por que uma caça sem achados ainda tem valor?::Documenta cobertura e pode revelar falta de telemetria.

### IA, governança e legal
Em que tarefas os LLMs são mais confiáveis em segurança?::Resumo, classificação, extração e explicação, sempre com validação.
O que é prompt injection indireta?::Instruções maliciosas contidas em dados externos que o modelo processa.
Delimitadores bastam contra prompt injection?::Não; as barreiras reais são privilégio mínimo, validação e aprovação.
O que é o princípio dos quatro olhos?::Quem propõe uma ação não é quem a aprova.
O que registrar na trilha de auditoria?::Quem, o quê, quando, por quê, resultado e identificador de correlação.
Como detectar adulteração na trilha?::Encadeando hashes ou usando armazenamento imutável.
Que ações são irreversíveis e não devem ser automatizadas?::Exclusão de dados e desligamento definitivo de sistemas.
O que diz o art. 20 da LGPD?::O titular pode pedir revisão de decisões baseadas unicamente em tratamento automatizado.
Pseudonimização equivale a anonimização?::Não; o dado continua pessoal se a reidentificação for possível.

## Exemplo prático
> [!example] Rotina de revisão
> Revise 15 cartões por dia: leia a pergunta, responda em voz alta, confira, e marque como fácil ou difícil. Cartões difíceis voltam em 1 dia; fáceis, em 4 dias ou mais.

## Boas práticas
- Faça sessões curtas e diárias em vez de maratonas.
- Escreva seus próprios cartões a partir das perguntas "Para revisar" de cada nota.
- Reformule cartões que você acerta sem pensar, tornando-os mais exigentes.
- Combine com o [[Roteiro de Estudos de 8 Semanas]].

## Erros comuns
- Cartões com várias ideias, que não permitem avaliação objetiva.
- Ler a resposta sem tentar lembrar antes.
- Acumular revisões atrasadas até desistir.

## Para revisar
> [!question] Perguntas
> 1. Por que cada cartão deve testar um único fato?
> 2. Qual a diferença entre reconhecimento e recordação ativa?
> 3. Que ajuste fazer em cartões fáceis demais?

## Links relacionados
[[MOC - Automação de Segurança]], [[Referências e Certificações]], [[Glossário#Cibersegurança]].
