---
tags: [rust, crates, jogos]
aliases: ["motor de jogos"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Áreas de Aplicação]]", "[[Traits]]"]
---

# bevy

**Bevy** é uma engine de jogos *data-driven* baseada em **ECS** (Entity Component System): dados em *componentes*, lógica em *sistemas* (funções comuns de Rust).

| Conceito | Papel |
|---|---|
| **Entity** | um identificador (um "objeto" do jogo) |
| **Component** | dados anexados a uma entidade (`struct`) |
| **System** | função que consulta componentes e executa lógica |
| **Resource** | dado global único (tempo, configuração) |

```toml
[dependencies]
bevy = "0.16"
```

```rust
// requer crate: bevy
use bevy::prelude::*;

#[derive(Component)]
struct Pessoa;

#[derive(Component)]
struct Nome(String);

fn adiciona_pessoas(mut commands: Commands) {
    commands.spawn((Pessoa, Nome("Ana".to_string())));
    commands.spawn((Pessoa, Nome("Bia".to_string())));
}

fn cumprimenta(query: Query<&Nome, With<Pessoa>>) {
    for nome in &query {
        println!("olá, {}!", nome.0);
    }
}

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .add_systems(Startup, adiciona_pessoas)
        .add_systems(Update, cumprimenta)
        .run();
}
```

> [!question] Verificar na documentação oficial
> O Bevy lança versões 0.x com mudanças frequentes de API. Confirme versão e exemplos em bevyengine.org e docs.rs/bevy.

> [!tip] Por que ECS?
> Dados contíguos e sistemas independentes permitem paralelismo automático e ótimo uso de cache.

## Veja também

- [[Áreas de Aplicação]]
- [[Traits]]
