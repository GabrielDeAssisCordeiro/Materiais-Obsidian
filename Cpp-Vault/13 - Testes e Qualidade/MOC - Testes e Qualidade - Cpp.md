---
titulo: "MOC - Testes e Qualidade - Cpp"
tags: [cpp, moc, testes, qualidade]
aliases: ["MOC Testes e Qualidade"]
tipo: moc
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Build e Ferramentas]]", "[[MOC - Erros e Exceções]]"]
---

# MOC - Testes e Qualidade - Cpp

```mermaid
flowchart TD
    F[Fundamentos de testes] --> G[GoogleTest]
    F --> C[Catch2 e doctest]
    G --> M[gMock]
    G --> CI[CI/CD]
    CI --> COV[Cobertura]
    CI --> SAN["Sanitizers (seção 12)"]
    F --> FZ[Fuzzing]
    F --> B[Google Benchmark]
    CI --> CG[Core Guidelines]
```

## Testes

- [[Fundamentos de Testes Unitários]]
- [[GoogleTest]]
- [[Catch2 e doctest]]
- [[gMock e Dublês de Teste]]
- [[Fuzzing]]
- [[Google Benchmark]]

## Qualidade

- [[Cobertura com gcov e lcov]]
- [[CI e CD para Cpp]]
- [[Core Guidelines]]

## Ordem sugerida

[[Fundamentos de Testes Unitários]] → [[GoogleTest]] → [[Catch2 e doctest]] → [[gMock e Dublês de Teste]] → [[Cobertura com gcov e lcov]] → [[CI e CD para Cpp]] → [[Fuzzing]] → [[Google Benchmark]] → [[Core Guidelines]]

## Veja também

- [[Home - Cpp]]
- [[MOC - Build e Ferramentas]]
- [[MOC - Erros e Exceções]]
- [[Sanitizers]]
