---
titulo: "Mimikatz"
tipo: ferramenta
nome: "Mimikatz"
categoria: "Ofensivo/Pos-Exploracao"
subcategoria: "Extração de Credenciais"
plataformas: ["Windows"]
licenca: "CC BY 4.0"
linguagem: "C"
mitre_attack: ["T1003.001"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/gentilkiwi/mimikatz"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/pos-exploracao
  - arsenal-de-ferramentas
---

# Mimikatz

> Extrai credenciais em texto claro, hashes e tickets Kerberos da memória do LSASS.

## Como funciona
Explora o fato de que o processo LSASS (Local Security Authority Subsystem Service) do Windows mantém em memória material de autenticação (hashes NTLM, tickets Kerberos e, dependendo da configuração, senhas reversíveis) necessário para single sign-on; o Mimikatz lê essa memória e decodifica as estruturas internas do Windows para extrair esse material.

## Como usar
Requer privilégio de administrador/SYSTEM; dentro do console, `privilege::debug` eleva o privilégio do processo atual e `sekurlsa::logonpasswords` despeja as credenciais em memória. Outros módulos abusam de Kerberos (`kerberos::`) ou geram tickets forjados (`kerberos::golden`) a partir de material previamente extraído.

## Casos de uso
- Validação de exposição de credenciais em memória pós-comprometimento
- Demonstração de risco de pass-the-hash em avaliações de AD

## Alternativas
[[LaZagne]] · ProcDump + análise offline

## Categoria
[[MOC - Pós-Exploração]]

## Link oficial
https://github.com/gentilkiwi/mimikatz
