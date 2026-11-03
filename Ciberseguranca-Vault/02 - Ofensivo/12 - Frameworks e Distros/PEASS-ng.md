---
titulo: "PEASS-ng"
tipo: ferramenta
nome: "PEASS-ng"
categoria: "Ofensivo/Frameworks-e-Distros"
subcategoria: "Enumeração para Escalonamento de Privilégio"
plataformas: ["Linux", "Windows"]
licenca: "GPLv3"
linguagem: "Shell/C#/Python"
mitre_attack: ["T1068"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/peass-ng/PEASS-ng"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/framework
---

# PEASS-ng

> Conjunto de scripts (LinPEAS/WinPEAS) que enumeram vetores de escalonamento de privilégio local.

## Como funciona
Executa uma checklist extensa e automatizada de pontos de verificação conhecidos por permitirem escalonamento de privilégio local (binários com SUID mal configurados, tarefas agendadas graváveis, credenciais em arquivos de configuração, serviços com permissão insegura) e destaca em cores, no próprio terminal, os achados mais prováveis de serem exploráveis.

## Como usar
Basta transferir e executar o script correspondente ao sistema operacional (`./linpeas.sh` em Linux, `winpeas.exe` em Windows) diretamente na máquina alvo, já com acesso local; a saída colorida prioriza visualmente (vermelho/amarelo) os achados mais relevantes dentre centenas de verificações realizadas.

## Casos de uso
- Identificação automatizada de más configurações para escalonamento local
- Checklist de pós-exploração em CTFs e pentests autorizados

## Alternativas
[[PowerSploit]]

## Categoria
[[MOC - Frameworks e Distros]]

## Link oficial
https://github.com/peass-ng/PEASS-ng
