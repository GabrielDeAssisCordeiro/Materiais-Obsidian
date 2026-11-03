---
titulo: "Projeto 08 – Solução: Dashboard de Finanças"
tags: [python, projeto, solucao, projeto-final, fastapi, sqlite]
nivel: avancado
criado: 2026-10-14
projeto: 8
---

# ✅ Projeto 08 – Solução: Dashboard de Finanças

Enunciado: [[09 - Projetos Práticos/Projeto 08 - Projeto Final|Projeto 08]].

## 📁 Estrutura

```text
financas/
├── db.py
├── main.py
├── static/
│   └── index.html
└── test_db.py
```

## 💻 `db.py` – camada de dados

```python
# arquivo: db.py
"""Acesso ao SQLite. Valores monetários em CENTAVOS (inteiros)."""

from __future__ import annotations

import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager

SCHEMA = """
CREATE TABLE IF NOT EXISTS transacoes (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    data           TEXT    NOT NULL,
    descricao      TEXT    NOT NULL,
    categoria      TEXT    NOT NULL,
    tipo           TEXT    NOT NULL CHECK (tipo IN ('receita', 'despesa')),
    valor_centavos INTEGER NOT NULL CHECK (valor_centavos > 0)
);
CREATE INDEX IF NOT EXISTS idx_transacoes_data ON transacoes (data);
"""


def caminho_padrao() -> str:
    return os.environ.get("FINANCAS_DB", "financas.db")


@contextmanager
def conectar(caminho: str | None = None) -> Iterator[sqlite3.Connection]:
    """Uma conexão por uso: commit se deu certo, rollback se falhou, sempre fecha."""
    conn = sqlite3.connect(caminho or caminho_padrao())
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def iniciar(caminho: str | None = None) -> None:
    with conectar(caminho) as conn:
        conn.executescript(SCHEMA)


def adicionar(conn: sqlite3.Connection, data: str, descricao: str,
              categoria: str, tipo: str, valor_centavos: int) -> int:
    cur = conn.execute(
        "INSERT INTO transacoes (data, descricao, categoria, tipo, valor_centavos) "
        "VALUES (?, ?, ?, ?, ?)",
        (data, descricao, categoria, tipo, valor_centavos),
    )
    return cur.lastrowid


def listar(conn: sqlite3.Connection, mes: str | None = None) -> list[dict]:
    sql = "SELECT * FROM transacoes"
    params: tuple = ()
    if mes:
        sql += " WHERE substr(data, 1, 7) = ?"
        params = (mes,)
    sql += " ORDER BY data DESC, id DESC"
    return [dict(l) for l in conn.execute(sql, params)]


def remover(conn: sqlite3.Connection, id_: int) -> bool:
    return conn.execute("DELETE FROM transacoes WHERE id = ?", (id_,)).rowcount > 0


def resumo(conn: sqlite3.Connection, mes: str) -> dict:
    linhas = conn.execute(
        "SELECT tipo, categoria, SUM(valor_centavos) AS total "
        "FROM transacoes WHERE substr(data, 1, 7) = ? "
        "GROUP BY tipo, categoria ORDER BY total DESC",
        (mes,),
    ).fetchall()
    receitas = sum(l["total"] for l in linhas if l["tipo"] == "receita")
    despesas = sum(l["total"] for l in linhas if l["tipo"] == "despesa")
    por_categoria = {l["categoria"]: l["total"] for l in linhas if l["tipo"] == "despesa"}
    return {
        "mes": mes,
        "receitas_centavos": receitas,
        "despesas_centavos": despesas,
        "saldo_centavos": receitas - despesas,
        "despesas_por_categoria": por_categoria,
    }
```

## 💻 `main.py` – API

```python
# arquivo: main.py
"""API do dashboard de finanças pessoais."""

from contextlib import asynccontextmanager
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import db

PASTA_ESTATICA = Path(__file__).parent / "static"
MES = Query(pattern=r"^\d{4}-(0[1-9]|1[0-2])$", description="AAAA-MM")


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.iniciar()          # cria as tabelas na inicialização
    yield


app = FastAPI(title="Finanças Pessoais", lifespan=lifespan)


class TransacaoIn(BaseModel):
    data: date
    descricao: str = Field(min_length=1, max_length=120)
    categoria: str = Field(min_length=1, max_length=40)
    tipo: Literal["receita", "despesa"]
    valor: Decimal = Field(gt=0, max_digits=12, decimal_places=2)


def _para_api(linha: dict) -> dict:
    return {
        "id": linha["id"],
        "data": linha["data"],
        "descricao": linha["descricao"],
        "categoria": linha["categoria"],
        "tipo": linha["tipo"],
        "valor": linha["valor_centavos"] / 100,
    }


@app.get("/", include_in_schema=False)
def pagina():
    return FileResponse(PASTA_ESTATICA / "index.html")


@app.post("/transacoes", status_code=201)
def criar(t: TransacaoIn):
    with db.conectar() as conn:
        novo_id = db.adicionar(
            conn, t.data.isoformat(), t.descricao.strip(), t.categoria.strip(),
            t.tipo, int(t.valor * 100),
        )
    return {"id": novo_id}


@app.get("/transacoes")
def listar(mes: str | None = Query(None, pattern=r"^\d{4}-(0[1-9]|1[0-2])$")):
    with db.conectar() as conn:
        return [_para_api(l) for l in db.listar(conn, mes)]


@app.delete("/transacoes/{id_}", status_code=204)
def apagar(id_: int):
    with db.conectar() as conn:
        if not db.remover(conn, id_):
            raise HTTPException(404, "Transação não encontrada")


@app.get("/resumo")
def obter_resumo(mes: str = MES):
    with db.conectar() as conn:
        r = db.resumo(conn, mes)
    return {
        "mes": r["mes"],
        "receitas": r["receitas_centavos"] / 100,
        "despesas": r["despesas_centavos"] / 100,
        "saldo": r["saldo_centavos"] / 100,
        "despesas_por_categoria": {
            k: v / 100 for k, v in r["despesas_por_categoria"].items()
        },
    }
```

## 💻 `static/index.html`

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Finanças Pessoais</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 880px; margin: 2rem auto; padding: 0 1rem; }
    .cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
    .card { border: 1px solid #ccc; border-radius: 8px; padding: 1rem; }
    .card strong { display: block; font-size: 1.4rem; }
    form { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: .5rem; margin: 1.5rem 0; }
    table { width: 100%; border-collapse: collapse; }
    th, td { text-align: left; padding: .4rem; border-bottom: 1px solid #ddd; }
    .receita { color: #0a7d32; } .despesa { color: #b3261e; }
    canvas { max-height: 280px; }
  </style>
</head>
<body>
  <h1>💰 Finanças Pessoais</h1>
  <label>Mês: <input type="month" id="mes"></label>

  <div class="cards">
    <div class="card">Receitas<strong id="rec">–</strong></div>
    <div class="card">Despesas<strong id="desp">–</strong></div>
    <div class="card">Saldo<strong id="saldo">–</strong></div>
  </div>

  <form id="form">
    <input type="date" name="data" required>
    <input name="descricao" placeholder="Descrição" required>
    <input name="categoria" placeholder="Categoria" required>
    <select name="tipo"><option value="despesa">Despesa</option><option value="receita">Receita</option></select>
    <input name="valor" type="number" step="0.01" min="0.01" placeholder="Valor" required>
    <button>Adicionar</button>
  </form>

  <canvas id="grafico"></canvas>

  <table>
    <thead><tr><th>Data</th><th>Descrição</th><th>Categoria</th><th>Valor</th><th></th></tr></thead>
    <tbody id="linhas"></tbody>
  </table>

<script>
const fmt = v => v.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
const $ = id => document.getElementById(id);
let grafico;

$("mes").value = new Date().toISOString().slice(0, 7);

async function carregar() {
  const mes = $("mes").value;
  const [resumo, lista] = await Promise.all([
    fetch(`/resumo?mes=${mes}`).then(r => r.json()),
    fetch(`/transacoes?mes=${mes}`).then(r => r.json()),
  ]);

  $("rec").textContent = fmt(resumo.receitas);
  $("desp").textContent = fmt(resumo.despesas);
  $("saldo").textContent = fmt(resumo.saldo);

  const cats = Object.keys(resumo.despesas_por_categoria);
  grafico?.destroy();
  grafico = new Chart($("grafico"), {
    type: "doughnut",
    data: { labels: cats, datasets: [{ data: Object.values(resumo.despesas_por_categoria) }] },
    options: { plugins: { title: { display: true, text: "Despesas por categoria" } } },
  });

  const tbody = $("linhas");
  tbody.replaceChildren();
  for (const t of lista) {
    const tr = document.createElement("tr");
    for (const texto of [t.data, t.descricao, t.categoria]) {
      const td = document.createElement("td");
      td.textContent = texto;               // textContent evita XSS
      tr.append(td);
    }
    const tdValor = document.createElement("td");
    tdValor.textContent = (t.tipo === "despesa" ? "− " : "+ ") + fmt(t.valor);
    tdValor.className = t.tipo;
    const tdAcao = document.createElement("td");
    const btn = document.createElement("button");
    btn.textContent = "🗑";
    btn.onclick = async () => { await fetch(`/transacoes/${t.id}`, { method: "DELETE" }); carregar(); };
    tdAcao.append(btn);
    tr.append(tdValor, tdAcao);
    tbody.append(tr);
  }
}

$("form").addEventListener("submit", async e => {
  e.preventDefault();
  const dados = Object.fromEntries(new FormData(e.target));
  const r = await fetch("/transacoes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dados),
  });
  if (!r.ok) { alert("Dados inválidos"); return; }
  e.target.reset();
  carregar();
});

$("mes").addEventListener("change", carregar);
carregar();
</script>
</body>
</html>
```

## 🧪 `test_db.py`

```python
# arquivo: test_db.py
import sqlite3
import pytest
import db


@pytest.fixture
def caminho(tmp_path):
    arq = str(tmp_path / "t.db")
    db.iniciar(arq)
    return arq


def test_adicionar_e_listar(caminho):
    with db.conectar(caminho) as conn:
        db.adicionar(conn, "2026-10-05", "Mercado", "Alimentação", "despesa", 15990)
        db.adicionar(conn, "2026-10-01", "Salário", "Renda", "receita", 500000)
        db.adicionar(conn, "2026-11-01", "Outro mês", "X", "despesa", 100)
    with db.conectar(caminho) as conn:
        assert len(db.listar(conn, "2026-10")) == 2
        assert len(db.listar(conn)) == 3


def test_resumo(caminho):
    with db.conectar(caminho) as conn:
        db.adicionar(conn, "2026-10-01", "Salário", "Renda", "receita", 500000)
        db.adicionar(conn, "2026-10-05", "Mercado", "Alimentação", "despesa", 15990)
        db.adicionar(conn, "2026-10-06", "Cinema", "Lazer", "despesa", 4000)
        r = db.resumo(conn, "2026-10")
    assert r["saldo_centavos"] == 500000 - 15990 - 4000
    assert r["despesas_por_categoria"] == {"Alimentação": 15990, "Lazer": 4000}


def test_check_constraint(caminho):
    with pytest.raises(sqlite3.IntegrityError):
        with db.conectar(caminho) as conn:
            db.adicionar(conn, "2026-10-01", "x", "y", "despesa", -5)


def test_rollback(caminho):
    with pytest.raises(sqlite3.IntegrityError):
        with db.conectar(caminho) as conn:
            db.adicionar(conn, "2026-10-01", "ok", "y", "despesa", 100)
            db.adicionar(conn, "2026-10-01", "ruim", "y", "despesa", 0)   # falha
    with db.conectar(caminho) as conn:
        assert db.listar(conn) == []        # nada foi gravado (transação atômica)


def test_remover(caminho):
    with db.conectar(caminho) as conn:
        i = db.adicionar(conn, "2026-10-01", "x", "y", "despesa", 100)
        assert db.remover(conn, i) is True
        assert db.remover(conn, i) is False
```

## ▶️ Executar

```bash
pip install "fastapi[standard]" pytest
fastapi dev main.py          # abra http://127.0.0.1:8000
pytest -q
```

## 🔍 Pontos importantes

- **Camadas:** navegador → rotas → `db.py` → SQLite. Cada uma testável/substituível.
- **Centavos inteiros** no banco; conversão `Decimal → int(valor * 100)` só na borda. O `Decimal` do Pydantic evita erros de `float` na entrada.
- **`conectar()`** é um *context manager* com `commit/rollback/close` — exatamente o padrão do módulo 07, e o teste `test_rollback` prova a atomicidade.
- **`CHECK` no SQL** é a última linha de defesa de integridade.
- **XSS:** o front usa `textContent`, nunca `innerHTML`, para dados vindos do usuário.
- **Segurança de path:** `Path(__file__).parent` torna o app independente do diretório de execução.

## 🎓 Parabéns!

Você percorreu todo o caminho do `print("Olá")` até uma aplicação completa. Continue em [[10 - Recursos e Referências/01 - Livros Recomendados|Recursos e Referências]].

---

⬅️ [[09 - Projetos Práticos/Projeto 08 - Projeto Final|Projeto 08]] | ➡️ [[10 - Recursos e Referências/01 - Livros Recomendados|Módulo 10 – Recursos]]

#python #projeto #solucao #projeto-final #fastapi #sqlite
