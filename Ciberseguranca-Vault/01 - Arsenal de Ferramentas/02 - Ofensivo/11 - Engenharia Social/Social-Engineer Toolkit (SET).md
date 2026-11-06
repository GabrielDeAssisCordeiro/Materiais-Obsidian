---
titulo: "Social-Engineer Toolkit (SET)"
tipo: ferramenta
nome: "Social-Engineer Toolkit (SET)"
categoria: "Ofensivo/Social-Engineering"
subcategoria: "Framework de Ataques de Engenharia Social"
plataformas: ["Linux", "macOS"]
licenca: "BSD-3-Clause"
linguagem: "Python"
mitre_attack: ["T1566"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/trustedsec/social-engineer-toolkit"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/social-engineering
  - arsenal-de-ferramentas
---

# Social-Engineer Toolkit (SET)

> Framework para criação de campanhas de phishing, clonagem de sites e payloads de engenharia social.

## Como funciona
Automatiza cenários de ataque centrados em engajamento humano: clona páginas de login existentes (copiando HTML/CSS da página original) para capturar credenciais submetidas, gera payloads integrados ao Metasploit para campanhas de e-mail, e orquestra o fluxo completo (criação do vetor, hospedagem, captura de resultado) através de um menu interativo guiado.

## Como usar
Executa-se `setoolkit` e navega-se pelo menu interativo (ex.: 'Social-Engineering Attacks' > 'Website Attack Vectors' > 'Credential Harvester'), informando a URL do site a clonar; o SET sobe um servidor web local que serve a cópia e registra as credenciais submetidas.

## Casos de uso
- Simulação de phishing autorizada para treinamento de colaboradores
- Clonagem de página de login para teste de conscientização

## Alternativas
[[GoPhish]] · [[Evilginx]]

## Categoria
[[MOC - Engenharia Social]]

## Link oficial
https://github.com/trustedsec/social-engineer-toolkit
