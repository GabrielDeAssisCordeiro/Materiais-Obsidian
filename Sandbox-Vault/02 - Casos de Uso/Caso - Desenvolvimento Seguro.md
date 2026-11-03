---
tags:
  - casos-de-uso
aliases:
  - "Secure development"
tipo: caso-de-uso
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Princípio do Menor Privilégio]]"
  - "[[Sandbox por Containers]]"
---
# Caso - Desenvolvimento Seguro

Desenvolver em ambientes isolados protege a máquina do desenvolvedor contra **dependências comprometidas** (ataques à cadeia de suprimentos), scripts de instalação maliciosos e segredos expostos.

- Abrir projetos desconhecidos em *devcontainer* ou VM.
- Evitar montar `~/.ssh` e `~/.aws` dentro do ambiente.
- Executar `npm install`/`pip install` de pacotes novos em ambiente descartável.

> [!warning] Scripts de instalação executam código
> Pacotes podem rodar código no momento da instalação (`postinstall`, `setup.py`). Em projetos não confiáveis, instale dentro de uma sandbox sem rede de saída irrestrita e sem segredos.

## Exercício

Liste quais pastas sensíveis do seu usuário nunca deveriam ser montadas em um ambiente de desenvolvimento de projeto desconhecido.

## Veja também

- [[Princípio do Menor Privilégio]]
- [[Criar Ambientes Python Isolados]]
- [[Sandbox por Containers]]
- [[MOC - Casos de Uso]]
