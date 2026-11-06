---
titulo: "Exercícios de Funções e Modularização"
tags: [python, basico, exercicios, pratica, funcoes]
nivel: iniciante
criado: 2026-10-05
modulo: "03 - Funções e Modularização"
---

# 🏋️ Exercícios de Funções e Modularização

Exercícios **progressivos** para fixar o **Módulo 03**. Resolva sozinho(a) antes de abrir cada solução.

> [!tip] Como praticar
> 1. Crie um **ambiente virtual** para o módulo (`python -m venv .venv`), como em [[03 - Funções e Modularização/05 - Virtual Environments e pip|Virtual Environments e pip]].
> 2. Escreva cada solução com **docstring** ([[03 - Funções e Modularização/06 - Docstrings|Docstrings]]) e teste com valores comuns **e** extremos.
> 3. Use o **debugger** (`F11` entra na função) quando algo não bater.

**Revise antes:** [[03 - Funções e Modularização/01 - Definindo Funções|Funções]] · [[03 - Funções e Modularização/02 - args kwargs e Argumentos Padrão|args/kwargs]] · [[03 - Funções e Modularização/03 - Escopo e Closures|Escopo e Closures]] · [[03 - Funções e Modularização/04 - Módulos e Packages|Módulos e Packages]]

---

## 🟢 Nível 1: Aquecimento

> [!question] 1. Maior de dois
> Escreva `maior(a, b)` que **retorne** o maior valor, sem usar `max()`.

> [!success]- Solução
> ```python
> def maior(a, b):
>     """Retorna o maior entre a e b."""
>     return a if a >= b else b
> ```

> [!question] 2. Contador de vogais
> Escreva `contar_vogais(texto)` que retorne quantas vogais (com acentos) o texto tem.

> [!success]- Solução
> ```python
> def contar_vogais(texto):
>     """Conta as vogais (com ou sem acento) de um texto."""
>     return sum(1 for c in texto.lower() if c in "aeiouáàâãéêíóôõúü")
> ```

> [!question] 3. Saudação flexível
> Escreva `saudar(nome, saudacao="Olá", pontuacao="!")` e chame de 4 formas diferentes (posicional, nomeada, mista, só o obrigatório).

> [!success]- Solução
> ```python
> def saudar(nome, saudacao="Olá", pontuacao="!"):
>     """Monta uma saudação."""
>     return f"{saudacao}, {nome}{pontuacao}"
>
> print(saudar("Ada"))
> print(saudar("Ada", "Oi"))
> print(saudar("Ada", pontuacao="."))
> print(saudar(saudacao="Bom dia", nome="Ada"))
> ```

---

## 🟡 Nível 2: Retorno e argumentos

> [!question] 4. Estatísticas
> Escreva `estatisticas(*numeros)` que devolva `(menor, maior, média)`. Se não houver números, devolva `None`.

> [!success]- Solução
> ```python
> def estatisticas(*numeros):
>     """Devolve (menor, maior, média) ou None se não houver números."""
>     if not numeros:
>         return None
>     return min(numeros), max(numeros), sum(numeros) / len(numeros)
>
> menor, maior, media = estatisticas(4, 9, 1, 7)
> ```

> [!question] 5. Corrigindo o padrão mutável
> Corrija sem alterar o comportamento esperado (cada chamada sem `lista` deve começar com lista vazia):
> ```python
> def registrar(evento, historico=[]):
>     historico.append(evento)
>     return historico
> ```

> [!success]- Solução
> ```python
> def registrar(evento, historico=None):
>     """Adiciona o evento ao histórico (cria um novo se não for informado)."""
>     if historico is None:
>         historico = []
>     historico.append(evento)
>     return historico
> ```

> [!question] 6. Montando tags HTML
> Escreva `tag(nome, conteudo, **atributos)` que gere `<a href="x" id="y">texto</a>`. Use `class_` para o atributo `class`.

> [!success]- Solução
> ```python
> def tag(nome, conteudo, **atributos):
>     """Gera uma tag HTML simples."""
>     attrs = "".join(f' {k.rstrip("_")}="{v}"' for k, v in atributos.items())
>     return f"<{nome}{attrs}>{conteudo}</{nome}>"
>
> print(tag("a", "texto", href="x", id="y"))
> ```

> [!question] 7. Somente nomeados
> Crie `formatar_preco(valor, *, moeda="R$", casas=2)` e mostre por que `formatar_preco(5, "US$")` falha.

> [!success]- Solução
> ```python
> def formatar_preco(valor, *, moeda="R$", casas=2):
>     """Formata um valor monetário."""
>     return f"{moeda} {valor:,.{casas}f}"
>
> formatar_preco(1234.5)                  # 'R$ 1,234.50'
> formatar_preco(5, moeda="US$")          # ✅
> formatar_preco(5, "US$")                # ❌ TypeError: só aceita 1 posicional
> ```

---

## 🟠 Nível 3: Escopo, closures e recursão

> [!question] 8. Contador com closure
> Escreva `criar_contador(passo=1)` que devolva uma função; cada chamada incrementa o valor em `passo` e o retorna. Mostre que dois contadores são independentes.

> [!success]- Solução
> ```python
> def criar_contador(passo=1):
>     """Cria um contador independente que avança de `passo` em `passo`."""
>     valor = 0
>
>     def proximo():
>         nonlocal valor
>         valor += passo
>         return valor
>
>     return proximo
>
> a = criar_contador()
> b = criar_contador(10)
> print(a(), a(), b(), b())    # 1 2 10 20
> ```

> [!question] 9. Fábrica de validadores
> Escreva `entre(minimo, maximo)` que retorne uma função `validar(n)` (True se `minimo <= n <= maximo`). Use-a com `filter`.

> [!success]- Solução
> ```python
> def entre(minimo, maximo):
>     """Cria um validador de intervalo fechado."""
>     def validar(n):
>         return minimo <= n <= maximo
>     return validar
>
> adulto = entre(18, 64)
> print(list(filter(adulto, [10, 18, 30, 70])))   # [18, 30]
> ```

> [!question] 10. Descubra o erro de escopo
> Por que falha, e como corrigir de duas formas (uma com `global`, outra **melhor**, sem ele)?
> ```python
> pontos = 0
> def marcar(valor):
>     pontos += valor
> marcar(10)
> ```

> [!success]- Solução
> `pontos += valor` é uma atribuição ⇒ `pontos` vira local ⇒ `UnboundLocalError`.
> ```python
> # Com global (evite)
> pontos = 0
> def marcar(valor):
>     global pontos
>     pontos += valor
>
> # Melhor: sem estado global
> def marcar(pontos, valor):
>     return pontos + valor
> pontos = marcar(pontos, 10)
> ```

> [!question] 11. Late binding
> Corrija para que imprima `[0, 10, 20]`:
> ```python
> fs = [lambda: i * 10 for i in range(3)]
> print([f() for f in fs])      # [20, 20, 20]
> ```

> [!success]- Solução
> ```python
> fs = [lambda i=i: i * 10 for i in range(3)]
> print([f() for f in fs])      # [0, 10, 20]
> ```

> [!question] 12. Recursão: soma de dígitos e potência
> Escreva, **recursivamente**: `soma_digitos(n)` (`1234` → `10`) e `potencia(base, exp)`.

> [!success]- Solução
> ```python
> def soma_digitos(n):
>     """Soma os dígitos de um inteiro não negativo."""
>     if n < 10:
>         return n
>     return n % 10 + soma_digitos(n // 10)
>
> def potencia(base, exp):
>     """Calcula base ** exp (exp inteiro >= 0)."""
>     if exp == 0:
>         return 1
>     return base * potencia(base, exp - 1)
>
> print(soma_digitos(1234), potencia(2, 10))   # 10 1024
> ```

---

## 🔴 Nível 4: Módulos, packages e desafios

> [!question] 13. Seu primeiro módulo
> Crie `conversores.py` com `celsius_para_fahrenheit`, `km_para_milhas` e `kg_para_libras`. Inclua docstring de módulo, docstrings nas funções e um bloco `if __name__ == "__main__":` com *asserts*. Depois importe em `main.py` de **três** formas.

> [!success]- Solução
> ```python
> # conversores.py
> """Conversores de unidades."""
>
> def celsius_para_fahrenheit(c):
>     """Converte °C em °F."""
>     return c * 9 / 5 + 32
>
> def km_para_milhas(km):
>     """Converte quilômetros em milhas."""
>     return km * 0.621371
>
> def kg_para_libras(kg):
>     """Converte quilos em libras."""
>     return kg * 2.20462
>
> if __name__ == "__main__":
>     assert celsius_para_fahrenheit(0) == 32
>     assert round(km_para_milhas(10), 2) == 6.21
>     print("Testes ok")
> ```
> ```python
> # main.py
> import conversores
> from conversores import km_para_milhas
> import conversores as conv
>
> print(conversores.celsius_para_fahrenheit(100))
> print(km_para_milhas(5))
> print(conv.kg_para_libras(70))
> ```

> [!question] 14. Package `utils`
> Monte o package `utils/` com `texto.py` (`inverter`, `eh_palindromo`) e `numeros.py` (`eh_primo`, `fatorial`). O `__init__.py` deve permitir `from utils import eh_primo, inverter`. Rode um `main.py` na raiz.

> [!success]- Solução
> ```text
> projeto/
> ├── main.py
> └── utils/
>     ├── __init__.py
>     ├── texto.py
>     └── numeros.py
> ```
> ```python
> # utils/texto.py
> def inverter(texto):
>     """Inverte o texto."""
>     return texto[::-1]
>
> def eh_palindromo(texto):
>     """Indica se o texto é palíndromo."""
>     limpo = "".join(c.lower() for c in texto if c.isalnum())
>     return limpo == limpo[::-1]
> ```
> ```python
> # utils/numeros.py
> def eh_primo(n):
>     """Indica se n é primo."""
>     if n < 2:
>         return False
>     return all(n % d for d in range(2, int(n ** 0.5) + 1))
>
> def fatorial(n):
>     """Calcula n!."""
>     resultado = 1
>     for i in range(2, n + 1):
>         resultado *= i
>     return resultado
> ```
> ```python
> # utils/__init__.py
> from .texto import inverter, eh_palindromo
> from .numeros import eh_primo, fatorial
>
> __all__ = ["inverter", "eh_palindromo", "eh_primo", "fatorial"]
> ```
> ```python
> # main.py
> from utils import eh_primo, inverter
> print(eh_primo(13), inverter("Python"))
> ```

> [!question] 15. Memoização com closure
> Escreva `memoizar(func)` que devolva uma versão de `func` que **guarda resultados** em um dicionário. Aplique em uma `fibonacci` recursiva e compare o tempo para `n = 35`. (Dica: `time.perf_counter()`.)

> [!success]- Solução
> ```python
> import time
>
> def memoizar(func):
>     """Devolve func com cache de resultados por argumento."""
>     cache = {}
>
>     def interna(n):
>         if n not in cache:
>             cache[n] = func(n)
>         return cache[n]
>
>     return interna
>
> def fib(n):
>     return n if n < 2 else fib(n - 1) + fib(n - 2)
>
> t = time.perf_counter()
> fib(32)
> print(f"Sem cache: {time.perf_counter() - t:.2f}s")
>
> @memoizar            # sintaxe de decorator; veja o Módulo 07
> def fib_rapido(n):
>     return n if n < 2 else fib_rapido(n - 1) + fib_rapido(n - 2)
>
> t = time.perf_counter()
> fib_rapido(300)
> print(f"Com cache: {time.perf_counter() - t:.6f}s")
> ```
> A biblioteca padrão já traz isso pronto: `functools.cache` ([[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|functools]]). O `@` será explicado em [[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]].

> [!question] 16. Descubra os bugs
> ```python
> # (a)
> def total(precos):
>     soma = 0
>     for p in precos:
>         soma += p
>         return soma
>
> # (b)
> def adicionar(x, destino=[]):
>     destino.append(x)
>     return destino
>
> # (c)
> def dobrar(lista):
>     for i in range(len(lista)):
>         lista[i] *= 2
>     return lista
> original = [1, 2, 3]
> novo = dobrar(original)       # queria preservar "original"
>
> # (d)
> def f(a=1, b):
>     return a + b
>
> # (e)  (arquivo chamado random.py)
> import random
> print(random.randint(1, 6))
> ```

> [!success]- Solução
> ```python
> # (a) return dentro do for: devolve após o 1º item
> def total(precos):
>     soma = 0
>     for p in precos:
>         soma += p
>     return soma               # (ou sum(precos))
>
> # (b) padrão mutável compartilhado
> def adicionar(x, destino=None):
>     if destino is None:
>         destino = []
>     destino.append(x)
>     return destino
>
> # (c) altera o argumento; crie nova lista
> def dobrar(lista):
>     return [x * 2 for x in lista]
>
> # (d) parâmetro sem padrão depois de com padrão
> def f(b, a=1):
>     return a + b
>
> # (e) o arquivo random.py sombreia a biblioteca padrão: renomeie-o
> #     (e apague a pasta __pycache__)
> ```

> [!question] 17. Mini-projeto: Biblioteca de utilidades
> Monte um package `minhalib/` com 3 módulos (`matematica.py`, `texto.py`, `colecoes.py`), cada um com **pelo menos 3 funções documentadas** (estilo Google), um `__init__.py` que exponha as funções principais, doctests e um `requirements.txt` vazio (ou com `pytest`). Crie um ambiente virtual e rode `python -m doctest -v` em cada módulo.

> [!success]- Solução (esqueleto)
> ```text
> minhalib/
> ├── .venv/                  # não versionar
> ├── minhalib/
> │   ├── __init__.py
> │   ├── matematica.py
> │   ├── texto.py
> │   └── colecoes.py
> ├── main.py
> └── requirements.txt
> ```
> ```python
> # minhalib/matematica.py
> """Funções matemáticas auxiliares."""
>
> def media(*numeros):
>     """Calcula a média aritmética.
>
>     Args:
>         *numeros: Valores numéricos.
>
>     Returns:
>         A média, ou 0.0 se nenhum número for informado.
>
>     >>> media(2, 4, 6)
>     4.0
>     >>> media()
>     0.0
>     """
>     return sum(numeros) / len(numeros) if numeros else 0.0
>
> def eh_primo(n):
>     """Indica se n é primo.
>
>     >>> eh_primo(7)
>     True
>     >>> eh_primo(8)
>     False
>     """
>     return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
>
> def mdc(a, b):
>     """Calcula o máximo divisor comum (algoritmo de Euclides).
>
>     >>> mdc(12, 18)
>     6
>     """
>     while b:
>         a, b = b, a % b
>     return a
> ```
> ```python
> # minhalib/__init__.py
> from .matematica import media, eh_primo, mdc
> from .texto import contar_palavras, eh_palindromo, titulo
> from .colecoes import unicos_ordenados, achatar, agrupar_por
>
> __all__ = ["media", "eh_primo", "mdc", "contar_palavras", "eh_palindromo",
>            "titulo", "unicos_ordenados", "achatar", "agrupar_por"]
> ```
> Rode: `python -m doctest -v minhalib/matematica.py`. Repita para os outros módulos. Completar `texto.py` e `colecoes.py` é o exercício.

---

## 🧪 Quiz relâmpago

> [!question] Responda sem rodar o código
> 1. O que `print(f())` mostra? `def f(): pass`
> 2. `def g(a, *args, **kw): ...` chamada `g(1, 2, 3, x=4)`. O que são `a`, `args` e `kw`?
> 3. `def h(x, /, y, *, z): ...` Quais chamadas são válidas? (i) `h(1, 2, z=3)` (ii) `h(1, y=2, z=3)` (iii) `h(x=1, y=2, z=3)` (iv) `h(1, 2, 3)`
> 4. O que imprime?
>    ```python
>    x = 5
>    def f():
>        print(x)
>        x = 10
>    f()
>    ```
> 5. Qual regra descreve a ordem de busca de nomes? Cite as 4 letras.
> 6. Por que `from modulo import *` é desencorajado?
> 7. O que faz `if __name__ == "__main__":`?
> 8. Qual comando instala o pacote `requests` com segurança no ambiente atual?

> [!success]- Respostas
> 1. `None`.
> 2. `a = 1`, `args = (2, 3)`, `kw = {'x': 4}`.
> 3. (i) ✅ (ii) ✅ (iii) ❌ (`x` é só posicional) (iv) ❌ (`z` é só nomeado).
> 4. `UnboundLocalError`: a atribuição `x = 10` torna `x` local em toda a função.
> 5. **LEGB**: Local, Enclosing, Global, Built-in.
> 6. Polui o namespace, esconde a origem dos nomes e pode sobrescrever outros.
> 7. Executa o bloco apenas quando o arquivo roda como script, e não quando é importado.
> 8. `python -m pip install requests` (com o ambiente virtual ativo).

---

## ✅ Checklist do módulo

- [ ] Defino funções que **retornam** valores (e não só imprimem)
- [ ] Uso argumentos posicionais, nomeados, padrão, `*args` e `**kwargs`
- [ ] Evito **padrões mutáveis** (`None` como sentinela)
- [ ] Entendo **LEGB**, `global`, `nonlocal` e quando evitá-los
- [ ] Sei criar e usar **closures**
- [ ] Organizo código em **módulos** e **packages** e uso `__name__ == "__main__"`
- [ ] Crio e ativo **ambientes virtuais** e uso `pip` / `requirements.txt`
- [ ] Documento com **docstrings** (e conheço doctests)
- [ ] Resolvi pelo menos 12 dos exercícios acima

---

## 🚀 Próximo módulo
➡️ [[04 - Programação Orientada a Objetos/01 - Classes e Objetos|Módulo 04: Programação Orientada a Objetos]]

⬅️ [[03 - Funções e Modularização/06 - Docstrings|Docstrings]] · ⬆️ [[Índice - Python|Índice]]

#python #basico #exercicios #pratica #funcoes #modulos #closures
