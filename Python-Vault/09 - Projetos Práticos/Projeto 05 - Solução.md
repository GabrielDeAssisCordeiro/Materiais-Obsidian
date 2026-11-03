---
titulo: "Projeto 05 – Solução: API REST"
tags: [python, projeto, solucao, api, fastapi]
nivel: intermediario
criado: 2026-10-14
projeto: 5
---

# ✅ Projeto 05 – Solução: API REST

Enunciado: [[09 - Projetos Práticos/Projeto 05 - API REST|Projeto 05]].

## 💻 Código completo

```python
# arquivo: main.py
"""API REST de catálogo de livros (FastAPI)."""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


# ---------- Modelos ----------
class LivroIn(BaseModel):
    """Corpo de POST/PUT."""
    titulo: str = Field(min_length=1, max_length=200)
    autor: str = Field(min_length=1, max_length=100)
    ano: int = Field(ge=1450, le=2100)


class Livro(LivroIn):
    """Resposta: entrada + id."""
    id: int


class LivroPatch(BaseModel):
    """Corpo de PATCH: tudo opcional."""
    titulo: str | None = Field(default=None, min_length=1, max_length=200)
    autor: str | None = Field(default=None, min_length=1, max_length=100)
    ano: int | None = Field(default=None, ge=1450, le=2100)


# ---------- Repositório em memória ----------
class RepositorioLivros:
    def __init__(self) -> None:
        self._dados: dict[int, Livro] = {}
        self._proximo_id = 1

    def criar(self, dados: LivroIn) -> Livro:
        livro = Livro(id=self._proximo_id, **dados.model_dump())
        self._dados[livro.id] = livro
        self._proximo_id += 1
        return livro

    def listar(self, autor: str | None, skip: int, limit: int) -> list[Livro]:
        livros = list(self._dados.values())
        if autor:
            livros = [l for l in livros if autor.lower() in l.autor.lower()]
        return livros[skip : skip + limit]

    def obter(self, id_: int) -> Livro | None:
        return self._dados.get(id_)

    def substituir(self, id_: int, dados: LivroIn) -> Livro | None:
        if id_ not in self._dados:
            return None
        self._dados[id_] = Livro(id=id_, **dados.model_dump())
        return self._dados[id_]

    def atualizar(self, id_: int, dados: LivroPatch) -> Livro | None:
        atual = self._dados.get(id_)
        if atual is None:
            return None
        novo = atual.model_copy(update=dados.model_dump(exclude_unset=True))
        self._dados[id_] = novo
        return novo

    def remover(self, id_: int) -> bool:
        return self._dados.pop(id_, None) is not None


repo = RepositorioLivros()
app = FastAPI(title="Catálogo de Livros", version="1.0")


def _ou_404(livro: Livro | None) -> Livro:
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro


# ---------- Rotas ----------
@app.post("/livros", response_model=Livro, status_code=201)
def criar_livro(dados: LivroIn):
    return repo.criar(dados)


@app.get("/livros", response_model=list[Livro])
def listar_livros(
    autor: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    return repo.listar(autor, skip, limit)


@app.get("/livros/{livro_id}", response_model=Livro)
def obter_livro(livro_id: int):
    return _ou_404(repo.obter(livro_id))


@app.put("/livros/{livro_id}", response_model=Livro)
def substituir_livro(livro_id: int, dados: LivroIn):
    return _ou_404(repo.substituir(livro_id, dados))


@app.patch("/livros/{livro_id}", response_model=Livro)
def atualizar_livro(livro_id: int, dados: LivroPatch):
    return _ou_404(repo.atualizar(livro_id, dados))


@app.delete("/livros/{livro_id}", status_code=204)
def remover_livro(livro_id: int):
    if not repo.remover(livro_id):
        raise HTTPException(status_code=404, detail="Livro não encontrado")
```

## 🧪 Testes

```python
# arquivo: test_api.py
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def setup_function():
    main.repo.__init__()          # zera o estado entre testes


def test_crud():
    r = client.post("/livros", json={"titulo": "Fluent Python", "autor": "Luciano Ramalho", "ano": 2022})
    assert r.status_code == 201
    id_ = r.json()["id"]

    assert client.get(f"/livros/{id_}").json()["titulo"] == "Fluent Python"
    assert client.patch(f"/livros/{id_}", json={"ano": 2023}).json()["ano"] == 2023
    assert client.get("/livros", params={"autor": "ramalho"}).json()[0]["id"] == id_
    assert client.delete(f"/livros/{id_}").status_code == 204
    assert client.get(f"/livros/{id_}").status_code == 404


def test_validacao():
    r = client.post("/livros", json={"titulo": "", "autor": "X", "ano": 1000})
    assert r.status_code == 422
```

## ▶️ Experimente

```bash
fastapi dev main.py
curl -X POST localhost:8000/livros -H "Content-Type: application/json" \
     -d '{"titulo":"Python Fluente","autor":"Luciano Ramalho","ano":2023}'
curl "localhost:8000/livros?autor=ramalho"
```

Abra `http://127.0.0.1:8000/docs` para a documentação interativa.

## 🔍 Pontos importantes

- **`LivroIn` × `Livro`:** o cliente nunca envia `id`; herdamos para não repetir campos.
- **`exclude_unset=True`** é a chave do PATCH: distingue "não enviado" de "enviado como `None`".
- **Repositório isolado:** trocar por SQLite só altera `RepositorioLivros` (as rotas permanecem).
- **`response_model`** filtra e valida a saída — evita vazar campos internos.
- Rotas síncronas (`def`) rodam em *threadpool*; use `async def` apenas com bibliotecas assíncronas.

## 🌶️ Equivalente em Flask (resumo)

```python
from flask import Flask, jsonify, request, abort
app = Flask(__name__)
livros: dict[int, dict] = {}

@app.post("/livros")
def criar():
    dados = request.get_json(silent=True) or {}
    if not dados.get("titulo"):
        abort(422, "título obrigatório")        # validação manual
    ...
    return jsonify(livro), 201
```

---

⬅️ [[09 - Projetos Práticos/Projeto 05 - API REST|Projeto 05]] | ➡️ [[09 - Projetos Práticos/Projeto 06 - Bot|Projeto 06]]

#python #projeto #solucao #api #fastapi
