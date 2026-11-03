---
titulo: "MOC — Erros e Exceções"
tags: [cpp, moc, erros, excecoes]
aliases: ["MOC Erros e Exceções", "Tratamento de Erros"]
tipo: moc
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - STL e Ranges]]"]
---

# MOC — Erros e Exceções

Como detectar, sinalizar e tratar falhas: exceções, códigos de erro, `expected`, asserts e contratos.

## Exceções

- [[Exceções try catch throw]]
- [[Hierarquia de Exceções]]
- [[Segurança de Exceções]]
- [[Boas Práticas e Custo das Exceções]]

## Alternativas às exceções

- [[Códigos de Erro e error_code]]
- [[expected]] (tipo, na seção de STL)
- [[Tratamento de Erros com expected]]
- [[optional]] (ausência sem motivo)

## Bugs de programação

- [[Asserts e Contratos]]
- [[static_assert e Type Traits]]

## Mapa de decisão

```mermaid
flowchart TD
    A["Algo deu errado"] --> B{"Bug do programador?"}
    B -->|sim| C["assert / contrato"]
    B -->|não| D{"Esperado e frequente?"}
    D -->|sim| E["expected / error_code / optional"]
    D -->|"não, excepcional"| F["exceção"]
```

## Veja também

- [[Home - Cpp]]
- [[MOC - STL e Ranges]]
- [[RAII]]
- [[noexcept e Movimento]]
