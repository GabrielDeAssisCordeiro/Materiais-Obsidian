---
titulo: "Propriedades e Métodos Mágicos (dunder)"
tags: [python, intermediario, poo]
nivel: intermediario
criado: 2026-10-05
modulo: "04 - Programação Orientada a Objetos"
---

# ✨ Propriedades e Métodos Mágicos (dunder)

Duas ferramentas que fazem suas classes parecerem **nativas** do Python:
- **Propriedades** (`@property`): atributos com **lógica** por trás
- **Métodos mágicos** (*dunder methods*, de *double underscore*): permitem usar `+`, `len()`, `==`, `for`, `with`... com seus objetos

---

## Parte 1: Propriedades

## 1. O problema

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Ada", 36)
p.idade = -50       # ❌ nada impede um valor absurdo
```

Em Java você criaria `getIdade()`/`setIdade()` desde o início. Em Python, começa-se com **atributo simples** e, **se precisar** de regras, troca-se por **`@property`** sem mudar o código de quem usa (`p.idade` continua igual).

## 2. `@property`: getter, setter e deleter

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade          # passa pelo setter!

    @property
    def idade(self):                # getter
        return self._idade

    @idade.setter
    def idade(self, valor):         # setter (validação)
        if not isinstance(valor, int):
            raise TypeError("Idade deve ser inteiro")
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor

    @idade.deleter
    def idade(self):                # deleter (raro)
        del self._idade


p = Pessoa("Ada", 36)
print(p.idade)        # 36         → chama o getter
p.idade = 37          # ✅         → chama o setter
p.idade = -1          # ❌ ValueError: Idade não pode ser negativa
```

> [!note] O dado "real" fica em `_idade`
> A propriedade `idade` é a **interface pública**; o valor armazenado vive em `self._idade` (convenção de protegido, veja [[04 - Programação Orientada a Objetos/03 - Herança Polimorfismo e Encapsulamento#4. Encapsulamento|Encapsulamento]]).

> [!warning] Armadilha: recursão infinita
> ```python
> @idade.setter
> def idade(self, valor):
>     self.idade = valor        # ❌ chama o próprio setter para sempre
>     # RecursionError: maximum recursion depth exceeded
>
>     self._idade = valor       # ✅ guarde em outro nome
> ```

> [!warning] Armadilha: o setter precisa ter **o mesmo nome**
> ```python
> @property
> def idade(self): ...
>
> @idade.setter
> def definir_idade(self, v): ...   # ❌ cria OUTRA propriedade (e perde a setter)
> ```

## 3. Propriedades **calculadas** (somente leitura)

Sem setter, a propriedade é **somente leitura**:

```python
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):                   # calculada a cada acesso
        return self.base * self.altura

    @property
    def eh_quadrado(self):
        return self.base == self.altura


r = Retangulo(3, 4)
print(r.area)            # 12  (sem parênteses!)
r.base = 10
print(r.area)            # 40  (sempre atualizada)
r.area = 99              # ❌ AttributeError: property 'area' of 'Retangulo' object has no setter
```

| Ideia | Resultado |
|-------|-----------|
| Atributo derivado de outros | Nunca fica **desatualizado** |
| Parece atributo, é método | API limpa: `r.area` e não `r.get_area()` |

> [!tip] Quando **não** usar property
> Se o cálculo é **caro** (rede, disco, laço enorme), use um método explícito (`calcular_area()`) para o leitor perceber o custo, ou *cache* com `functools.cached_property`.

### `cached_property`: calcula uma vez
```python
from functools import cached_property

class Relatorio:
    def __init__(self, dados):
        self.dados = dados

    @cached_property
    def total(self):
        print("calculando...")
        return sum(self.dados)

r = Relatorio([1, 2, 3])
print(r.total)    # calculando... 6
print(r.total)    # 6  (cache)
```

## 4. Exemplo: conversão de unidades com property

```python
class Temperatura:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Abaixo do zero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5 / 9     # reaproveita a validação


t = Temperatura(100)
print(t.fahrenheit)     # 212.0
t.fahrenheit = 32
print(t.celsius)        # 0.0
```

---

## Parte 2: Métodos Mágicos (dunder)

São métodos com nomes como `__init__`, `__str__`, `__add__`. **Você não os chama diretamente**: o Python os chama quando você usa certas sintaxes.

| Você escreve | Python chama |
|--------------|--------------|
| `Classe(...)` | `__init__` |
| `print(obj)` / `str(obj)` | `__str__` |
| `repr(obj)` | `__repr__` |
| `a + b` | `a.__add__(b)` |
| `a == b` | `a.__eq__(b)` |
| `a < b` | `a.__lt__(b)` |
| `len(obj)` | `__len__` |
| `obj[i]` | `__getitem__` |
| `for x in obj` | `__iter__` |
| `x in obj` | `__contains__` |
| `obj()` | `__call__` |
| `with obj:` | `__enter__` / `__exit__` |
| `bool(obj)` | `__bool__` |

> [!note] O "protocolo de dados" do Python
> Implementar dunders é como seu objeto **participa da linguagem**. Foi assim que `list`, `dict` e `str` foram construídos.

## 5. Representação: `__repr__` e `__str__`

```python
class Ponto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Ponto({self.x!r}, {self.y!r})"     # inequívoco, "recriável"

    def __str__(self):
        return f"({self.x}, {self.y})"              # amigável


p = Ponto(1, 2)
print(p)         # (1, 2)
print(repr(p))   # Ponto(1, 2)
print(f"{p!r}")  # Ponto(1, 2)
```

## 6. Igualdade, hash e ordenação

```python
class Ponto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, outro):
        if not isinstance(outro, Ponto):
            return NotImplemented          # deixa o Python tentar o outro lado
        return (self.x, self.y) == (outro.x, outro.y)

    def __hash__(self):
        return hash((self.x, self.y))      # necessário para usar em set/dict


print(Ponto(1, 2) == Ponto(1, 2))          # True
print(len({Ponto(1, 2), Ponto(1, 2)}))     # 1
```

> [!warning] Defina `__hash__` junto com `__eq__`
> Se você definir `__eq__` **sem** `__hash__`, o Python define `__hash__ = None` e o objeto **deixa de ser hasheável** (não entra em sets nem serve de chave de dict). Regra: **objetos iguais devem ter o mesmo hash**, e só deve haver hash para objetos **imutáveis**.

> [!warning] Retorne `NotImplemented`, não `False`
> Em comparações/operadores com tipos incompatíveis, `return NotImplemented` (a constante, **não** a exceção `NotImplementedError`) permite que o Python tente a operação reversa e, por fim, levante `TypeError` corretamente.

### Ordenação
```python
from functools import total_ordering

@total_ordering                      # gera <=, >, >= a partir de __eq__ e __lt__
class Versao:
    def __init__(self, maior, menor):
        self.maior, self.menor = maior, menor

    def __eq__(self, o):
        return (self.maior, self.menor) == (o.maior, o.menor)

    def __lt__(self, o):
        return (self.maior, self.menor) < (o.maior, o.menor)

    def __repr__(self):
        return f"v{self.maior}.{self.menor}"

print(sorted([Versao(2, 1), Versao(1, 9), Versao(2, 0)]))
# [v1.9, v2.0, v2.1]
print(max(Versao(1, 0), Versao(3, 2)))     # v3.2
```
(Para classes de dados, [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots|dataclasses]] geram tudo isso com `order=True`.)

## 7. Operadores aritméticos

```python
class Vetor:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, o):                    # v1 + v2
        if not isinstance(o, Vetor):
            return NotImplemented
        return Vetor(self.x + o.x, self.y + o.y)

    def __sub__(self, o):                    # v1 - v2
        return Vetor(self.x - o.x, self.y - o.y)

    def __mul__(self, k):                    # v * 3
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Vetor(self.x * k, self.y * k)

    def __rmul__(self, k):                   # 3 * v  (operando invertido)
        return self * k

    def __neg__(self):                       # -v
        return Vetor(-self.x, -self.y)

    def __abs__(self):                       # abs(v)
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self):                      # if v:
        return bool(self.x or self.y)

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"


a, b = Vetor(1, 2), Vetor(3, 4)
print(a + b)       # Vetor(4, 6)
print(b - a)       # Vetor(2, 2)
print(a * 3)       # Vetor(3, 6)
print(3 * a)       # Vetor(3, 6)   ← __rmul__
print(-a)          # Vetor(-1, -2)
print(abs(b))      # 5.0
```

| Operador | Método | Reverso | In-place |
|----------|--------|---------|----------|
| `+` | `__add__` | `__radd__` | `__iadd__` (`+=`) |
| `-` | `__sub__` | `__rsub__` | `__isub__` |
| `*` | `__mul__` | `__rmul__` | `__imul__` |
| `/` | `__truediv__` | `__rtruediv__` | |
| `//` | `__floordiv__` | | |
| `%` | `__mod__` | | |
| `**` | `__pow__` | | |
| `@` | `__matmul__` | | |

> [!tip] Moderação
> Sobrecarregue operadores só quando o significado for **óbvio** (vetores, dinheiro, matrizes). `carro + pessoa` é um mau design.

## 8. Comportamento de coleção

```python
class Playlist:
    def __init__(self, *musicas):
        self._musicas = list(musicas)

    def __len__(self):                   # len(p)
        return len(self._musicas)

    def __getitem__(self, i):            # p[0], p[1:3], e permite 'for' por padrão
        return self._musicas[i]

    def __setitem__(self, i, v):         # p[0] = "..."
        self._musicas[i] = v

    def __delitem__(self, i):            # del p[0]
        del self._musicas[i]

    def __contains__(self, m):           # "x" in p
        return m in self._musicas

    def __iter__(self):                  # for m in p
        return iter(self._musicas)

    def __repr__(self):
        return f"Playlist({', '.join(map(repr, self._musicas))})"


p = Playlist("Imagine", "Yesterday", "Hey Jude")
print(len(p))              # 3
print(p[0])                # Imagine
print(p[1:])               # ['Yesterday', 'Hey Jude']
print("Yesterday" in p)     # True
for m in p:
    print(m)
print(sorted(p), list(reversed(p)))
```

> [!note] Implementando só `__len__` e `__getitem__`, você já ganha iteração, `in`, `reversed`... Veja mais em [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|Generators e Iterators]].

## 9. Objetos "chamáveis": `__call__`

```python
class Multiplicador:
    def __init__(self, fator):
        self.fator = fator

    def __call__(self, x):
        return x * self.fator

dobro = Multiplicador(2)
print(dobro(21))                # 42
print(list(map(dobro, [1, 2, 3])))   # [2, 4, 6]
```
Um objeto com `__call__` se comporta como **função com estado** (alternativa a [[03 - Funções e Modularização/03 - Escopo e Closures|closures]]; base de decorators com classe).

## 10. Gerenciadores de contexto: `__enter__` e `__exit__`

```python
class Cronometro:
    def __enter__(self):
        import time
        self.inicio = time.perf_counter()
        return self

    def __exit__(self, tipo_exc, exc, tb):
        import time
        print(f"Levou {time.perf_counter() - self.inicio:.3f}s")
        return False        # False = não suprime exceções

with Cronometro():
    sum(range(1_000_000))
```
Aprofunde em [[05 - Tratamento de Erros e Arquivos/04 - Context Managers com with|Context Managers]].

## 11. Ciclo de vida e acesso a atributos (para conhecer)

| Método | Quando é chamado |
|--------|------------------|
| `__new__(cls, ...)` | **Cria** a instância (antes do `__init__`) |
| `__init__(self, ...)` | **Inicializa** a instância |
| `__del__(self)` | Antes de o objeto ser destruído (evite depender dele) |
| `__getattr__(self, nome)` | Só quando o atributo **não é encontrado** |
| `__getattribute__(self, nome)` | **Todo** acesso a atributo |
| `__setattr__(self, nome, v)` | Toda atribuição de atributo |
| `__format__(self, spec)` | `f"{obj:spec}"` |
| `__slots__` | Restringe atributos (veja [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots\|Slots]]) |

```python
class Config:
    def __init__(self, **dados):
        self._dados = dados

    def __getattr__(self, nome):
        try:
            return self._dados[nome]
        except KeyError:
            raise AttributeError(nome) from None

c = Config(host="localhost", porta=5432)
print(c.host, c.porta)      # localhost 5432
```

> [!warning] Cuidado com `__getattr__`/`__setattr__`
> Fáceis de gerar **recursão infinita** (acessar `self.x` dentro de `__getattribute__`). Em `__setattr__`, use `super().__setattr__(nome, valor)`.

Metaprogramação avançada (descriptors, metaclasses) em [[08 - Avançado/01 - Metaprogramação|Metaprogramação]].

---

## 12. Exemplo completo: classe `Dinheiro`

```python
from functools import total_ordering

@total_ordering
class Dinheiro:
    def __init__(self, centavos):
        self._centavos = int(centavos)          # evita erros de float

    @classmethod
    def de_reais(cls, reais):
        return cls(round(reais * 100))

    @property
    def reais(self):
        return self._centavos / 100

    def __add__(self, o):
        if not isinstance(o, Dinheiro):
            return NotImplemented
        return Dinheiro(self._centavos + o._centavos)

    def __sub__(self, o):
        if not isinstance(o, Dinheiro):
            return NotImplemented
        return Dinheiro(self._centavos - o._centavos)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Dinheiro(round(self._centavos * k))

    __rmul__ = __mul__

    def __eq__(self, o):
        return isinstance(o, Dinheiro) and self._centavos == o._centavos

    def __lt__(self, o):
        if not isinstance(o, Dinheiro):
            return NotImplemented
        return self._centavos < o._centavos

    def __hash__(self):
        return hash(self._centavos)

    def __bool__(self):
        return self._centavos != 0

    def __str__(self):
        return f"R$ {self.reais:,.2f}"

    def __repr__(self):
        return f"Dinheiro({self._centavos})"


a = Dinheiro.de_reais(10.10)
b = Dinheiro.de_reais(0.20)
print(a + b)                  # R$ 10.30
print(a * 3)                  # R$ 30.30
print(sum([a, b], Dinheiro(0)))   # R$ 10.30
print(a > b, a == Dinheiro(1010))  # True True
```

---

> [!question] Exercícios
> 1. Crie `Termometro` com propriedade `celsius` que rejeite valores abaixo de `-273.15`, e propriedade somente leitura `kelvin`.
> 2. Crie `Produto` com `preco` validado (>= 0) e `preco_com_imposto` calculado (propriedade somente leitura).
> 3. Implemente `Fracao(num, den)` com `__add__`, `__mul__`, `__eq__`, `__repr__`, `__str__` (`3/4`). Normalize com `math.gcd`.
> 4. Faça uma classe `Fila` com `__len__`, `__iter__`, `__contains__`, `__bool__` e métodos `entrar`/`sair`.
> 5. Por que o código abaixo dá `RecursionError`? Corrija.
>    ```python
>    class A:
>        @property
>        def x(self): return self.x
>    ```
> 6. O que acontece se definir `__eq__` sem `__hash__`? Mostre.
> 7. Crie `Contador` com `__call__` que incrementa e retorna o valor a cada chamada.
> 8. Implemente `Matriz2x2` com `__add__`, `__mul__` (produto matricial) e `__repr__`.

> [!success]- Soluções
> 1. ```python
>    class Termometro:
>        def __init__(self, celsius=0):
>            self.celsius = celsius
>        @property
>        def celsius(self):
>            return self._celsius
>        @celsius.setter
>        def celsius(self, v):
>            if v < -273.15:
>                raise ValueError("Abaixo do zero absoluto")
>            self._celsius = v
>        @property
>        def kelvin(self):
>            return self._celsius + 273.15
>    ```
> 2. ```python
>    class Produto:
>        IMPOSTO = 0.1
>        def __init__(self, nome, preco):
>            self.nome = nome
>            self.preco = preco
>        @property
>        def preco(self): return self._preco
>        @preco.setter
>        def preco(self, v):
>            if v < 0:
>                raise ValueError("Preço negativo")
>            self._preco = v
>        @property
>        def preco_com_imposto(self):
>            return self._preco * (1 + self.IMPOSTO)
>    ```
> 3. ```python
>    from math import gcd
>    class Fracao:
>        def __init__(self, num, den=1):
>            if den == 0:
>                raise ZeroDivisionError("Denominador zero")
>            g = gcd(num, den)
>            self.num, self.den = num // g, den // g
>        def __add__(self, o):
>            return Fracao(self.num * o.den + o.num * self.den, self.den * o.den)
>        def __mul__(self, o):
>            return Fracao(self.num * o.num, self.den * o.den)
>        def __eq__(self, o):
>            return (self.num, self.den) == (o.num, o.den)
>        def __hash__(self): return hash((self.num, self.den))
>        def __str__(self): return f"{self.num}/{self.den}"
>        def __repr__(self): return f"Fracao({self.num}, {self.den})"
>    print(Fracao(1, 2) + Fracao(1, 4))    # 3/4
>    ```
> 4. ```python
>    class Fila:
>        def __init__(self): self._itens = []
>        def entrar(self, x): self._itens.append(x)
>        def sair(self): return self._itens.pop(0)
>        def __len__(self): return len(self._itens)
>        def __iter__(self): return iter(self._itens)
>        def __contains__(self, x): return x in self._itens
>        def __bool__(self): return bool(self._itens)
>    ```
> 5. O getter retorna `self.x`, que chama o próprio getter. Guarde em outro nome: `return self._x`.
> 6. ```python
>    class P:
>        def __init__(self, v): self.v = v
>        def __eq__(self, o): return self.v == o.v
>    {P(1)}    # TypeError: unhashable type: 'P'
>    ```
> 7. ```python
>    class Contador:
>        def __init__(self): self.valor = 0
>        def __call__(self):
>            self.valor += 1
>            return self.valor
>    c = Contador(); c(); print(c())    # 2
>    ```
> 8. ```python
>    class Matriz2x2:
>        def __init__(self, a, b, c, d): self.m = [[a, b], [c, d]]
>        def __add__(self, o):
>            return Matriz2x2(*(self.m[i][j] + o.m[i][j] for i in range(2) for j in range(2)))
>        def __mul__(self, o):
>            return Matriz2x2(*(sum(self.m[i][k] * o.m[k][j] for k in range(2))
>                                for i in range(2) for j in range(2)))
>        def __repr__(self): return f"Matriz2x2({self.m})"
>    ```

---

⬅️ [[04 - Programação Orientada a Objetos/03 - Herança Polimorfismo e Encapsulamento|Herança, Polimorfismo e Encapsulamento]] | ➡️ [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots|Dataclasses e Slots]]

#python #intermediario #poo #property #dunder #metodos-magicos #sobrecarga-de-operadores
