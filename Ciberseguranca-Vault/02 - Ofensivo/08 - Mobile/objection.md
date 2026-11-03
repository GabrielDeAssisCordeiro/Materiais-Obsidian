---
titulo: "objection"
tipo: ferramenta
nome: "objection"
categoria: "Ofensivo/Mobile"
subcategoria: "Exploração Runtime de Apps"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv3"
linguagem: "Python"
mitre_attack: ["T1422"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/sensepost/objection"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/mobile
---

# objection

> Ferramenta de exploração runtime construída sobre Frida, sem necessidade de jailbreak/root.

## Como funciona
Empacota dezenas de hooks e técnicas comuns de teste de apps móveis (bypass de SSL pinning, detecção de root/jailbreak, dump de memória, interceptação de armazenamento local) como comandos prontos sobre o motor de instrumentação do Frida, eliminando a necessidade de escrever JavaScript manualmente para as tarefas mais rotineiras.

## Como usar
`objection -g com.app.alvo explore` injeta-se no processo do app e abre um shell interativo; dentro dele, comandos como `android sslpinning disable` ou `ios sslpinning disable` desativam proteções automaticamente, e `memory dump all` extrai a memória do processo para análise posterior.

## Casos de uso
- Bypass de proteções runtime em apps Android/iOS
- Exploração interativa de apps sem acesso root ao dispositivo

## Alternativas
[[Frida]]

## Categoria
[[MOC - Mobile - Cibersegurança]]

## Link oficial
https://github.com/sensepost/objection
