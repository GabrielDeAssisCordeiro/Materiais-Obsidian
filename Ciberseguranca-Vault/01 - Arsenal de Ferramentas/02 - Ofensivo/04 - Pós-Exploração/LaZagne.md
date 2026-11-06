---
titulo: "LaZagne"
tipo: ferramenta
nome: "LaZagne"
categoria: "Ofensivo/Pos-Exploracao"
subcategoria: "Recuperação de Senhas Locais"
plataformas: ["Windows", "Linux", "macOS"]
licenca: "LGPL-3.0"
linguagem: "Python"
mitre_attack: ["T1555"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/AlessandroZ/LaZagne"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/pos-exploracao
  - arsenal-de-ferramentas
---

# LaZagne

> Recupera senhas armazenadas em navegadores, clientes de e-mail e outras aplicações locais.

## Como funciona
Para cada aplicação suportada, implementa a lógica específica de onde e como aquele software armazena e (quando aplicável) criptografa suas credenciais locais — bancos SQLite de navegadores, chaveiros do sistema, arquivos de configuração de clientes FTP/e-mail — e reverte essa proteção usando APIs do próprio sistema operacional (ex.: DPAPI no Windows).

## Como usar
A execução mais simples é `lazagne.exe all`, que varre todas as categorias suportadas (navegadores, Wi-Fi, bancos de dados, jogos, etc.); módulos individuais podem ser chamados isoladamente (`lazagne.exe browsers`) para reduzir ruído.

## Casos de uso
- Avaliação de exposição de credenciais salvas em estações de trabalho
- Pós-exploração em testes de engenharia social com acesso físico

## Alternativas
[[Mimikatz]]

## Categoria
[[MOC - Pós-Exploração]]

## Link oficial
https://github.com/AlessandroZ/LaZagne
