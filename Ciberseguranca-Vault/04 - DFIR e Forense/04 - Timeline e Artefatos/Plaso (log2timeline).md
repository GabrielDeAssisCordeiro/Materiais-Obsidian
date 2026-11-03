---
titulo: "Plaso (log2timeline)"
tipo: ferramenta
nome: "Plaso (log2timeline)"
categoria: "DFIR/Timeline-e-Artefatos"
subcategoria: "Geração de Super-Timeline Forense"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "Python"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://plaso.readthedocs.io/"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/timeline
---

# Plaso (log2timeline)

> Framework que extrai eventos com timestamp de dezenas de fontes forenses e os unifica em uma única timeline.

## Como funciona
Aplica 'parsers' específicos a cada tipo de artefato suportado (registro do Windows, logs de evento, histórico de navegador, metadados de sistema de arquivos) extraindo todo evento com timestamp associado, e consolida tudo isso em um único arquivo de armazenamento ordenado cronologicamente — a chamada 'super-timeline' — permitindo correlacionar atividades de fontes completamente diferentes na mesma linha do tempo.

## Como usar
`log2timeline.py saida.plaso /caminho/imagem_montada` processa a evidência gerando o arquivo de armazenamento; em seguida, `psort.py -o l2tcsv -w timeline.csv saida.plaso` exporta a timeline final em formato legível (CSV), filtrável por data/hora de interesse.

## Casos de uso
- Reconstrução cronológica completa de atividade em um sistema comprometido
- Correlação de eventos de múltiplas fontes forenses na mesma timeline

## Alternativas
[[KAPE]] · [[Timesketch]]

## Categoria
[[MOC - Timeline e Artefatos]]

## Link oficial
https://plaso.readthedocs.io/
