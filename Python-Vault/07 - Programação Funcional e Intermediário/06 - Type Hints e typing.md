---
titulo: "Type Hints e o módulo typing"
tags: [python, intermediario, tipos]
nivel: intermediario
criado: 2026-10-09
modulo: "07 - Programação Funcional e Intermediário"
---

# 🏷️ Type Hints e o módulo `typing`

> [!note] Ideia central
> Python é **dinamicamente tipado**: o interpretador **não** verifica tipos anotados. Type hints são *documentação verificável*: servem a editores (autocomplete), a ferramentas como **mypy** e **pyright**, e a bibliotecas (dataclasses, Pydantic, FastAPI).

## 1. Sintaxe básica

```python
nome: str = "Ana"
idade: int = 30
preco: float = 9.9
ativo: bool = True

def saudar(nome: str, vezes: int = 1) -> str:
    return (f"Olá, {nome}! " * vezes).strip()

def log(msg: str) -> None:        # não retorna nada
    print(msg)
```

> [!warning] Anotação não impõe nada em tempo de execução
> ```python
> def dobro(x: int) -> int:
>     return x * 2
>
> print(dobro("ab"))    # 'abab' — roda! mypy reclamaria, o Python não
> ```

## 2. Coleções (sintaxe moderna, 3.9+)

Não precisa mais de `List`, `Dict` de `typing`:

```python
numeros: list[int] = [1, 2, 3]
pessoa: dict[str, int] = {"ana": 30}
unicos: set[str] = {"a", "b"}
ponto: tuple[float, float] = (1.0, 2.0)
variavel: tuple[int, ...] = (1, 2, 3, 4)     # tupla de tamanho livre
```

| ❌ Antigo | ✅ Moderno |
|---|---|
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Optional[int]` | `int \| None` |
| `Union[int, str]` | `int \| str` |

## 3. União, `None` e `Optional`

```python
def achar(id: int) -> str | None:
    return {1: "Ana"}.get(id)

nome = achar(2)
print(nome.upper())          # ❌ mypy: "None" não tem upper()

if nome is not None:         # ✅ narrowing
    print(nome.upper())
```

> [!tip] Narrowing
> Checagens como `is None`, `isinstance(x, str)` e `match` estreitam o tipo dentro do bloco.

## 4. `Any`, `object` e `Never`

| Tipo | Significado |
|---|---|
| `Any` | desliga a checagem (escape hatch) |
| `object` | qualquer valor, mas só use o que `object` oferece |
| `Never` / `NoReturn` | função que nunca retorna (ex: sempre levanta exceção) |

## 5. Tipos de funções: `Callable`

```python
from collections.abc import Callable

def aplicar(f: Callable[[int, int], int], a: int, b: int) -> int:
    return f(a, b)

aplicar(lambda x, y: x + y, 2, 3)
```

Veja [[07 - Programação Funcional e Intermediário/01 - Funções de Ordem Superior|Funções de Ordem Superior]].

## 6. Abstrações: `Sequence`, `Iterable`, `Mapping`

Prefira tipos **abstratos** em parâmetros e **concretos** em retornos:

```python
from collections.abc import Iterable, Sequence, Mapping

def total(xs: Iterable[float]) -> float:        # aceita list, tuple, generator...
    return sum(xs)

def primeiro(xs: Sequence[str]) -> str:         # precisa de indexação
    return xs[0]

def contar(m: Mapping[str, int]) -> int:        # somente leitura
    return sum(m.values())
```

> [!tip] Lei de Postel dos tipos
> *Seja liberal no que aceita, específico no que retorna.* Veja [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|Iterators]]: `Iterator[T]` e `Generator[Y, S, R]`.

## 7. Generics com a sintaxe do Python 3.12 (PEP 695)

```python
# 3.12+
def primeiro[T](xs: list[T]) -> T:
    return xs[0]

class Caixa[T]:
    def __init__(self, item: T) -> None:
        self.item = item

    def pegar(self) -> T:
        return self.item

c = Caixa(42)            # Caixa[int]
c2 = Caixa("oi")         # Caixa[str]
```

Antes do 3.12:

```python
from typing import TypeVar, Generic
T = TypeVar("T")

class Caixa(Generic[T]): ...
```

### Limites (bounds) e constraints

```python
def maior[T: (int, float)](a: T, b: T) -> T:     # só int ou float
    return a if a > b else b

class Animal: ...
def adotar[A: Animal](a: A) -> A:                 # A precisa ser subclasse de Animal
    return a
```

### Alias com `type`

```python
type ID = int | str
type Matriz[T] = list[list[T]]
type JSON = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
```

## 8. `TypedDict`

Para dicionários com **chaves conhecidas** (ex: JSON):

```python
from typing import TypedDict, NotRequired

class Usuario(TypedDict):
    nome: str
    idade: int
    email: NotRequired[str]

u: Usuario = {"nome": "Ana", "idade": 30}
```

## 9. `Literal`, `Final`, `ClassVar`

```python
from typing import Literal, Final, ClassVar

Modo = Literal["r", "w", "a"]

def abrir(caminho: str, modo: Modo) -> None: ...
abrir("x", "z")           # ❌ mypy: valor inválido

MAX: Final = 100          # constante: não reatribuir

class Contador:
    total: ClassVar[int] = 0   # atributo de classe
```

## 10. `Protocol`: *duck typing* tipado

```python
from typing import Protocol

class Fechavel(Protocol):
    def close(self) -> None: ...

def encerrar(x: Fechavel) -> None:
    x.close()

class Conexao:
    def close(self) -> None:
        print("fechou")

encerrar(Conexao())       # ✅ sem herdar de nada!
```

> [!tip] "Se anda como pato..."
> `Protocol` é *subtipagem estrutural*: basta ter os métodos certos. Compare com [[04 - Programação Orientada a Objetos/03 - Herança Polimorfismo e Encapsulamento|herança]] (subtipagem nominal) e `abc.ABC`.

| | Herança/ABC | Protocol |
|---|---|---|
| Precisa declarar herança | ✅ | ❌ |
| Verificação em runtime | `isinstance` | só com `@runtime_checkable` |
| Bom para | hierarquias controladas | integrar código de terceiros |

## 11. `Self`, `override`, `overload`

```python
from typing import Self, overload, override

class Builder:
    def __init__(self) -> None:
        self.partes: list[str] = []

    def add(self, p: str) -> Self:        # encadeamento correto em subclasses
        self.partes.append(p)
        return self

class Base:
    def falar(self) -> str: return "..."

class Cao(Base):
    @override                              # erro se Base.falar não existir
    def falar(self) -> str: return "au"

@overload
def dobrar(x: int) -> int: ...
@overload
def dobrar(x: str) -> str: ...
def dobrar(x):
    return x * 2
```

## 12. `ParamSpec` e decorators

```python
from collections.abc import Callable
import functools

def log[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"chamando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

Mais em [[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]].

## 13. Dataclasses e hints

```python
from dataclasses import dataclass, field

@dataclass(slots=True)
class Pedido:
    id: int
    itens: list[str] = field(default_factory=list)
```

Veja [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots|Dataclasses e Slots]].

## 14. Verificando com mypy / pyright

```bash
pip install mypy
mypy meu_script.py
mypy --strict pacote/
```

```python
# exemplo.py
def soma(a: int, b: int) -> int:
    return a + b

soma("1", 2)
```

```text
exemplo.py:4: error: Argument 1 to "soma" has incompatible type "str"; expected "int"
```

> [!tip] Adoção gradual
> Comece anotando funções públicas. Configure em `pyproject.toml`:
> ```toml
> [tool.mypy]
> python_version = "3.12"
> strict = true
> ```
> Veja [[08 - Avançado/07 - Packaging e Distribuição|Packaging]].

## 15. Inspecionando hints em runtime

```python
from typing import get_type_hints

def f(x: int, y: str = "a") -> bool: ...
print(get_type_hints(f))
# {'x': <class 'int'>, 'y': <class 'str'>, 'return': <class 'bool'>}
print(f.__annotations__)
```

## 16. Pegadinhas

> [!warning] 1. Mutável como padrão (continua valendo!)
> ```python
> def add(x: int, lista: list[int] = []) -> list[int]:   # ❌
>     ...
> def add(x: int, lista: list[int] | None = None) -> list[int]:  # ✅
>     lista = [] if lista is None else lista
> ```

> [!warning] 2. `list[int]` ≠ `list[int | str]` (invariância)
> Uma `list[int]` **não** é aceita onde se espera `list[int | str]`, pois a função poderia inserir `str`. Use `Sequence[int | str]` (covariante, só leitura).

> [!warning] 3. `Optional[int]` **não** significa parâmetro opcional
> Significa `int | None`. Para ser opcional precisa de valor padrão.

> [!warning] 4. Referência a classe ainda não definida
> ```python
> class No:
>     def proximo(self) -> "No": ...      # string (forward reference)
>     def outro(self) -> Self: ...        # ou Self
> ```

> [!warning] 5. Excesso de `Any`
> Cada `Any` é um buraco na rede de segurança. Prefira `object`, `Protocol` ou generics.

## 17. Exercícios

> [!question] Exercício 1
> Anote: `def media(valores): return sum(valores) / len(valores)` — aceitando qualquer sequência numérica.

> [!success]- Solução
> ```python
> from collections.abc import Sequence
>
> def media(valores: Sequence[float]) -> float:
>     return sum(valores) / len(valores)
> ```

> [!question] Exercício 2
> Escreva uma função genérica `ultimo[T](xs: Sequence[T]) -> T | None`.

> [!success]- Solução
> ```python
> from collections.abc import Sequence
>
> def ultimo[T](xs: Sequence[T]) -> T | None:
>     return xs[-1] if xs else None
> ```

> [!question] Exercício 3
> Defina um `Protocol` `Desenhavel` com `desenhar() -> str` e uma função que aceita uma lista deles.

> [!success]- Solução
> ```python
> from typing import Protocol
> from collections.abc import Iterable
>
> class Desenhavel(Protocol):
>     def desenhar(self) -> str: ...
>
> class Circulo:
>     def desenhar(self) -> str: return "○"
>
> def renderizar(itens: Iterable[Desenhavel]) -> str:
>     return "".join(i.desenhar() for i in itens)
>
> print(renderizar([Circulo(), Circulo()]))   # ○○
> ```

> [!question] Exercício 4
> Modele com `TypedDict` uma resposta de API `{"status": "ok"|"erro", "dados": list[int]}`.

> [!success]- Solução
> ```python
> from typing import TypedDict, Literal
>
> class Resposta(TypedDict):
>     status: Literal["ok", "erro"]
>     dados: list[int]
> ```

---

⬅️ [[07 - Programação Funcional e Intermediário/05 - Context Managers Avançados|Context Managers Avançados]] | ➡️ [[07 - Programação Funcional e Intermediário/07 - Exercícios de Programação Funcional e Intermediário|Exercícios do Módulo 07]]

#python #intermediario #type-hints #typing #mypy #generics #protocol
