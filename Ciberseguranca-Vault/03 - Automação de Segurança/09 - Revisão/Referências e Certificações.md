---
titulo: "Referências e Certificações"
aliases: ["Certificações", "Leituras Recomendadas"]
tags:
  - ciberseguranca
  - automacao-de-seguranca
  - revisao
tipo: revisao
nivel: iniciante
relacionados:
  - "[[MOC - Revisão - Automação]]"
  - "[[Roteiro de Estudos de 8 Semanas]]"
  - "[[MOC - Automação de Segurança]]"
  - "[[Glossário#Cibersegurança]]"
---

# Referências e Certificações

## Objetivo
Indicar fontes primárias para aprofundamento e certificações coerentes com a trilha de automação de segurança. Mapa: [[MOC - Revisão - Automação]].

> [!warning] Verifique a situação atual
> Nomes de exames, versões, preços e URLs mudam com frequência. Confirme tudo nos sites oficiais antes de decidir. As referências abaixo são listadas por nome, sem links, e foram escolhidas por serem fontes de autoridade.

## Conceito
Priorize **fontes primárias** (padrões, documentação oficial, publicações de órgãos de referência) sobre resumos de terceiros. Organize o estudo conectando cada fonte às notas do vault.

### Frameworks e padrões
- **NIST Cybersecurity Framework 2.0** e publicações NIST SP 800 (por exemplo, SP 800-61 sobre resposta a incidentes): [[Framework NIST CSF]].
- **MITRE ATT&CK** e o ATT&CK Navigator: [[Framework MITRE ATT&CK]].
- **CIS Controls v8** e **CIS Benchmarks**: [[Framework CIS Controls]], [[Hardening com CIS Benchmarks]].
- **OWASP**: Top 10, ASVS, SAMM e DevSecOps Guideline: [[SAST]], [[DAST]].
- **FIRST**: CVSS e EPSS; **CISA**: catálogo KEV: [[Priorização com CVSS, EPSS e KEV]].
- **OASIS**: especificações STIX e TAXII: [[STIX e TAXII]].
- **SLSA e CycloneDX/SPDX** para cadeia de suprimentos: [[SBOM]], [[Segurança em Pipelines CI-CD]].
- **Sigma** (repositório de regras e especificação) e **YARA** (documentação oficial): [[Regras Sigma - Automação]], [[YARA - Automação]].
- **OWASP Top 10 para aplicações com LLM** e o **NIST AI RMF**: [[Riscos de IA em Segurança]].

### Legislação e orientações brasileiras
- Lei nº 13.709/2018 (LGPD) e regulamentos da **ANPD**, incluindo o de comunicação de incidentes.
- Lei nº 12.965/2014 (Marco Civil da Internet) e Lei nº 12.737/2012.
- Materiais do **CERT.br** e do **CTIR Gov**: [[Aspectos Legais e LGPD]].

### Documentação das ferramentas
Documentação oficial do seu SIEM, EDR e SOAR; do Open Policy Agent; do Terraform/OpenTofu; do MISP e do OpenCTI; de Sigma, YARA e OSV; dos provedores de nuvem (guias de segurança e benchmarks): [[Comparativo de Ferramentas - Automação]].

### Certificações
| Trilha | Exemplos | Relevância para o vault |
|---|---|---|
| Fundamentos | CompTIA Security+, ISC2 CC | Base conceitual |
| Operações de segurança | CompTIA CySA+, GIAC GCIA/GCIH/GCFA, Blue Team Level 1 | [[Triagem Automática de Alertas]], [[Playbook de Malware]] |
| Engenharia de detecção e SOC | GIAC GCDA, Splunk e Microsoft SC-200 | [[Detection as Code]], [[SIEM]] |
| Nuvem | AWS Security Specialty, Azure AZ-500, Google Professional Cloud Security Engineer | [[CSPM]] |
| DevSecOps | Certified DevSecOps Professional, GIAC GWEB e cursos de plataforma | [[Segurança em Pipelines CI-CD]] |
| Gestão e governança | CISSP, CISM, CRISC, ISO/IEC 27001 Lead Implementer | [[Governança da Automação]] |
| Privacidade | Exin PDPE, CIPP/E ou formações de encarregado | [[Aspectos Legais e LGPD]] |
| Automação e código | Certificações de Python, Terraform Associate | [[Infrastructure as Code]] |

Escolha pelo objetivo: operações (CySA+, GIAC), engenharia (nuvem e DevSecOps) ou gestão (CISSP, CISM).

## Exemplo prático
> [!example] Plano de certificação em 6 meses
> Meses 1 e 2: concluir este vault e o [[Roteiro de Estudos de 8 Semanas]]. Meses 3 a 5: estudar o conteúdo do exame escolhido, usando o vault como mapa e o [[Banco de Exercícios]] para prática. Mês 6: simulados e exame.

## Boas práticas
- Prefira laboratórios práticos próprios a apenas leitura de resumos.
- Cite fontes nas suas notas e registre a data de consulta.
- Releia as fontes primárias quando uma norma ou versão mudar.
- Participe de comunidades e eventos para acompanhar mudanças.

## Erros comuns
- Colecionar certificações sem aplicar o conteúdo.
- Estudar para o exame e esquecer a prática.
- Usar material desatualizado.
- Tratar blogs como fonte de verdade sobre leis.

## Para revisar
> [!question] Perguntas
> 1. Por que priorizar fontes primárias?
> 2. Que certificação se alinha melhor ao seu objetivo de carreira?
> 3. Que fonte você usaria para confirmar o prazo legal de comunicação de incidentes?

## Links relacionados
[[Flashcards - Automação]], [[Anti-Padrões de Automação de Segurança]], [[Glossário#Cibersegurança]].
