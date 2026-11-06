---
titulo: "APKTool"
tipo: ferramenta
nome: "APKTool"
categoria: "Ofensivo/Mobile"
subcategoria: "Engenharia Reversa de Pacotes Android"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "Java"
mitre_attack: ["T1422"]
nivel: intermediario
situacao: ativo
link_oficial: "https://apktool.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/mobile
  - arsenal-de-ferramentas
---

# APKTool

> Decompila e recompila arquivos APK, permitindo edição de recursos e smali code.

## Como funciona
Desempacota o APK (um arquivo ZIP) e converte o bytecode Dalvik (.dex) para 'smali', uma representação textual intermediária legível e editável, além de decodificar recursos binários (XML compactado, imagens) para seus formatos originais; após edição, o processo inverso reconstrói um APK funcional a partir do smali e recursos modificados.

## Como usar
`apktool d app.apk` decompila o pacote para uma pasta com os recursos e smali; após editar os arquivos necessários, `apktool b app/` recompila um novo APK, que ainda precisa ser assinado (ex.: com `apksigner` ou `jarsigner`) antes de ser instalado em um dispositivo.

## Casos de uso
- Análise estática de lógica e recursos de apps Android
- Modificação de app para testes de segurança (patching para bypass)

## Alternativas
[[MobSF]] · jadx

## Categoria
[[MOC - Mobile - Cibersegurança]]

## Link oficial
https://apktool.org/
