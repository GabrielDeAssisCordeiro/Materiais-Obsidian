---
titulo: "Evilginx"
tipo: ferramenta
nome: "Evilginx"
categoria: "Ofensivo/Social-Engineering"
subcategoria: "Proxy Reverso de Phishing (Bypass MFA)"
plataformas: ["Linux"]
licenca: "GPLv3"
linguagem: "Go"
mitre_attack: ["T1566.002", "T1111"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/kgretzky/evilginx2"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/social-engineering
---

# Evilginx

> Proxy reverso transparente que captura credenciais e tokens de sessão, demonstrando bypass de MFA baseado em OTP.

## Como funciona
Funciona como um proxy reverso posicionado entre a vítima e o serviço legítimo real: a vítima interage com a página genuína (servida através do proxy), incluindo a etapa de MFA, enquanto o Evilginx captura de forma transparente tanto as credenciais quanto o cookie de sessão emitido após a autenticação bem-sucedida — esse cookie, se reutilizado pelo atacante, concede acesso autenticado sem precisar repetir o desafio de MFA.

## Como usar
Configura-se um 'phishlet' (template que descreve o serviço a ser proxiado) com `config domain alvo-simulado.com` apontando para um domínio controlado pelo operador; ao ativar o phishlet, o Evilginx gera a URL de phishing e, assim que uma vítima autentica através dela, a sessão capturada fica disponível para o operador importar em seu próprio navegador.

## Casos de uso
- Demonstração de risco de phishing avançado com captura de sessão para gestão
- Avaliação de eficácia de controles de MFA em exercícios red team autorizados

## Alternativas
[[Social-Engineer Toolkit (SET)]] · [[GoPhish]]

## Categoria
[[MOC - Engenharia Social]]

## Link oficial
https://github.com/kgretzky/evilginx2
