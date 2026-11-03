---
tags: [rust, crates]
aliases: ["chrono", "time", "std::time", "datas e horas", "Instant"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Escolhendo e avaliando crates]]"]
---

# chrono e time

## Biblioteca padrão

`std::time` cobre medições e duração, mas **não** calendário nem fuso horário.

```rust
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

fn main() {
    // Instant: relógio monotônico, para medir tempo decorrido
    let inicio = Instant::now();
    let soma: u64 = (1..=1_000_000u64).sum();
    let gasto = inicio.elapsed();
    println!("soma={soma} em {:?} ({} µs)", gasto, gasto.as_micros());

    // Duration
    let d = Duration::from_millis(1500);
    println!("{} s e {} ms", d.as_secs(), d.subsec_millis());
    println!("{:?}", d + Duration::from_secs(2));

    // SystemTime: relógio de parede (pode retroceder)
    let epoca = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    println!("segundos desde 1970: {}", epoca.as_secs() > 0);
}
```

## chrono e time

| | `chrono` | `time` |
|---|---|---|
| Popularidade | muito alta | alta e crescente |
| Fusos horários | `chrono-tz` | `time-tz` / `OffsetDateTime` |
| API | `DateTime<Utc>`, `NaiveDate`, `format("%Y-%m-%d")` | `OffsetDateTime`, `Date`, macros `format_description!` |

```rust
// requer crate: chrono
use chrono::{Datelike, Duration, NaiveDate, Utc};

fn main() {
    let agora = Utc::now();
    println!("{}", agora.format("%d/%m/%Y %H:%M"));

    let data = NaiveDate::from_ymd_opt(2026, 10, 24).unwrap();
    let daqui_a_30 = data + Duration::days(30);
    println!("{} ({:?})", daqui_a_30, daqui_a_30.weekday());
}
```

> [!tip] Guarde tempos em UTC
> Armazene e calcule em UTC; converta para o fuso local só na exibição.

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/chrono antes de copiar para um projeto.

## Veja também

- [[Escolhendo e avaliando crates]]
