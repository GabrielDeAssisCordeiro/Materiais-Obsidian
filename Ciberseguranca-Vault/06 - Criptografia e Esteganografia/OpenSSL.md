---
titulo: "OpenSSL"
tipo: ferramenta
nome: "OpenSSL"
categoria: "Cripto-e-Stego"
subcategoria: "Toolkit Criptográfico"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "C"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.openssl.org/"
tags:
  - ciberseguranca
  - ferramenta
  - cripto
---

# OpenSSL

> Biblioteca e toolkit de linha de comando de referência para operações criptográficas e TLS/SSL.

## Como funciona
Implementa a maioria dos algoritmos criptográficos padrão (cifração simétrica/assimétrica, hashing, assinatura digital) e o protocolo TLS/SSL completo, servindo tanto como biblioteca consumida por outros softwares quanto como ferramenta de linha de comando para operações pontuais como geração de chaves, certificados e verificação manual de conexões TLS.

## Como usar
`openssl genrsa -out chave.pem 2048` gera um par de chaves RSA; `openssl req -new -x509 -key chave.pem -out cert.pem` cria um certificado autoassinado; `openssl s_client -connect alvo.com:443` conecta-se a um servidor TLS para inspecionar manualmente o certificado apresentado e os parâmetros da negociação.

## Casos de uso
- Geração e inspeção de certificados/chaves criptográficas
- Diagnóstico manual de conexões TLS/SSL em troubleshooting de segurança

## Alternativas
[[CyberChef]]

## Categoria
[[MOC - Criptografia e Esteganografia]]

## Link oficial
https://www.openssl.org/
