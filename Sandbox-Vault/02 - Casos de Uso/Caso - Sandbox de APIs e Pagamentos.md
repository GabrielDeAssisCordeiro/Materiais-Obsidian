---
tags:
  - casos-de-uso
aliases:
  - "Stripe sandbox"
  - "PayPal sandbox"
  - "Modo de teste"
tipo: caso-de-uso
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Caso - Homologação e Staging]]"
  - "[[Sandbox de Dados]]"
---
# Caso - Sandbox de APIs e Pagamentos

Provedores como **Stripe** e **PayPal** oferecem ambientes de teste (*test mode* / *sandbox*) com chaves e contas separadas, onde nenhum dinheiro real é movimentado.

- Use chaves de teste exclusivamente em desenvolvimento e staging.
- Simule falhas (cartão recusado, *timeouts*, *webhooks* repetidos).
- Nunca versione chaves; use gerenciador de segredos.

> [!question] Verificar na documentação oficial
> Números de cartão de teste e nomes de variáveis mudam por provedor; consulte a documentação oficial de cada um.

> [!warning] Sandbox de API ≠ sandbox de segurança
> Aqui "sandbox" significa **ambiente de simulação funcional**. Não protege o seu sistema de código hostil.

## Exercício

Leia a documentação de um provedor de pagamentos e liste 3 cenários de falha que você testaria no modo sandbox.

## Veja também

- [[Caso - Homologação e Staging]]
- [[Sandbox de Dados]]
- [[Criar Sandbox de Desenvolvimento Web e APIs]]
- [[MOC - Casos de Uso]]
