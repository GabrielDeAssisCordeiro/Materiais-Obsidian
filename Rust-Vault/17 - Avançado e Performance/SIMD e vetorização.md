---
tags: [rust, performance, simd]
aliases: ["std::arch", "auto-vectorization", "portable simd", "wide"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Otimização de desempenho]]", "[[Iteradores]]", "[[Unsafe Rust]]", "[[Release profile LTO e codegen]]"]
---

# SIMD e vetorização

**SIMD** (*Single Instruction, Multiple Data*) processa vários valores com uma única instrução da CPU.

## Níveis de uso (do mais simples ao mais manual)

| Nível | Como |
|---|---|
| **Auto-vetorização** | escreva laços simples sobre fatias; o LLVM vetoriza sozinho em `--release` |
| **Crates seguros** | `wide`, `memchr`, `simdutf8` ou `faster` abstraem as instruções |
| **`std::simd`** (portable SIMD) | API portátil, ainda **instável** (nightly) |
| **`std::arch`** | intrínsecos específicos de arquitetura (`unsafe`) |

## Facilitando a auto-vetorização

```rust
// Laço simples sobre fatias, sem ramos nem dependências entre iterações
fn soma_produtos(a: &[f32], b: &[f32]) -> f32 {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}

// Processar em blocos fixos ajuda o compilador
fn soma_blocos(v: &[f32]) -> f32 {
    let mut acc = [0.0f32; 8];
    let blocos = v.chunks_exact(8);
    let resto = blocos.remainder();
    for bloco in blocos {
        for i in 0..8 {
            acc[i] += bloco[i];
        }
    }
    acc.iter().sum::<f32>() + resto.iter().sum::<f32>()
}

fn main() {
    let a: Vec<f32> = (0..1000).map(|i| i as f32).collect();
    let b = vec![2.0f32; 1000];
    println!("{}", soma_produtos(&a, &b));
    println!("{}", soma_blocos(&a));
}
```

## Intrínsecos com detecção em tempo de execução

```rust
#[cfg(target_arch = "x86_64")]
fn soma_i32(v: &[i32]) -> i32 {
    if is_x86_feature_detected!("avx2") {
        // SAFETY: acabamos de verificar que a CPU suporta AVX2
        unsafe { soma_avx2(v) }
    } else {
        v.iter().sum()
    }
}

#[cfg(target_arch = "x86_64")]
#[target_feature(enable = "avx2")]
unsafe fn soma_avx2(v: &[i32]) -> i32 {
    // O compilador pode usar AVX2 neste corpo para vetorizar automaticamente
    v.iter().sum()
}

#[cfg(not(target_arch = "x86_64"))]
fn soma_i32(v: &[i32]) -> i32 {
    v.iter().sum()
}

fn main() {
    println!("{}", soma_i32(&[1, 2, 3, 4, 5]));
}
```

> [!question] Verificar na documentação oficial
> O estado de `std::simd` e das regras de `#[target_feature]` (funções seguras com `target_feature`) mudou nas últimas versões. Confirme em doc.rust-lang.org/std/arch e doc.rust-lang.org/std/simd.

> [!tip] Verifique o assembly
> Use cargo-show-asm (`cargo asm`) ou o Compiler Explorer (godbolt.org) para confirmar que o laço foi vetorizado.

## Veja também

- [[Otimização de desempenho]]
- [[Iteradores]]
- [[Unsafe Rust]]
- [[Release profile LTO e codegen]]
