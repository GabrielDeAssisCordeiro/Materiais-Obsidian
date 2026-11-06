---
titulo: "theHarvester"
tipo: ferramenta
nome: "theHarvester"
categoria: "Ofensivo/Reconhecimento"
subcategoria: "OSINT Passivo"
plataformas: ["Linux", "macOS", "Windows"]
licenca: "GPLv2"
linguagem: "Python"
mitre_attack: ["T1596", "T1593"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/laramies/theHarvester"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/recon
  - arsenal-de-ferramentas
---

# theHarvester

> Coleta e-mails, subdomínios, IPs e nomes de funcionários a partir de fontes públicas.

## Como funciona
Consulta motores de busca (Bing, DuckDuckGo), APIs de terceiros (Shodan, Hunter.io, SecurityTrails) e registros DNS/certificados, agregando os resultados em uma única lista sem interagir diretamente com a infraestrutura do alvo. Por operar de forma passiva, não gera tráfego direto contra os ativos pesquisados, reduzindo o risco de detecção na fase de reconhecimento.

## Como usar
Executa-se informando o domínio alvo (`-d`), as fontes a consultar (`-b all` ou uma fonte específica) e o limite de resultados (`-l`). As chaves de API de serviços pagos são configuradas em um arquivo YAML de configuração; sem elas, apenas fontes gratuitas respondem. A saída pode ser exportada em XML/JSON para alimentar outras ferramentas do fluxo de recon.

## Casos de uso
- Levantamento inicial de superfície de ataque
- Enumeração de e-mails para campanhas de engenharia social autorizadas

## Alternativas
[[Amass]] · [[Recon-ng]] · [[SpiderFoot]]

## Categoria
[[MOC - Reconhecimento]]

## Link oficial
https://github.com/laramies/theHarvester
