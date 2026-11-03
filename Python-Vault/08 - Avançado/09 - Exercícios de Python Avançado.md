---
titulo: "Exercícios do Módulo 08"
tags: [python, avancado, exercicios]
nivel: avancado
criado: 2026-10-09
modulo: "08 - Avançado"
---

# 🧪 Exercícios do Módulo 08

Notas de apoio: [[08 - Avançado/01 - Metaprogramação|Metaprogramação]] · [[08 - Avançado/02 - Asyncio|Asyncio]] · [[08 - Avançado/03 - Multiprocessing|Multiprocessing]] · [[08 - Avançado/04 - CPython Internals|CPython]] · [[08 - Avançado/05 - Performance e Profiling|Performance]] · [[08 - Avançado/06 - Testes com unittest e pytest|Testes]] · [[08 - Avançado/07 - Packaging e Distribuição|Packaging]] · [[08 - Avançado/08 - Design Patterns Avançados e Clean Code|Patterns]]

> [!tip] Como usar
> Resolva sem olhar. Para cada exercício, escreva um **teste pytest** antes ou depois, meça com `timeit` quando falar de desempenho e rode `mypy`.

## 🟢 Nível 1

> [!question] 1. Descriptor `Tipado(tipo)`
> Crie um descriptor que só aceita valores do tipo informado e use-o em uma classe `Pessoa` (`nome: str`, `idade: int`).

> [!success]- Solução
> ```python
> class Tipado:
>     def __init__(self, tipo): self.tipo = tipo
>     def __set_name__(self, dono, nome): self.nome = nome
>     def __get__(self, obj, t=None):
>         return self if obj is None else obj.__dict__[self.nome]
>     def __set__(self, obj, v):
>         if not isinstance(v, self.tipo):
>             raise TypeError(f"{self.nome} deve ser {self.tipo.__name__}")
>         obj.__dict__[self.nome] = v
>
> class Pessoa:
>     nome = Tipado(str)
>     idade = Tipado(int)
>     def __init__(self, nome, idade):
>         self.nome, self.idade = nome, idade
> ```

> [!question] 2. Teste com pytest
> Escreva testes parametrizados para o descriptor acima (casos válidos e inválidos).

> [!success]- Solução
> ```python
> import pytest
>
> @pytest.mark.parametrize("nome, idade", [("Ana", 30), ("", 0)])
> def test_ok(nome, idade):
>     p = Pessoa(nome, idade)
>     assert (p.nome, p.idade) == (nome, idade)
>
> @pytest.mark.parametrize("nome, idade", [(1, 30), ("Ana", "30"), (None, None)])
> def test_erro(nome, idade):
>     with pytest.raises(TypeError):
>         Pessoa(nome, idade)
> ```

## 🟡 Nível 2

> [!question] 3. Registro automático
> Com `__init_subclass__`, faça `Comando` registrar subclasses por nome e crie `executar(nome)`.

> [!success]- Solução
> ```python
> class Comando:
>     registro: dict[str, type["Comando"]] = {}
>     def __init_subclass__(cls, **kw):
>         super().__init_subclass__(**kw)
>         Comando.registro[cls.__name__.lower()] = cls
>     def rodar(self): raise NotImplementedError
>
> class Ola(Comando):
>     def rodar(self): print("olá!")
>
> def executar(nome): Comando.registro[nome]().rodar()
> executar("ola")
> ```

> [!question] 4. Downloads limitados
> Simule 30 downloads (`asyncio.sleep(random)`) com no máximo 5 simultâneos, com timeout de 2 s cada, e imprima quantos deram timeout.

> [!success]- Solução
> ```python
> import asyncio, random
>
> async def baixar(i, sem):
>     async with sem:
>         try:
>             async with asyncio.timeout(2):
>                 await asyncio.sleep(random.uniform(0.1, 3))
>             return True
>         except TimeoutError:
>             return False
>
> async def main():
>     sem = asyncio.Semaphore(5)
>     res = await asyncio.gather(*(baixar(i, sem) for i in range(30)))
>     print("timeouts:", res.count(False))
>
> asyncio.run(main())
> ```

> [!question] 5. CPU em paralelo
> Calcule `fib(32)` ingênuo para 8 entradas com `ProcessPoolExecutor` e compare com sequencial.

> [!success]- Solução
> ```python
> import time
> from concurrent.futures import ProcessPoolExecutor
>
> def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
>
> if __name__ == "__main__":
>     xs = [32] * 8
>     t = time.perf_counter(); [fib(x) for x in xs]
>     print("seq", round(time.perf_counter() - t, 2))
>     t = time.perf_counter()
>     with ProcessPoolExecutor() as ex: list(ex.map(fib, xs))
>     print("par", round(time.perf_counter() - t, 2))
> ```

## 🔴 Nível 3

> [!question] 6. Profile e otimize
> A função abaixo é lenta. Perfile, identifique o gargalo e otimize (meça antes e depois).
> ```python
> def duplicados(lista):
>     return [x for i, x in enumerate(lista) if x in lista[:i]]
> ```

> [!success]- Solução
> O gargalo é `x in lista[:i]` (O(n²) e cria cópias).
> ```python
> def duplicados(lista):
>     vistos, dup = set(), []
>     for x in lista:
>         if x in vistos:
>             dup.append(x)
>         else:
>             vistos.add(x)
>     return dup
> ```
> Mantém a mesma saída (cada repetição aparece a cada reocorrência) em O(n).

> [!question] 7. Metaclass de validação
> Crie uma metaclass que proíbe subclasses de definirem métodos com nome em `camelCase` (ex: `meuMetodo`).

> [!success]- Solução
> ```python
> import re
>
> class SoSnake(type):
>     def __new__(mcs, nome, bases, ns):
>         for k, v in ns.items():
>             if callable(v) and re.search(r"[a-z][A-Z]", k):
>                 raise TypeError(f"{nome}.{k}: use snake_case")
>         return super().__new__(mcs, nome, bases, ns)
> ```

## 🏗️ Mini-projeto: Pacote `cachetools_mini`

**Objetivo:** criar um pequeno pacote instalável com decoradores de cache, totalmente testado e tipado.

Requisitos:
1. Layout `src/` e `pyproject.toml` (setuptools ou uv/poetry).
2. Decorator `@ttl_cache(segundos)` com `ParamSpec` ([[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]]).
3. Método `.cache_clear()` e `.cache_info()` no wrapper.
4. Testes pytest com `monkeypatch` simulando o tempo (sem `sleep` real).
5. `mypy --strict` limpo, cobertura ≥ 90%.
6. Comando CLI `cachetools-demo` em `[project.scripts]`.
7. `python -m build` e instalação do wheel num venv limpo.

> [!success]- Solução (núcleo)
> ```python
> # src/cachetools_mini/__init__.py
> import functools, time
> from collections.abc import Callable, Hashable
> from typing import Any
>
> def ttl_cache[**P, R](segundos: float, relogio: Callable[[], float] = time.monotonic):
>     def deco(func: Callable[P, R]) -> Callable[P, R]:
>         cache: dict[Hashable, tuple[float, R]] = {}
>         stats = {"hits": 0, "misses": 0}
>
>         @functools.wraps(func)
>         def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
>             chave = (args, tuple(sorted(kwargs.items())))
>             agora = relogio()
>             if chave in cache and agora - cache[chave][0] < segundos:
>                 stats["hits"] += 1
>                 return cache[chave][1]
>             stats["misses"] += 1
>             r = func(*args, **kwargs)
>             cache[chave] = (agora, r)
>             return r
>
>         wrapper.cache_clear = cache.clear            # type: ignore[attr-defined]
>         wrapper.cache_info = lambda: dict(stats)     # type: ignore[attr-defined]
>         return wrapper
>     return deco
> ```
> ```python
> # tests/test_ttl.py
> from cachetools_mini import ttl_cache
>
> def test_expira():
>     t = [0.0]
>     chamadas = []
>
>     @ttl_cache(10, relogio=lambda: t[0])
>     def f(x):
>         chamadas.append(x)
>         return x * 2
>
>     assert f(2) == 4 and f(2) == 4
>     assert chamadas == [2]
>     t[0] = 11
>     f(2)
>     assert chamadas == [2, 2]
> ```
> Injetar o `relogio` evita `sleep` nos testes (dependency injection).

## 📝 Quiz

> [!question] Q1. Qual método do descriptor roda ao atribuir `obj.x = 1`?
> a) `__get__` b) `__set__` c) `__set_name__`

> [!success]- Resposta
> **b)**.

> [!question] Q2. Threads aceleram laço de CPU puro em CPython (com GIL)?
> a) Sim b) Não

> [!success]- Resposta
> **b)** Use processos (ou o build free-threaded experimental).

> [!question] Q3. `time.sleep(1)` dentro de `async def` faz…
> a) cede ao loop b) bloqueia todo o loop

> [!success]- Resposta
> **b)**. Use `await asyncio.sleep(1)`.

> [!question] Q4. Qual comando gera wheel e sdist?
> a) `pip build` b) `python -m build`

> [!success]- Resposta
> **b)**.

> [!question] Q5. O primeiro passo para otimizar é…
> a) reescrever em C b) medir/perfilar

> [!success]- Resposta
> **b)**.

## ✅ Checklist

- [ ] Sei criar descriptors e usar `__init_subclass__`; entendo quando uma metaclass é necessária
- [ ] Escrevo programas `asyncio` com `TaskGroup`, timeouts e semáforos
- [ ] Escolho entre threads, processos e asyncio conforme o gargalo
- [ ] Entendo GIL, refcount e GC
- [ ] Uso `timeit` e `cProfile` antes de otimizar
- [ ] Escrevo testes com pytest (fixtures, parametrize, mocks)
- [ ] Empacoto e publico com `pyproject.toml`
- [ ] Aplico SOLID e clean code de forma pragmática

## 🚀 Próximo módulo

➡️ [[09 - Projetos Práticos/Projeto 01 - Calculadora CLI|Módulo 09 – Projetos Práticos]]

---

⬅️ [[08 - Avançado/08 - Design Patterns Avançados e Clean Code|Design Patterns Avançados e Clean Code]]

#python #avancado #exercicios #asyncio #pytest #packaging
