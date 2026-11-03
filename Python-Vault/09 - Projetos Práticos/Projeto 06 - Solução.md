---
titulo: "Projeto 06 – Solução: Bot de Telegram"
tags: [python, projeto, solucao, bot, telegram]
nivel: intermediario
criado: 2026-10-14
projeto: 6
---

# ✅ Projeto 06 – Solução: Bot de Telegram

Enunciado: [[09 - Projetos Práticos/Projeto 06 - Bot|Projeto 06]].

## 📁 Estrutura

```text
bot/
├── logica.py     # regras puras (testáveis)
├── bot.py        # handlers e inicialização
└── test_logica.py
```

## 💻 `logica.py`

```python
# arquivo: logica.py
"""Lógica pura do bot: sem dependência do Telegram."""

import random

LIMITE_LADOS = 1000
LIMITE_ESPERA = 24 * 3600  # 24 h


def rolar_dado(lados: int = 6, rng: random.Random | None = None) -> int:
    if not 2 <= lados <= LIMITE_LADOS:
        raise ValueError(f"escolha entre 2 e {LIMITE_LADOS} lados")
    return (rng or random).randint(1, lados)


def lancar_moeda(rng: random.Random | None = None) -> str:
    return (rng or random).choice(["cara", "coroa"])


def parse_lembrete(args: list[str]) -> tuple[int, str]:
    """['30', 'tomar', 'água'] -> (30, 'tomar água')"""
    if len(args) < 2:
        raise ValueError("uso: /lembrar <segundos> <texto>")
    try:
        segundos = int(args[0])
    except ValueError:
        raise ValueError("o primeiro argumento deve ser um número de segundos") from None
    if not 1 <= segundos <= LIMITE_ESPERA:
        raise ValueError(f"segundos entre 1 e {LIMITE_ESPERA}")
    return segundos, " ".join(args[1:])
```

## 💻 `bot.py`

```python
# arquivo: bot.py
"""Bot de Telegram com python-telegram-bot v21+."""

import logging
import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import logica

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.INFO
)
log = logging.getLogger("bot")

AJUDA = (
    "Comandos:\n"
    "/dado [lados] – rola um dado (padrão 6)\n"
    "/moeda – cara ou coroa\n"
    "/lembrar <segundos> <texto> – agenda um lembrete\n"
    "/ajuda – esta mensagem"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome = update.effective_user.first_name
    await update.message.reply_text(f"Olá, {nome}! 👋\n\n{AJUDA}")


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(AJUDA)


async def dado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        lados = int(context.args[0]) if context.args else 6
        resultado = logica.rolar_dado(lados)
    except ValueError as erro:
        await update.message.reply_text(f"⚠️ {erro}")
        return
    await update.message.reply_text(f"🎲 d{lados}: {resultado}")


async def moeda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"🪙 {logica.lancar_moeda()}")


async def disparar_lembrete(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    await context.bot.send_message(job.chat_id, f"⏰ Lembrete: {job.data}")


async def lembrar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        segundos, texto = logica.parse_lembrete(context.args)
    except ValueError as erro:
        await update.message.reply_text(f"⚠️ {erro}")
        return
    context.job_queue.run_once(
        disparar_lembrete,
        when=segundos,
        chat_id=update.effective_chat.id,
        data=texto,
        name=f"lembrete-{update.effective_chat.id}",
    )
    await update.message.reply_text(f"✅ Combinado! Aviso em {segundos}s.")


async def eco(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main() -> None:
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise SystemExit("Defina a variável de ambiente TELEGRAM_TOKEN.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))
    app.add_handler(CommandHandler("dado", dado))
    app.add_handler(CommandHandler("moeda", moeda))
    app.add_handler(CommandHandler("lembrar", lembrar))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, eco))

    log.info("Bot iniciado. Ctrl+C para parar.")
    app.run_polling()


if __name__ == "__main__":
    main()
```

## 🧪 `test_logica.py`

```python
# arquivo: test_logica.py
import random
import pytest
import logica


def test_dado_determinístico():
    rng = random.Random(1)
    assert 1 <= logica.rolar_dado(6, rng) <= 6


@pytest.mark.parametrize("lados", [0, 1, 5000, -3])
def test_dado_invalido(lados):
    with pytest.raises(ValueError):
        logica.rolar_dado(lados)


def test_lembrete():
    assert logica.parse_lembrete(["30", "tomar", "água"]) == (30, "tomar água")


@pytest.mark.parametrize("args", [[], ["10"], ["abc", "x"], ["0", "x"]])
def test_lembrete_invalido(args):
    with pytest.raises(ValueError):
        logica.parse_lembrete(args)
```

## 🔍 Pontos importantes

- **Handlers finos, lógica separada:** testamos `logica.py` sem rede nem token (R6).
- **`async/await`:** cada handler é uma corrotina; o `Application` gerencia o *event loop* ([[08 - Avançado/02 - Asyncio|Asyncio]]).
- **`JobQueue.run_once`** agenda sem bloquear. `job.data` carrega o texto.
- **`raise ... from None`** esconde o `ValueError` interno e mostra só a mensagem amigável.
- `filters.TEXT & ~filters.COMMAND` evita responder duas vezes a comandos.

## 🌐 Esboço em Discord (`discord.py`)

```python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def dado(ctx, lados: int = 6):
    import logica
    await ctx.send(f"🎲 {logica.rolar_dado(lados)}")

bot.run(os.environ["DISCORD_TOKEN"])
```

---

⬅️ [[09 - Projetos Práticos/Projeto 06 - Bot|Projeto 06]] | ➡️ [[09 - Projetos Práticos/Projeto 07 - Login com SQLite|Projeto 07]]

#python #projeto #solucao #bot #telegram
