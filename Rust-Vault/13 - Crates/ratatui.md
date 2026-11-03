---
tags: [rust, crates]
aliases: ["ratatui", "TUI", "interface de terminal", "crossterm"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Áreas de Aplicação]]", "[[Escolhendo e avaliando crates]]"]
---

# ratatui

**ratatui** constrói interfaces de terminal (TUI) com widgets (listas, tabelas, gráficos, blocos), usando um backend como `crossterm`.

```toml
[dependencies]
ratatui = "0.29"
crossterm = "0.28"
```

```rust
// requer crate: ratatui
use ratatui::{
    crossterm::event::{self, Event, KeyCode},
    widgets::{Block, Borders, Paragraph},
    DefaultTerminal, Frame,
};

fn main() -> std::io::Result<()> {
    let mut terminal = ratatui::init(); // entra em modo raw + tela alternativa
    let resultado = executa(&mut terminal);
    ratatui::restore();                  // restaura o terminal SEMPRE
    resultado
}

fn executa(terminal: &mut DefaultTerminal) -> std::io::Result<()> {
    loop {
        terminal.draw(desenha)?;
        if let Event::Key(tecla) = event::read()? {
            if tecla.code == KeyCode::Char('q') {
                return Ok(());
            }
        }
    }
}

fn desenha(frame: &mut Frame) {
    let texto = Paragraph::new("Olá, ratatui! Pressione 'q' para sair.")
        .block(Block::default().title("Exemplo").borders(Borders::ALL));
    frame.render_widget(texto, frame.area());
}
```

> [!question] Verificar na documentação oficial
> A API mudou entre versões (por exemplo, `frame.size()` virou `frame.area()`, e `ratatui::init()` surgiu depois). Confirme em ratatui.rs.

> [!warning] Restaure o terminal
> Se o programa der panic sem restaurar o terminal, o shell fica quebrado. Use `ratatui::init()`, que instala um *panic hook* para isso.

## Veja também

- [[Áreas de Aplicação]]
- [[Escolhendo e avaliando crates]]
