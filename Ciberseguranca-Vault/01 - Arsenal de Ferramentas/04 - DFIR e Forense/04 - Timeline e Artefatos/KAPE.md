---
titulo: "KAPE"
tipo: ferramenta
nome: "KAPE"
categoria: "DFIR/Timeline-e-Artefatos"
subcategoria: "Coleta Direcionada de Artefatos (Windows)"
plataformas: ["Windows"]
licenca: "Gratuito (uso não-comercial)"
linguagem: "C#"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/timeline
  - arsenal-de-ferramentas
---

# KAPE

> Ferramenta de coleta e processamento rápido de artefatos forenses direcionados em sistemas Windows.

## Como funciona
Em vez de criar uma imagem forense completa do disco (processo lento), copia seletivamente apenas os artefatos forenses relevantes já conhecidos (registro, logs de evento, arquivos de prefetch, histórico de navegador) usando 'targets' pré-definidos, e opcionalmente já executa 'modules' que processam esses artefatos coletados (parsers) automaticamente na mesma execução.

## Como usar
`kape.exe --tsource C: --tdest saida --target KapeTriage` coleta o conjunto padrão de artefatos de triagem de um disco; a flag `--module` pode ser combinada para já parsear os artefatos coletados (ex.: com Plaso/EZ Tools) imediatamente após a coleta.

## Casos de uso
- Resposta rápida a incidente com coleta seletiva de artefatos
- Triagem forense em larga escala sem necessidade de imagem completa

## Alternativas
[[Plaso (log2timeline)]]

## Categoria
[[MOC - Timeline e Artefatos]]

## Link oficial
https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape
