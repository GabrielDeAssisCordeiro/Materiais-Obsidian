---
titulo: "Canarytokens"
tipo: ferramenta
nome: "Canarytokens"
categoria: "Defensivo/Deception-Honeypots"
subcategoria: "Tokens de Alerta (Deception)"
plataformas: ["Web", "Multiplataforma"]
licenca: "Gratuito (serviço) / MIT (self-hosted)"
linguagem: "Python"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://canarytokens.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/deception
---

# Canarytokens

> Gera 'iscas digitais' (documentos, URLs, chaves de API, registros DNS) que disparam um alerta imediato quando acessados.

## Como funciona
Cada token gerado é um recurso aparentemente legítimo e valioso (um documento Word, uma credencial AWS falsa, uma entrada DNS) embutido com um mecanismo de callback discreto: assim que alguém abre o documento, usa a credencial falsa ou resolve o domínio, uma notificação é disparada instantaneamente ao proprietário, revelando que um atacante alcançou aquele ponto específico do ambiente.

## Como usar
Gera-se um token gratuitamente no site (ou via instância self-hosted), escolhendo o tipo (documento, URL, chave AWS, etc.) e o e-mail/webhook de alerta; o token é então posicionado estrategicamente em locais que um atacante provavelmente acessaria (ex.: uma pasta de 'credenciais.docx' em um servidor de arquivos).

## Casos de uso
- Detecção precoce de movimentação lateral/acesso não autorizado
- Alertas de baixo custo sem necessidade de infraestrutura própria de honeypot

## Alternativas
[[Cowrie]]

## Categoria
[[MOC - Deception e Honeypots]]

## Link oficial
https://canarytokens.org/
