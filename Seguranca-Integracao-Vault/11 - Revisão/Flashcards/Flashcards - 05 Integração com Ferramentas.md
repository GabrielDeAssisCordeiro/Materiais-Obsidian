---
titulo: "Flashcards - 05 Integração com Ferramentas"
aliases: ["Flashcards 05"]
tags:
  - integracao-seguranca
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Integração com SIEM - Splunk Elastic e Wazuh]]"
  - "[[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]]"
  - "[[Integração com Gestão de Segredos - Vault e gitleaks]]"
---

# Flashcards - 05 Integração com Ferramentas

## Resumo

Cartões de revisão do módulo **Integração com Ferramentas**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Integração com SIEM - Splunk Elastic e Wazuh]], [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]], [[Integração com Gestão de Segredos - Vault e gitleaks]], [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]].

## Como funciona

Instale o plugin Spaced Repetition e use *Review flashcards*. O algoritmo agenda a próxima revisão conforme sua avaliação (fácil, bom, difícil).

## Exemplo prático

Responda mentalmente antes de virar o cartão. Se errar, releia a nota de origem e reformule o cartão com suas palavras.

## Boas práticas

- Revise um pouco todos os dias.
- Crie cartões próprios para pontos que você errou.
- Mantenha respostas curtas.

## Erros comuns

- Decorar sem entender a razão.
- Acumular revisões atrasadas.
- Cartões longos demais.

## Referências para aprofundar

Plugin Spaced Repetition para Obsidian; veja [[Como usar este vault - Integração]].

## Flashcards

#flashcards

Qual o cabeçalho de autenticação do Splunk HEC?::Authorization: Splunk <token>, no endpoint /services/collector/event.
O que observar na resposta do _bulk do Elasticsearch?::Pode vir 200 com errors true; é preciso inspecionar os itens.
Como tratar Vulnerabilities nulo no JSON do Trivy?::Como lista vazia.
Por que usar --redact no gitleaks?::Para que os relatórios não reproduzam o valor do segredo.
O que fazer quando um segredo vaza?::Revogar e rotacionar; apagar o commit não invalida a credencial.
O que é o AppRole do Vault?::Autenticação para aplicações com role_id e secret_id de curta duração.
Como evitar tickets duplicados no Jira?::Chave de deduplicação determinística em label ou campo, ou registro local.
Como o Teams recebe notificações atualmente?::Por Workflows (Power Automate) com Adaptive Cards, pois conectores antigos foram descontinuados; confira a documentação.
Por que evitar enviar arquivos ao VirusTotal?::Uploads ficam acessíveis a terceiros; prefira consultar por hash.
Como lidar com a cota do VirusTotal?::Usar cache com TTL e rate limiting no cliente.
Qual a diferença entre MISP e OpenCTI?::MISP compartilha IoCs e eventos; OpenCTI organiza inteligência em grafo baseado em STIX 2.1.

## Veja também

- [[Integração com SIEM - Splunk Elastic e Wazuh]]
- [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]]
- [[Integração com Gestão de Segredos - Vault e gitleaks]]
- [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]]
- [[MOC - Revisão - Integração]]
- [[Como usar este vault - Integração]]

#flashcards #seguranca/revisao/flashcards
