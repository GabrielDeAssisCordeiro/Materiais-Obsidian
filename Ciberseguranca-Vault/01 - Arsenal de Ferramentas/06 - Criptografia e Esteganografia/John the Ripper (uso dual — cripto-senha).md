---
titulo: "John the Ripper (uso dual — cripto/senha)"
tipo: ferramenta
nome: "John the Ripper (uso dual — cripto/senha)"
categoria: "Cripto-e-Stego"
subcategoria: "Benchmark e Criptoanálise de Hashes"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: ["T1110.002"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.openwall.com/john/"
tags:
  - ciberseguranca
  - ferramenta
  - cripto
  - arsenal-de-ferramentas
---

# John the Ripper (uso dual — cripto/senha)

> Nesta categoria, o John the Ripper é referenciado pela ótica de criptoanálise e suporte a formatos de hash de arquivos. Nota completa (uso ofensivo de quebra de senha) em [[John the Ripper]], pasta 1.10-Password-Cracking.

## Como funciona
Ver nota principal em [[John the Ripper]] para detalhes do motor e modos de ataque.

## Como usar
O modo `--test` embutido realiza benchmark comparativo de velocidade entre os diversos formatos de hash suportados na máquina local, útil para dimensionar o esforço computacional necessário para auditar uma política de senha específica.

## Casos de uso
- Benchmark comparativo de formatos de hash suportados
- Suporte a formatos de arquivo criptografados (zip, PDF, documentos)

## Alternativas
[[Hashcat]]

## Categoria
[[MOC - Criptografia e Esteganografia]]

## Link oficial
https://www.openwall.com/john/
