---
titulo: "Frida"
tipo: ferramenta
nome: "Frida"
categoria: "Ofensivo/Mobile"
subcategoria: "Instrumentação Dinâmica"
plataformas: ["Linux", "Windows", "macOS", "Android", "iOS"]
licenca: "wxWindows (LGPL-like)"
linguagem: "C/Python/JavaScript"
mitre_attack: ["T1422"]
nivel: avancado
situacao: ativo
link_oficial: "https://frida.re/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/mobile
  - arsenal-de-ferramentas
---

# Frida

> Toolkit de instrumentação dinâmica para injetar scripts JavaScript em processos nativos e apps móveis.

## Como funciona
Injeta um motor JavaScript (QuickJS/V8) dentro do processo alvo em tempo de execução, permitindo interceptar ('hook') qualquer função nativa ou gerenciada antes/depois de sua execução, ler e modificar argumentos e valores de retorno, e chamar funções arbitrárias do processo — tudo sem recompilar o binário alvo.

## Como usar
`frida -U -f com.app.alvo -l script.js --no-pause` inicia o app em um dispositivo USB conectado, já com o script de hook carregado desde a inicialização; scripts típicos interceptam funções de verificação de certificado (bypass de SSL pinning) ou de checagem de root/jailbreak.

## Casos de uso
- Bypass de SSL pinning em testes de apps móveis
- Hooking de funções para análise de comportamento em tempo de execução

## Alternativas
[[objection]]

## Categoria
[[MOC - Mobile - Cibersegurança]]

## Link oficial
https://frida.re/
