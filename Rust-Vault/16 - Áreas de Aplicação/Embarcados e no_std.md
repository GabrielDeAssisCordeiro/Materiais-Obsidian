---
tags: [rust, areas, no_std]
aliases: ["no_std", "embedded", "microcontrolador", "embassy", "embedded-hal", "core", "alloc"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Stack, heap e layout de memória]]", "[[Targets e cross-compilation]]", "[[Atômicos]]", "[[Sistemas operacionais em Rust]]"]
---

# Embarcados e no_std

Em microcontroladores não há sistema operacional, e frequentemente nem `malloc`. Rust suporta isso com `#![no_std]`: o crate usa só a biblioteca **`core`** (e opcionalmente **`alloc`**), sem `std`.

| Camada | Disponível em | Contém |
|---|---|---|
| `core` | sempre | `Option`, `Result`, iteradores, `fmt`, atômicos, `Cell`... |
| `alloc` | se houver alocador | `Vec`, `String`, `Box`, `Rc`, `Arc` |
| `std` | só com SO | threads, arquivos, rede, `HashMap` |

```rust
// trecho: firmware mínimo (exige target embarcado, por isso não é compilado aqui)
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _; // define o que fazer em panic: travar

#[entry]
fn main() -> ! {
    // acessar periféricos via um PAC/HAL, ex.: piscar um LED
    loop {
        // led.toggle(); delay.delay_ms(500);
    }
}
```

```bash
rustup target add thumbv7em-none-eabihf   # Cortex-M4F/M7
cargo install probe-rs-tools
cargo run --release                        # grava e executa via probe-rs
```

## Ecossistema

- **`embedded-hal`**: traits comuns (`OutputPin`, `SpiBus`, `I2c`...) para que drivers funcionem em qualquer chip.
- **PAC/HAL**: crates gerados por chip (`stm32f4xx-hal`, `rp2040-hal`, `esp-hal`, `nrf-hal`).
- **Embassy**: executor `async` para microcontroladores, sem alocação dinâmica.
- **RTIC**: concorrência baseada em interrupções.
- **`heapless`**: `Vec`, `String`, filas de capacidade fixa na pilha.
- **`defmt`**: logs eficientes.

> [!tip] Por que Rust aqui
> O sistema de tipos modela o estado do hardware (por exemplo, um pino "configurado como saída" é outro tipo que um "configurado como entrada"); veja [[Typestate]].

> [!warning] `panic` sem `std`
> Você deve definir o *panic handler* (`panic-halt`, `panic-probe`...). Em firmware, prefira retornar `Result` a entrar em pânico.

## Veja também

- [[Stack, heap e layout de memória]]
- [[Targets e cross-compilation]]
- [[Atômicos]]
- [[Sistemas operacionais em Rust]]
