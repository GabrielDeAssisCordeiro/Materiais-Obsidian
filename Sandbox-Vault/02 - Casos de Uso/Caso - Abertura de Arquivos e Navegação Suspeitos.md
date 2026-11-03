---
tags:
  - casos-de-uso
aliases:
  - "Arquivos suspeitos"
  - "Navegação isolada"
tipo: caso-de-uso
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Aplicação]]"
  - "[[Caso - Análise de Malware]]"
---
# Caso - Abertura de Arquivos e Navegação Suspeitos

Anexos de e-mail, PDFs, documentos do Office e links duvidosos podem explorar falhas do leitor ou induzir execução de macros.

| Opção | Quando usar |
|---|---|
| Windows Sandbox | Abrir arquivo no Windows rapidamente, ambiente descartável |
| VM descartável | Análise mais demorada |
| Navegador em container/isolamento remoto | Links suspeitos |
| Conversão para formato seguro | PDF → imagens, desarmar conteúdo ativo |

> [!tip] Desative pastas compartilhadas e área de transferência
> Copie o arquivo para dentro, nunca o contrário. Veja [[Fuga de Sandbox]] para riscos de integração.

## Exercício

Configure uma Windows Sandbox (ou VM) sem pasta compartilhada e abra nela um arquivo de teste inofensivo.

## Veja também

- [[Sandbox de Aplicação]]
- [[Criar Sandbox com Windows Sandbox]]
- [[Fuga de Sandbox]]
- [[MOC - Casos de Uso]]
