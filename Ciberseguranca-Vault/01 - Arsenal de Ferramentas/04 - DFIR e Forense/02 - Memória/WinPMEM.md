---
titulo: "WinPMEM"
tipo: ferramenta
nome: "WinPMEM"
categoria: "DFIR/Memoria"
subcategoria: "Aquisição de Memória RAM"
plataformas: ["Windows"]
licenca: "Apache-2.0"
linguagem: "C"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/Velocidex/WinPmem"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/memoria
  - arsenal-de-ferramentas
---

# WinPMEM

> Driver e utilitário para aquisição forense da memória RAM de sistemas Windows em execução.

## Como funciona
Carrega um driver de kernel temporário que mapeia e copia o conteúdo físico da RAM para um arquivo de imagem, contornando as restrições normais de acesso à memória física que o espaço de usuário teria, de forma a capturar o estado completo da memória de um sistema ainda ligado antes que seja desligado (o que apagaria todo o conteúdo volátil).

## Como usar
Executa-se o utilitário com privilégio administrativo apontando o arquivo de saída (`winpmem.exe imagem.mem`); a imagem resultante é então analisada com Volatility 3 ou Rekall para extração de artefatos.

## Casos de uso
- Captura de memória viva antes de desligar um host comprometido
- Primeira etapa de resposta a incidente para preservar evidência volátil

## Alternativas
[[Volatility 3]]

## Categoria
[[MOC - Memória]]

## Link oficial
https://github.com/Velocidex/WinPmem
