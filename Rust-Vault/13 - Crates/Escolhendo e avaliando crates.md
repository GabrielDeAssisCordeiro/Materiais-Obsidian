---
tags: [rust, crates]
aliases: ["avaliar dependências"]
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Comandos úteis do Cargo]]", "[[Cargo.toml e dependências]]", "[[Outros crates úteis]]"]
---

# Escolhendo e avaliando crates

O ecossistema gira em torno do **crates.io** (registro), **docs.rs** (documentação) e ferramentas como **lib.rs** e **blessed.rs** (listas curadas).

## Checklist de avaliação

| Critério | Pergunte |
|---|---|
| Manutenção | Último commit/release? Issues respondidas? |
| Adoção | Downloads, dependentes (reverse dependencies)? |
| Qualidade | Documentação completa? Testes e CI? |
| Maturidade | Versão `1.x` ou `0.x` (API instável)? |
| Segurança | Avisos no RustSec (`cargo audit`)? Muito `unsafe`? |
| Licença | Compatível com seu projeto? (`cargo deny`) |
| Peso | Quantas dependências transitivas traz (`cargo tree`)? Tempo de compilação? |
| Features | Dá para desligar o que não usa? |

```bash
cargo add serde --features derive   # adiciona a dependência
cargo tree -d                       # duplicatas de versões
cargo audit                         # vulnerabilidades conhecidas
```

> [!tip] Prefira a biblioteca padrão quando bastar
> Por exemplo, `std::sync::LazyLock` e `OnceLock` substituem `once_cell`/`lazy_static` em muitos casos; veja [[LazyLock e OnceLock]].

> [!warning] Cadeia de suprimentos
> Cada dependência é código de terceiros executado com os seus privilégios (inclusive `build.rs` e macros). Revise o que adiciona e fixe versões na CI.

## Veja também

- [[Comandos úteis do Cargo]]
- [[Cargo.toml e dependências]]
- [[Outros crates úteis]]
