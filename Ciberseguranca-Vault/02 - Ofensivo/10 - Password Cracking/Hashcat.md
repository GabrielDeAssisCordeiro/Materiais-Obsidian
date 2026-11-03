---
titulo: "Hashcat"
tipo: ferramenta
nome: "Hashcat"
categoria: "Ofensivo/Password-Cracking"
subcategoria: "Quebra de Hashes (GPU)"
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
  - ofensivo/senha
---

# Hashcat

> Ferramenta de quebra de hashes acelerada por GPU, suportando centenas de algoritmos.

## Como funciona
Explora o paralelismo massivo das GPUs para testar bilhões de candidatos de senha por segundo contra um hash alvo, suportando diferentes estratégias de ataque (dicionário, força bruta por máscara, combinação de wordlists, regras de mutação aplicadas a cada palavra) e centenas de modos de hash correspondentes a algoritmos específicos (NTLM, bcrypt, SHA, WPA2, etc., cada um identificado por um número de modo).

## Como usar
`hashcat -m 1000 hashes.txt wordlist.txt` indica o modo de hash (1000 = NTLM) e aplica um ataque de dicionário; regras de mutação (`-r regra.rule`) aumentam a cobertura combinando a wordlist com variações comuns (maiúsculas, números no final, etc.), e `-a 3` ativa ataque por máscara para força bruta direcionada.

## Casos de uso
- Quebra offline de hashes NTLM extraídos em pentest AD
- Auditoria de robustez de políticas de senha corporativas

## Alternativas
[[John the Ripper]]

## Categoria
[[MOC - Password Cracking]]

## Link oficial
https://hashcat.net/hashcat/
