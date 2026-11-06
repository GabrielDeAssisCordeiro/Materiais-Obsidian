---
titulo: "PowerSploit"
tipo: ferramenta
nome: "PowerSploit"
categoria: "Ofensivo/Pos-Exploracao"
subcategoria: "Módulos PowerShell Ofensivos"
plataformas: ["Windows"]
licenca: "BSD-3-Clause"
linguagem: "PowerShell"
mitre_attack: ["T1059.001"]
nivel: avancado
situacao: legado
link_oficial: "https://github.com/PowerShellMafia/PowerSploit"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/pos-exploracao
  - arsenal-de-ferramentas
---

# PowerSploit

> Coleção de módulos PowerShell para reconhecimento, escalonamento de privilégio e persistência.

## Como funciona
Implementa funcionalidades ofensivas diretamente em PowerShell, aproveitando-se do fato de que o PowerShell é nativo do Windows e tem acesso amplo ao .NET Framework; muitos módulos carregam código refletido em memória (reflective loading), evitando gravar binários em disco e dificultando detecção baseada em assinatura de arquivo.

## Como usar
Carrega-se o módulo com `Import-Module .\PowerSploit.psd1` e invocam-se funções específicas, como `Invoke-Mimikatz` (porta do Mimikatz para PowerShell) ou módulos de reconhecimento (`PowerView`) e persistência (`Persistence`). Por ser um projeto descontinuado, muitas assinaturas de antivírus/EDR já o detectam amplamente.

## Casos de uso
- Pós-exploração living-off-the-land em ambientes Windows
- Testes de detecção de uso malicioso de PowerShell (purple team)

## Alternativas
[[Empire]] · [[Mimikatz]]

## Categoria
[[MOC - Pós-Exploração]]

## Link oficial
https://github.com/PowerShellMafia/PowerSploit
