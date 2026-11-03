---
titulo: "Exercícios do Módulo 07"
tags: [python, intermediario, exercicios, funcional, decorators, generators]
nivel: intermediario
criado: 2026-10-09
modulo: "07 - Programação Funcional e Intermediário"
---

# 🧪 Exercícios do Módulo 07

> [!tip] Como usar
> Tente resolver **sem olhar** a solução (callouts recolhidos). Rode no REPL, use `breakpoint()` e, se possível, valide com `mypy`.

Notas de apoio: [[07 - Programação Funcional e Intermediário/01 - Funções de Ordem Superior|Ordem Superior]] · [[07 - Programação Funcional e Intermediário/02 - Lambda map filter reduce|Lambda/map/filter/reduce]] · [[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]] · [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|Generators]] · [[07 - Programação Funcional e Intermediário/05 - Context Managers Avançados|Context Managers]] · [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|Type Hints]]

## 🟢 Nível 1 – Aquecimento

> [!question] 1. `compor`
> Escreva `compor(*funcs)` que devolve uma função aplicando `funcs` da direita para a esquerda.

> [!success]- Solução
> ```python
> from functools import reduce
>
> def compor(*funcs):
>     return lambda x: reduce(lambda acc, f: f(acc), reversed(funcs), x)
>
> f = compor(str.upper, str.strip)
> print(f("  oi "))   # OI
> ```

> [!question] 2. Ordenação com `key`
> Ordene `["banana", "kiwi", "maçã"]` por tamanho e depois alfabeticamente.

> [!success]- Solução
> ```python
> frutas = ["banana", "kiwi", "maçã"]
> print(sorted(frutas, key=lambda s: (len(s), s)))
> ```

> [!question] 3. `map/filter/reduce`
> Dada `nums = range(1, 11)`, calcule o produto dos quadrados dos números ímpares.

> [!success]- Solução
> ```python
> from functools import reduce
> from operator import mul
> nums = range(1, 11)
> print(reduce(mul, map(lambda x: x*x, filter(lambda x: x % 2, nums)), 1))
> ```

## 🟡 Nível 2 – Decorators

> [!question] 4. `@repetir(n)`
> Decorator com parâmetro que executa a função `n` vezes e devolve a lista de resultados.

> [!success]- Solução
> ```python
> import functools
>
> def repetir(n):
>     def deco(func):
>         @functools.wraps(func)
>         def wrapper(*a, **kw):
>             return [func(*a, **kw) for _ in range(n)]
>         return wrapper
>     return deco
>
> @repetir(3)
> def oi(nome): return f"oi {nome}"
> print(oi("Ana"))
> ```

> [!question] 5. `@contar_chamadas`
> Decorator que guarda em `func.chamadas` quantas vezes foi chamada.

> [!success]- Solução
> ```python
> import functools
>
> def contar_chamadas(func):
>     @functools.wraps(func)
>     def wrapper(*a, **kw):
>         wrapper.chamadas += 1
>         return func(*a, **kw)
>     wrapper.chamadas = 0
>     return wrapper
>
> @contar_chamadas
> def f(): ...
> f(); f()
> print(f.chamadas)   # 2
> ```

> [!question] 6. `@retry`
> Decorator `retry(tentativas, excecoes=(Exception,))` que repete se houver exceção, relançando na última.

> [!success]- Solução
> ```python
> import functools, time
>
> def retry(tentativas=3, excecoes=(Exception,), espera=0.0):
>     def deco(func):
>         @functools.wraps(func)
>         def wrapper(*a, **kw):
>             for i in range(1, tentativas + 1):
>                 try:
>                     return func(*a, **kw)
>                 except excecoes:
>                     if i == tentativas:
>                         raise
>                     time.sleep(espera)
>         return wrapper
>     return deco
> ```

## 🟠 Nível 3 – Generators e Context Managers

> [!question] 7. `ler_em_blocos`
> Generator que lê um arquivo em blocos de `n` linhas (usando `itertools.batched`).

> [!success]- Solução
> ```python
> from itertools import batched
>
> def ler_em_blocos(caminho, n):
>     with open(caminho, encoding="utf-8") as f:
>         for bloco in batched(f, n):
>             yield [l.rstrip("\n") for l in bloco]
> ```

> [!question] 8. `@contextmanager` de timeout de log
> Crie `silencioso()` que redireciona `stdout` para o vazio durante o bloco.

> [!success]- Solução
> ```python
> import io
> from contextlib import contextmanager, redirect_stdout
>
> @contextmanager
> def silencioso():
>     with redirect_stdout(io.StringIO()):
>         yield
> ```

> [!question] 9. Fibonacci até limite
> Generator `fib_ate(limite)` que gera Fibonacci enquanto `<= limite`.

> [!success]- Solução
> ```python
> def fib_ate(limite):
>     a, b = 0, 1
>     while a <= limite:
>         yield a
>         a, b = b, a + b
> print(list(fib_ate(50)))
> ```

## 🔴 Nível 4 – Tipos

> [!question] 10. Cache genérico tipado
> Escreva `class Cache[K, V]` com `get(k) -> V | None` e `set(k, v)`.

> [!success]- Solução
> ```python
> class Cache[K, V]:
>     def __init__(self) -> None:
>         self._d: dict[K, V] = {}
>     def get(self, k: K) -> V | None:
>         return self._d.get(k)
>     def set(self, k: K, v: V) -> None:
>         self._d[k] = v
>
> c: Cache[str, int] = Cache()
> c.set("a", 1)
> ```

> [!question] 11. Decorator tipado
> Tipifique corretamente o decorator `@cronometrar` preservando a assinatura (`ParamSpec`).

> [!success]- Solução
> ```python
> import functools, time
> from collections.abc import Callable
>
> def cronometrar[**P, R](f: Callable[P, R]) -> Callable[P, R]:
>     @functools.wraps(f)
>     def w(*a: P.args, **kw: P.kwargs) -> R:
>         t = time.perf_counter()
>         try:
>             return f(*a, **kw)
>         finally:
>             print(f"{f.__name__}: {time.perf_counter()-t:.4f}s")
>     return w
> ```

## 🏗️ Mini-projeto: Pipeline de dados lazy

**Objetivo:** processar um CSV grande sem carregá-lo todo na memória, usando generators, decorators e context managers.

Requisitos:
1. Generator `ler_csv(caminho)` que gera dicionários (use `csv.DictReader`).
2. Generators `filtrar(registros, predicado)` e `transformar(registros, func)`.
3. Decorator `@medir` que imprime o tempo da função final.
4. Context manager `saida_csv(caminho, campos)` que abre o arquivo e entrega uma função `escrever(registro)`.
5. Tipos anotados e `mypy` limpo.

> [!success]- Solução
> ```python
> import csv, functools, time
> from collections.abc import Callable, Iterable, Iterator
> from contextlib import contextmanager
> from pathlib import Path
>
> type Registro = dict[str, str]
>
> def medir[**P, R](f: Callable[P, R]) -> Callable[P, R]:
>     @functools.wraps(f)
>     def w(*a: P.args, **kw: P.kwargs) -> R:
>         t = time.perf_counter()
>         try:
>             return f(*a, **kw)
>         finally:
>             print(f"{f.__name__}: {time.perf_counter() - t:.3f}s")
>     return w
>
> def ler_csv(caminho: Path) -> Iterator[Registro]:
>     with caminho.open(newline="", encoding="utf-8") as f:
>         yield from csv.DictReader(f)
>
> def filtrar(regs: Iterable[Registro],
>             pred: Callable[[Registro], bool]) -> Iterator[Registro]:
>     return (r for r in regs if pred(r))
>
> def transformar(regs: Iterable[Registro],
>                 func: Callable[[Registro], Registro]) -> Iterator[Registro]:
>     return (func(r) for r in regs)
>
> @contextmanager
> def saida_csv(caminho: Path, campos: list[str]):
>     with caminho.open("w", newline="", encoding="utf-8") as f:
>         w = csv.DictWriter(f, fieldnames=campos)
>         w.writeheader()
>         yield w.writerow
>
> @medir
> def main(entrada: Path, saida: Path) -> None:
>     regs = ler_csv(entrada)
>     regs = filtrar(regs, lambda r: float(r["valor"]) > 100)
>     regs = transformar(regs, lambda r: {**r, "nome": r["nome"].upper()})
>     with saida_csv(saida, ["nome", "valor"]) as escrever:
>         for r in regs:
>             escrever(r)
> ```

## 📝 Quiz rápido

> [!question] Q1. O que `next(g)` faz em um generator esgotado?
> a) retorna `None`  b) levanta `StopIteration`  c) reinicia  d) retorna `[]`

> [!success]- Resposta
> **b)** — salvo se passar um valor padrão: `next(g, None)`.

> [!question] Q2. Qual a ordem de aplicação em `@a @b def f()`?
> a) `a(b(f))`  b) `b(a(f))`

> [!success]- Resposta
> **a)** — `b` decora primeiro; na chamada, `a` executa por fora.

> [!question] Q3. `Optional[int]` equivale a…
> a) `int` opcional como parâmetro  b) `int | None`

> [!success]- Resposta
> **b)**.

> [!question] Q4. O que acontece se `__exit__` retornar `True`?
> a) nada  b) a exceção é suprimida

> [!success]- Resposta
> **b)**.

> [!question] Q5. `lambda` pode conter…
> a) várias instruções  b) apenas uma expressão

> [!success]- Resposta
> **b)**.

## ✅ Checklist do módulo

- [ ] Sei passar e retornar funções
- [ ] Domino `map`, `filter`, `reduce` e sei quando preferir comprehensions
- [ ] Escrevo decorators com e sem parâmetros usando `functools.wraps`
- [ ] Entendo iteráveis vs. iteradores e uso `yield`
- [ ] Uso `@contextmanager` e `ExitStack`
- [ ] Anoto código com generics, `Protocol` e `TypedDict` e rodo `mypy`

## 🚀 Próximo módulo

➡️ [[08 - Avançado/01 - Metaprogramação|Módulo 08 – Avançado: Metaprogramação]]

---

⬅️ [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|Type Hints e typing]]

#python #intermediario #exercicios #funcional #decorators #generators #typing
