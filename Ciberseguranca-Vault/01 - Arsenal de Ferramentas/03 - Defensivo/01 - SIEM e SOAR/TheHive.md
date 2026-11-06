---
titulo: "TheHive"
tipo: ferramenta
nome: "TheHive"
categoria: "Defensivo/SIEM-SOAR"
subcategoria: "Orquestração de Resposta a Incidentes (SOAR)"
plataformas: ["Linux", "Docker"]
licenca: "AGPL-3.0"
linguagem: "Scala"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://thehive-project.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/siem
  - arsenal-de-ferramentas
---

# TheHive

> Plataforma de gestão de casos e resposta a incidentes, frequentemente integrada a MISP e Cortex.

## Como funciona
Organiza o trabalho do SOC em 'casos', compostos por 'observáveis' (IOCs como IPs, hashes, domínios) e tarefas de investigação atribuíveis à equipe; integra-se ao motor de análise Cortex para enriquecer automaticamente observáveis (ex.: consultar reputação em VirusTotal) e ao MISP para importar/exportar indicadores de ameaça entre plataformas.

## Como usar
Cria-se um caso a partir de um alerta recebido (manual ou via integração com SIEM), adicionam-se observáveis extraídos do incidente e executam-se 'analyzers' do Cortex sobre eles para enriquecimento automático; tarefas são atribuídas à equipe e o caso é fechado com um resumo de resolução.

## Casos de uso
- Gestão centralizada de casos de resposta a incidentes (CSIRT/SOC)
- Enriquecimento automatizado de IOCs durante investigação

## Alternativas
[[MISP]]

## Categoria
[[MOC - SIEM e SOAR]]

## Link oficial
https://thehive-project.org/
