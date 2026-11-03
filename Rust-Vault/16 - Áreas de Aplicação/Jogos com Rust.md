---
tags: [rust, areas, jogos]
aliases: ["gamedev", "macroquad"]
tipo: pratica
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[bevy]]", "[[Rayon]]", "[[Traits]]", "[[Áreas de Aplicação]]"]
---

# Jogos com Rust

O desenvolvimento de jogos em Rust é impulsionado por **ECS** (*Entity Component System*): dados em componentes simples, comportamento em sistemas que processam conjuntos de componentes — um padrão que combina muito bem com o borrow checker e com paralelismo automático.

| Engine/biblioteca | Estilo |
|---|---|
| [[bevy]] | engine completa, orientada a dados (ECS) |
| `macroquad` | simples, ótima para começar e para protótipos 2D |
| `ggez` | 2D inspirada em LÖVE |
| `wgpu` | API gráfica de baixo nível portátil (Vulkan, Metal, DX12, WebGPU) |
| `rapier` | física 2D/3D |

## Ideia central do ECS (sem dependências)

```rust
struct Posicao {
    x: f32,
    y: f32,
}

struct Velocidade {
    dx: f32,
    dy: f32,
}

fn main() {
    // "Mundo" ingênuo: vetores paralelos indexados pela entidade
    let mut posicoes = vec![Posicao { x: 0.0, y: 0.0 }, Posicao { x: 5.0, y: 5.0 }];
    let velocidades = vec![Velocidade { dx: 1.0, dy: 0.5 }, Velocidade { dx: -1.0, dy: 0.0 }];

    // "Sistema" de movimento: processa todas as entidades com posição + velocidade
    for _quadro in 0..3 {
        for (p, v) in posicoes.iter_mut().zip(&velocidades) {
            p.x += v.dx;
            p.y += v.dy;
        }
    }

    for (i, p) in posicoes.iter().enumerate() {
        println!("entidade {i}: ({:.1}, {:.1})", p.x, p.y);
    }
}
```

## Exemplo em Bevy

```rust
// requer crate: bevy
use bevy::prelude::*;

#[derive(Component)]
struct Jogador;

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .add_systems(Startup, preparar)
        .add_systems(Update, mover)
        .run();
}

fn preparar(mut commands: Commands) {
    commands.spawn(Camera2d);
    commands.spawn((Jogador, Transform::default()));
}

fn mover(time: Res<Time>, mut q: Query<&mut Transform, With<Jogador>>) {
    for mut t in &mut q {
        t.translation.x += 50.0 * time.delta_secs();
    }
}
```

> [!question] Verificar na documentação oficial
> A API do Bevy muda a cada versão (por exemplo, `Camera2d` e `delta_secs`). Confira o guia da versão que você usa em bevy.org.

## Exercício

Estenda o ECS ingênuo acima com um componente `Vida` e um sistema que remove entidades com vida zero.

## Veja também

- [[bevy]]
- [[Rayon]]
- [[Traits]]
- [[Áreas de Aplicação]]
