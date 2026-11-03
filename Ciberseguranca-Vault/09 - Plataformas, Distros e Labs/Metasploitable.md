---
titulo: "Metasploitable"
tipo: ferramenta
nome: "Metasploitable"
categoria: "Plataforma"
subcategoria: "VM Vulnerável para Treino"
plataformas: ["Linux (VM)"]
licenca: "Gratuito (Rapid7)"
linguagem: "N/A"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://docs.rapid7.com/metasploit/metasploitable-2/"
tags:
  - ciberseguranca
  - ferramenta
  - plataforma
---

# Metasploitable

> Máquina virtual Linux propositalmente vulnerável, mantida pela Rapid7 (criadora do Metasploit), para prática segura.

## Como funciona
Vem pré-configurada com dezenas de serviços de rede propositalmente desatualizados e mal configurados (FTP, Samba, bancos de dados, serviços web) cada um explorável por uma vulnerabilidade conhecida e documentada, servindo como alvo completo para praticar o ciclo de reconhecimento-exploração-pós-exploração em ambiente totalmente isolado e sem risco legal.

## Como usar
Baixa-se a imagem de VM pré-construída e executa-se localmente (VMware/VirtualBox) em rede isolada; a partir de uma máquina Kali na mesma rede, aplica-se Nmap para reconhecimento e Metasploit Framework para exploração dos serviços vulneráveis identificados.

## Casos de uso
- Prática segura e legal de exploração com Metasploit Framework
- Laboratório clássico para iniciantes em pentest de infraestrutura

## Alternativas
[[DVWA]]

## Categoria
[[MOC - Plataformas, Distros e Labs]]

## Link oficial
https://docs.rapid7.com/metasploit/metasploitable-2/
