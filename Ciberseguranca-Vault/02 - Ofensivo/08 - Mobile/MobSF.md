---
titulo: "MobSF"
tipo: ferramenta
nome: "MobSF"
categoria: "Ofensivo/Mobile"
subcategoria: "Análise Estática e Dinâmica de Apps"
plataformas: ["Linux", "Windows", "macOS", "Docker"]
licenca: "GPLv3"
linguagem: "Python"
mitre_attack: ["T1422"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/MobSF/Mobile-Security-Framework-MobSF"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/mobile
---

# MobSF

> Plataforma automatizada de análise estática/dinâmica para apps Android, iOS e Windows.

## Como funciona
Na análise estática, descompila o pacote do app (APK/IPA) e inspeciona manifesto, permissões, código decompilado e recursos em busca de más práticas conhecidas (chaves hardcoded, permissões excessivas, configurações de rede inseguras); na análise dinâmica, executa o app em um emulador instrumentado, capturando chamadas de API, tráfego de rede e comportamento em tempo real.

## Como usar
A forma mais simples é via Docker (`docker run -p 8000:8000 opensecurity/mobile-security-framework-mobsf`); pela interface web, faz-se upload do APK/IPA e o relatório estático é gerado automaticamente, com pontuação de risco por categoria (rede, código, permissões) e opção de iniciar análise dinâmica em ambiente emulado integrado.

## Casos de uso
- Análise automatizada de segurança de APK/IPA antes de publicação
- Identificação de segredos hardcoded e más permissões

## Alternativas
[[objection]] · [[APKTool]]

## Categoria
[[MOC - Mobile - Cibersegurança]]

## Link oficial
https://github.com/MobSF/Mobile-Security-Framework-MobSF
