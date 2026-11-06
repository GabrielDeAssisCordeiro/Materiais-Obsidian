---
titulo: "Maltego"
tipo: ferramenta
nome: "Maltego"
categoria: "Ofensivo/Reconhecimento"
subcategoria: "Análise de Relacionamento OSINT"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Comercial (Community limitada)"
linguagem: "Java"
mitre_attack: ["T1593"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.maltego.com/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/recon
  - arsenal-de-ferramentas
---

# Maltego

> Visualização gráfica de relacionamentos entre entidades (pessoas, domínios, IPs, empresas) via transforms.

## Como funciona
Funciona com o conceito de 'entidades' (um domínio, um e-mail, uma pessoa) e 'transforms' — pequenos scripts/integrações que consultam uma fonte de dados (DNS, redes sociais, registros públicos, APIs comerciais) e retornam novas entidades relacionadas à original. Cada execução de transform expande o grafo, revelando conexões não óbvias entre infraestrutura e pessoas de uma organização.

## Como usar
Cria-se um novo grafo, arrasta-se uma entidade semente (ex.: domínio) para o canvas e clica-se com o botão direito para rodar transforms disponíveis (locais ou do Transform Hub). O resultado é um grafo interativo que pode ser reorganizado, filtrado por tipo de entidade e exportado como relatório visual.

## Casos de uso
- Mapeamento de relações organizacionais para engenharia social autorizada
- Correlação de infraestrutura entre domínios relacionados

## Alternativas
[[Recon-ng]] · [[SpiderFoot]]

## Categoria
[[MOC - Reconhecimento]]

## Link oficial
https://www.maltego.com/
