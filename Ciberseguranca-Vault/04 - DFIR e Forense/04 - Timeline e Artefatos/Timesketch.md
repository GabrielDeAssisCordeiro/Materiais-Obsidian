---
titulo: "Timesketch"
tipo: ferramenta
nome: "Timesketch"
categoria: "DFIR/Timeline-e-Artefatos"
subcategoria: "Análise Colaborativa de Timeline"
plataformas: ["Linux", "Docker"]
licenca: "Apache-2.0"
linguagem: "Python"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://timesketch.org/"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/timeline
---

# Timesketch

> Plataforma colaborativa para explorar e anotar super-timelines forenses (tipicamente geradas pelo Plaso).

## Como funciona
Importa timelines geradas por ferramentas como o Plaso para um backend Elasticsearch, permitindo que múltiplos investigadores explorem simultaneamente os mesmos eventos através de busca full-text, filtros temporais e anotações compartilhadas ('sketches'), com suporte a 'analyzers' automáticos que sinalizam padrões suspeitos conhecidos na timeline.

## Como usar
Cria-se um 'Sketch' e importa-se a timeline (arquivo Plaso ou CSV); a partir da interface web, buscas e filtros isolam o período/evento de interesse, e eventos relevantes podem ser marcados com tags e comentários compartilhados entre a equipe de investigação.

## Casos de uso
- Investigação colaborativa de timeline entre múltiplos analistas
- Correlação visual de grandes volumes de eventos temporais

## Alternativas
[[Plaso (log2timeline)]]

## Categoria
[[MOC - Timeline e Artefatos]]

## Link oficial
https://timesketch.org/
