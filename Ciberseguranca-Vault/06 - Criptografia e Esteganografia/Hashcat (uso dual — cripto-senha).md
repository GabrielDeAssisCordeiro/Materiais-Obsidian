---
titulo: "Hashcat (uso dual — cripto/senha)"
tipo: ferramenta
nome: "Hashcat (uso dual — cripto/senha)"
categoria: "Cripto-e-Stego"
subcategoria: "Benchmark e Criptoanálise de Hashes"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "C"
mitre_attack: ["T1110.002"]
nivel: intermediario
situacao: ativo
link_oficial: "https://hashcat.net/hashcat/"
tags:
  - ciberseguranca
  - ferramenta
  - cripto
---

# Hashcat (uso dual — cripto/senha)

> Nesta categoria, o Hashcat é referenciado pela ótica de benchmarking de algoritmos de hash e criptoanálise acadêmica. Nota completa (uso ofensivo de quebra de senha) em [[Hashcat]], pasta 1.10-Password-Cracking.

## Como funciona
Ver nota principal em [[Hashcat]] para detalhes do motor de computação em GPU e modos de ataque.

## Como usar
Além da quebra de senhas, serve para benchmarking comparativo da velocidade de diferentes algoritmos de hash em hardware específico, informando decisões de escolha de algoritmo (ex.: por que bcrypt é preferível a MD5 para armazenamento de senha, dada a diferença de ordens de grandeza na velocidade de teste de candidatos).

## Casos de uso
- Benchmark de performance de algoritmos de hash em GPU
- Avaliação acadêmica de resistência de algoritmos a ataques de força bruta

## Alternativas
[[John the Ripper]]

## Categoria
[[MOC - Criptografia e Esteganografia]]

## Link oficial
https://hashcat.net/hashcat/
