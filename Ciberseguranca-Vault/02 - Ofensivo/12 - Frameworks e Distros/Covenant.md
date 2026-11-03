---
titulo: "Covenant"
tipo: ferramenta
nome: "Covenant"
categoria: "Ofensivo/Frameworks-e-Distros"
subcategoria: "Framework C2 .NET"
plataformas: ["Linux", "Windows", "macOS (servidor .NET Core)"]
licenca: "GPLv3"
linguagem: "C#"
mitre_attack: ["T1071", "T1105"]
nivel: avancado
situacao: legado
link_oficial: "https://github.com/cobbr/Covenant"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/framework
---

# Covenant

> Framework C2 .NET com interface web colaborativa, focado em ambientes centrados em .NET/Windows.

## Como funciona
Centraliza a operação em uma interface web colaborativa (múltiplos operadores simultâneos), gerenciando 'Listeners' (canais de C2) e implantes chamados 'Grunts', escritos e compilados dinamicamente em C#/.NET, o que facilita integração com técnicas ofensivas que já exploram APIs .NET nativas do Windows.

## Como usar
Após subir o servidor (`dotnet Covenant.dll`), acessa-se a interface web para criar um Listener, gerar um Launcher (payload inicial) para entrega ao alvo e, após o callback, interagir com o Grunt resultante através de comandos na própria interface web.

## Casos de uso
- Red team em ambientes predominantemente Windows/.NET
- Treinamento sobre detecção de C2 baseado em .NET

## Alternativas
[[Sliver]] · [[Empire]]

## Categoria
[[MOC - Frameworks e Distros]]

## Link oficial
https://github.com/cobbr/Covenant
