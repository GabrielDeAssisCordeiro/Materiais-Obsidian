---
titulo: "Volatility 3"
tipo: ferramenta
nome: "Volatility 3"
categoria: "DFIR/Memoria"
subcategoria: "Análise Forense de Memória"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "VSL (Volatility Software License)"
linguagem: "Python"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/volatilityfoundation/volatility3"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/memoria
  - arsenal-de-ferramentas
---

# Volatility 3

> Framework padrão da indústria para análise forense de dumps de memória RAM.

## Como funciona
Interpreta a estrutura interna de memória de um sistema operacional (listas encadeadas do kernel representando processos, conexões de rede, módulos carregados) sem depender de símbolos de depuração pré-instalados no sistema analisado, reconstruindo esses dados a partir de um dump bruto de RAM para revelar processos ocultos, injeção de código e artefatos de malware residentes apenas em memória.

## Como usar
Um fluxo típico roda plugins específicos sobre o dump: `vol3 -f dump.mem windows.pslist` lista processos, `windows.netscan` revela conexões de rede e `windows.malfind` procura regiões de memória com características de injeção de código, cada plugin revelando uma categoria diferente de artefato.

## Casos de uso
- Identificação de malware residente apenas em memória (fileless)
- Reconstrução de atividade de um sistema no momento do dump

## Alternativas
[[Rekall]]

## Categoria
[[MOC - Memória]]

## Link oficial
https://github.com/volatilityfoundation/volatility3
