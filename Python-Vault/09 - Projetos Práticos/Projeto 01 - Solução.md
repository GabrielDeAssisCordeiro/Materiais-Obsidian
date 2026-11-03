---
titulo: "Projeto 01 – Solução: Calculadora CLI"
tags: [python, projeto, solucao, cli, calculadora]
nivel: iniciante
criado: 2026-10-14
projeto: 1
---

# ✅ Projeto 01 – Solução: Calculadora CLI

Enunciado: [[09 - Projetos Práticos/Projeto 01 - Calculadora CLI|Projeto 01]].

## 📁 Estrutura

```text
calculadora/
└── calculadora.py
```

## 💻 Código completo

```python
# arquivo: calculadora.py
"""Calculadora de linha de comando segura (sem eval)."""

import ast
import math
import operator
import sys

# Lista branca de operadores binários e unários
BINARIOS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
UNARIOS = {ast.USub: operator.neg, ast.UAdd: operator.pos}

FUNCOES = {"sqrt": math.sqrt, "abs": abs, "round": round}
CONSTANTES = {"pi": math.pi, "e": math.e}

LIMITE_EXPOENTE = 1000  # evita 9**9**9 travando a máquina


class ErroCalculo(Exception):
    """Erro de domínio: mensagem pronta para mostrar ao usuário."""


def avaliar(expressao: str, ambiente: dict | None = None) -> int | float:
    """Avalia uma expressão aritmética de forma segura."""
    ambiente = {**CONSTANTES, **(ambiente or {})}
    try:
        arvore = ast.parse(expressao.strip(), mode="eval")
    except SyntaxError as exc:
        raise ErroCalculo("expressão inválida") from exc
    try:
        return _avaliar(arvore.body, ambiente)
    except ZeroDivisionError as exc:
        raise ErroCalculo("divisão por zero") from exc
    except (ValueError, OverflowError, TypeError) as exc:
        raise ErroCalculo(f"erro de cálculo: {exc}") from exc


def _avaliar(no: ast.AST, amb: dict):
    match no:
        case ast.Constant(value=int() | float() as valor):
            return valor
        case ast.Name(id=nome):
            if nome in amb:
                return amb[nome]
            raise ErroCalculo(f"nome desconhecido: {nome!r}")
        case ast.UnaryOp(op=op, operand=operando) if type(op) in UNARIOS:
            return UNARIOS[type(op)](_avaliar(operando, amb))
        case ast.BinOp(left=esq, op=op, right=dir_) if type(op) in BINARIOS:
            a, b = _avaliar(esq, amb), _avaliar(dir_, amb)
            if isinstance(op, ast.Pow) and abs(b) > LIMITE_EXPOENTE:
                raise ErroCalculo("expoente grande demais")
            return BINARIOS[type(op)](a, b)
        case ast.Call(func=ast.Name(id=nome), args=args, keywords=[]) if nome in FUNCOES:
            return FUNCOES[nome](*(_avaliar(a, amb) for a in args))
        case _:
            raise ErroCalculo("operação não permitida")


def formatar(valor: int | float) -> str:
    if isinstance(valor, float) and valor.is_integer():
        return str(int(valor)) if abs(valor) < 1e15 else str(valor)
    return str(valor)


def repl() -> None:
    historico: list[str] = []
    ambiente: dict = {}
    print("Calculadora — digite 'historico' ou 'sair'.")
    while True:
        try:
            texto = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not texto:
            continue
        if texto in {"sair", "exit", "quit"}:
            break
        if texto == "historico":
            for i, linha in enumerate(historico, 1):
                print(f"{i:>3}. {linha}")
            continue
        try:
            resultado = avaliar(texto, ambiente)
        except ErroCalculo as erro:
            print(f"Erro: {erro}")
            continue
        ambiente["ans"] = resultado
        historico.append(f"{texto} = {formatar(resultado)}")
        print(formatar(resultado))


def main() -> int:
    if len(sys.argv) > 1:
        try:
            print(formatar(avaliar(" ".join(sys.argv[1:]))))
        except ErroCalculo as erro:
            print(f"Erro: {erro}", file=sys.stderr)
            return 1
        return 0
    repl()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 🔍 Pontos importantes

- **`match` estrutural** sobre nós `ast` ([[02 - Controle de Fluxo e Estruturas de Dados/01 - if elif else e match case|match/case]]): cada `case` descreve um formato de nó permitido; tudo o mais cai em `case _` → erro.
- **Lista branca:** só `BINARIOS`, `UNARIOS` e `FUNCOES` executam. `__import__('os')` vira `ast.Call` com nome fora de `FUNCOES` → recusado.
- **Exceções em camadas:** `ErroCalculo` é nossa exceção de domínio ([[05 - Tratamento de Erros e Arquivos/02 - Exceções Personalizadas|Exceções personalizadas]]); `raise ... from exc` preserva a causa.
- **Código de saída:** `main()` retorna `1` em erro, útil em scripts de shell.

## 🧪 Testes (pytest)

```python
# arquivo: test_calculadora.py
import pytest
from calculadora import avaliar, ErroCalculo


@pytest.mark.parametrize("expr, esperado", [
    ("2 + 3 * 4", 14),
    ("(2 + 3) * 4", 20),
    ("2 ** 10", 1024),
    ("sqrt(16) + 1", 5.0),
    ("-3 + 5", 2),
    ("10 // 3", 3),
])
def test_validas(expr, esperado):
    assert avaliar(expr) == esperado


@pytest.mark.parametrize("expr", ["10 / 0", "2 +", "__import__('os')", "9 ** 9 ** 9", "x + 1"])
def test_invalidas(expr):
    with pytest.raises(ErroCalculo):
        avaliar(expr)


def test_ans():
    assert avaliar("ans * 2", {"ans": 5}) == 10
```

---

⬅️ [[09 - Projetos Práticos/Projeto 01 - Calculadora CLI|Projeto 01]] | ➡️ [[09 - Projetos Práticos/Projeto 02 - To-Do com Arquivos|Projeto 02]]

#python #projeto #solucao #cli #ast #calculadora
