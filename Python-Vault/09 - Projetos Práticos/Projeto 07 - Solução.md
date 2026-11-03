---
titulo: "Projeto 07 – Solução: Login com SQLite"
tags: [python, projeto, solucao, sqlite, seguranca]
nivel: intermediario
criado: 2026-10-14
projeto: 7
---

# ✅ Projeto 07 – Solução: Login com SQLite

Enunciado: [[09 - Projetos Práticos/Projeto 07 - Login com SQLite|Projeto 07]].

## 💻 `auth.py`

```python
# arquivo: auth.py
"""Autenticação com SQLite, scrypt e bloqueio contra força bruta."""

from __future__ import annotations

import getpass
import hashlib
import hmac
import os
import re
import sqlite3
import time

# Parâmetros do scrypt (custo de CPU/memória ≈ 16 MiB)
N, R, P = 2**14, 8, 1
MAX_FALHAS = 5
BLOQUEIO_SEGUNDOS = 300

SCHEMA = """
CREATE TABLE IF NOT EXISTS usuarios (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario       TEXT NOT NULL UNIQUE COLLATE NOCASE,
    senha_hash    TEXT NOT NULL,
    criado_em     TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    falhas        INTEGER NOT NULL DEFAULT 0,
    bloqueado_ate REAL NOT NULL DEFAULT 0
);
"""


# ---------- Exceções ----------
class ErroAuth(Exception):
    """Base para erros de autenticação."""


class DadosInvalidos(ErroAuth): ...
class SenhaFraca(ErroAuth): ...
class UsuarioExistente(ErroAuth): ...
class CredenciaisInvalidas(ErroAuth): ...


class ContaBloqueada(ErroAuth):
    def __init__(self, restante: int):
        super().__init__(f"conta bloqueada; tente novamente em {restante}s")
        self.restante = restante


# ---------- Hash ----------
def hash_senha(senha: str, salt: bytes | None = None) -> str:
    salt = salt or os.urandom(16)
    h = hashlib.scrypt(senha.encode(), salt=salt, n=N, r=R, p=P, dklen=32)
    return f"scrypt${N}${R}${P}${salt.hex()}${h.hex()}"


def verificar_senha(senha: str, armazenado: str) -> bool:
    try:
        alg, n, r, p, salt_hex, hash_hex = armazenado.split("$")
        if alg != "scrypt":
            return False
        esperado = bytes.fromhex(hash_hex)
        calculado = hashlib.scrypt(
            senha.encode(), salt=bytes.fromhex(salt_hex),
            n=int(n), r=int(r), p=int(p), dklen=len(esperado),
        )
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(calculado, esperado)   # tempo constante


# Hash "falso": usado quando o usuário não existe, para igualar o tempo de resposta
_HASH_FALSO = hash_senha("senha-falsa-para-igualar-tempo")


# ---------- Banco ----------
def conectar(caminho: str = "usuarios.db") -> sqlite3.Connection:
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


# ---------- Regras ----------
def validar_usuario(usuario: str) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", usuario):
        raise DadosInvalidos("usuário: 3 a 20 caracteres (letras, números e _)")


def validar_senha(senha: str) -> None:
    if len(senha) < 8 or not re.search(r"[A-Za-z]", senha) or not re.search(r"\d", senha):
        raise SenhaFraca("senha: mínimo 8 caracteres, com letras e números")


def registrar(conn: sqlite3.Connection, usuario: str, senha: str) -> None:
    validar_usuario(usuario)
    validar_senha(senha)
    try:
        with conn:  # transação: commit ou rollback automático
            conn.execute(
                "INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)",
                (usuario, hash_senha(senha)),
            )
    except sqlite3.IntegrityError:
        raise UsuarioExistente("esse usuário já existe") from None


def login(conn: sqlite3.Connection, usuario: str, senha: str,
          agora: float | None = None) -> dict:
    agora = time.time() if agora is None else agora
    linha = conn.execute(
        "SELECT id, usuario, senha_hash, falhas, bloqueado_ate FROM usuarios WHERE usuario = ?",
        (usuario,),
    ).fetchone()

    if linha is None:
        verificar_senha(senha, _HASH_FALSO)          # gasta o mesmo tempo
        raise CredenciaisInvalidas("usuário ou senha inválidos")

    if linha["bloqueado_ate"] > agora:
        raise ContaBloqueada(int(linha["bloqueado_ate"] - agora) + 1)

    if not verificar_senha(senha, linha["senha_hash"]):
        falhas = linha["falhas"] + 1
        bloqueio = agora + BLOQUEIO_SEGUNDOS if falhas >= MAX_FALHAS else 0
        with conn:
            conn.execute(
                "UPDATE usuarios SET falhas = ?, bloqueado_ate = ? WHERE id = ?",
                (0 if bloqueio else falhas, bloqueio, linha["id"]),
            )
        # (o 'with' já confirmou a gravação; só então levantamos a exceção)
        raise CredenciaisInvalidas("usuário ou senha inválidos")

    with conn:
        conn.execute("UPDATE usuarios SET falhas = 0, bloqueado_ate = 0 WHERE id = ?",
                     (linha["id"],))
    return {"id": linha["id"], "usuario": linha["usuario"]}


# ---------- Interface de terminal ----------
def menu() -> None:
    conn = conectar()
    try:
        while True:
            print("\n1) Cadastrar  2) Entrar  0) Sair")
            opcao = input("> ").strip()
            if opcao == "0":
                break
            if opcao not in {"1", "2"}:
                print("Opção inválida.")
                continue
            usuario = input("Usuário: ").strip()
            senha = getpass.getpass("Senha: ")
            try:
                if opcao == "1":
                    registrar(conn, usuario, senha)
                    print("✅ Cadastro realizado!")
                else:
                    dados = login(conn, usuario, senha)
                    print(f"✅ Bem-vindo(a), {dados['usuario']}!")
            except ErroAuth as erro:
                print(f"❌ {erro}")
    finally:
        conn.close()


if __name__ == "__main__":
    menu()
```

## 🧪 `test_auth.py`

```python
# arquivo: test_auth.py
import pytest
import auth


@pytest.fixture
def conn():
    c = auth.conectar(":memory:")
    yield c
    c.close()


def test_hash_diferente_por_salt():
    assert auth.hash_senha("abc12345") != auth.hash_senha("abc12345")


def test_verificar():
    h = auth.hash_senha("segredo123")
    assert auth.verificar_senha("segredo123", h)
    assert not auth.verificar_senha("errada123", h)
    assert not auth.verificar_senha("x", "lixo")


def test_cadastro_e_login(conn):
    auth.registrar(conn, "Ana_01", "segredo123")
    assert auth.login(conn, "ana_01", "segredo123")["usuario"] == "Ana_01"   # NOCASE


def test_duplicado(conn):
    auth.registrar(conn, "ana", "segredo123")
    with pytest.raises(auth.UsuarioExistente):
        auth.registrar(conn, "ANA", "outrasenha1")


@pytest.mark.parametrize("senha", ["curta1", "somenteletras", "12345678"])
def test_senha_fraca(conn, senha):
    with pytest.raises(auth.SenhaFraca):
        auth.registrar(conn, "bia", senha)


def test_injection_nao_funciona(conn):
    auth.registrar(conn, "ana", "segredo123")
    with pytest.raises(auth.CredenciaisInvalidas):
        auth.login(conn, "x' OR '1'='1", "qualquer123")


def test_bloqueio(conn):
    auth.registrar(conn, "ana", "segredo123")
    t = 1_000_000.0
    for _ in range(auth.MAX_FALHAS):
        with pytest.raises(auth.CredenciaisInvalidas):
            auth.login(conn, "ana", "errada123", agora=t)
    with pytest.raises(auth.ContaBloqueada):
        auth.login(conn, "ana", "segredo123", agora=t + 10)       # mesmo com a senha certa
    assert auth.login(conn, "ana", "segredo123", agora=t + 301)   # passou o bloqueio
```

## 🔍 Pontos importantes

- **scrypt é lento de propósito:** atacantes que roubem o banco precisam de muito tempo/memória por tentativa.
- **Salt único** por usuário: senhas iguais geram hashes diferentes.
- **`hmac.compare_digest`** evita *timing attacks*.
- **`with conn:`** do `sqlite3` controla a **transação** (commit/rollback) — mas **não fecha** a conexão. Por isso `conn.close()` no `finally` ([[07 - Programação Funcional e Intermediário/05 - Context Managers Avançados|Context Managers]]).
- **Hash falso** quando o usuário não existe: sem ele, a resposta seria muito mais rápida e revelaria quais usuários existem.
- **Em produção:** HTTPS, *rate limit* por IP, 2FA, e bibliotecas consolidadas (argon2/bcrypt).

---

⬅️ [[09 - Projetos Práticos/Projeto 07 - Login com SQLite|Projeto 07]] | ➡️ [[09 - Projetos Práticos/Projeto 08 - Projeto Final|Projeto 08]]

#python #projeto #solucao #sqlite #seguranca #hash
