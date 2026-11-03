---
titulo: "Operadores"
tags: [python, basico, sintaxe]
nivel: iniciante
criado: 2026-10-05
modulo: "01 - Fundamentos"
---

# ➕ Operadores

**Operadores** são símbolos que realizam operações sobre valores (**operandos**). Em `5 + 3`, o `+` é o operador e `5` e `3` são os operandos.

---

## 1. Operadores aritméticos

| Operador | Operação | Exemplo | Resultado |
|----------|----------|---------|-----------|
| `+` | Soma | `7 + 2` | `9` |
| `-` | Subtração | `7 - 2` | `5` |
| `*` | Multiplicação | `7 * 2` | `14` |
| `/` | Divisão (sempre `float`) | `7 / 2` | `3.5` |
| `//` | Divisão inteira (piso) | `7 // 2` | `3` |
| `%` | Resto (módulo) | `7 % 2` | `1` |
| `**` | Potência | `7 ** 2` | `49` |

```python
print(10 / 2)     # 5.0  (note: float!)
print(10 // 3)    # 3
print(10 % 3)     # 1
print(2 ** 10)    # 1024
print(-7 // 2)    # -4   (arredonda para BAIXO, não para zero)
print(-7 % 2)     # 1
```

> [!warning] Armadilha: `/` sempre devolve `float`
> ```python
> # ❌ Esperar int
> metade = 10 / 2      # 5.0, não 5
>
> # ✅ Se quer inteiro
> metade = 10 // 2     # 5
> ```

> [!tip] Usos clássicos do `%`
> - Par ou ímpar: `n % 2 == 0`
> - Ciclar valores: `indice % tamanho`
> - Extrair dígito: `1234 % 10` → `4`

> [!warning] Divisão por zero
> `5 / 0` → `ZeroDivisionError`. Veja [[05 - Tratamento de Erros e Arquivos/01 - try except else finally|tratamento de erros]].

---

## 2. Operadores de atribuição

| Operador | Equivale a |
|----------|-----------|
| `x = 5` | atribui |
| `x += 3` | `x = x + 3` |
| `x -= 3` | `x = x - 3` |
| `x *= 3` | `x = x * 3` |
| `x /= 3` | `x = x / 3` |
| `x //= 3` | `x = x // 3` |
| `x %= 3` | `x = x % 3` |
| `x **= 3` | `x = x ** 3` |

> [!note] Não existe `x++` em Python
> ```python
> x = 0
> # ❌ x++   -> SyntaxError
> # ✅
> x += 1
> ```

### Operador morsa (`:=`)
Atribui **e** devolve o valor na mesma expressão (Python 3.8+):
```python
if (n := len("Python")) > 5:
    print(f"Tamanho {n} é grande")
```

---

## 3. Operadores de comparação

Sempre resultam em `bool`.

| Operador | Significado | Exemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual | `3 == 3` | `True` |
| `!=` | Diferente | `3 != 4` | `True` |
| `>` | Maior | `5 > 3` | `True` |
| `<` | Menor | `5 < 3` | `False` |
| `>=` | Maior ou igual | `5 >= 5` | `True` |
| `<=` | Menor ou igual | `4 <= 3` | `False` |

```python
print("a" < "b")           # True (ordem alfabética/Unicode)
print("Zebra" < "abelha")   # True (maiúsculas vêm antes!)
print(1 == 1.0)             # True
print("1" == 1)             # False (tipos diferentes)
```

### Comparações encadeadas (um recurso lindo do Python)
```python
idade = 25
print(18 <= idade < 65)     # True  (equivale a 18 <= idade and idade < 65)
```

> [!warning] Armadilha clássica: `=` vs `==`
> ```python
> # ❌ SyntaxError
> if x = 5:
>
> # ✅
> if x == 5:
> ```

---

## 4. Operadores lógicos

| Operador | Significado | Exemplo |
|----------|-------------|---------|
| `and` | E (ambos verdadeiros) | `True and False` → `False` |
| `or` | OU (ao menos um) | `True or False` → `True` |
| `not` | Negação | `not True` → `False` |

### Tabela-verdade

| A | B | `A and B` | `A or B` |
|---|---|-----------|----------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

```python
idade = 20
tem_ingresso = True
print(idade >= 18 and tem_ingresso)    # True
print(not tem_ingresso)                # False
```

### Curto-circuito (*short-circuit*)
Python **para de avaliar** assim que o resultado é conhecido.

```python
def teste():
    print("executou!")
    return True

print(False and teste())   # False  (teste() NÃO é chamada)
print(True or teste())     # True   (teste() NÃO é chamada)
```

Útil para evitar erros:
```python
lista = []
if lista and lista[0] > 10:    # não dá IndexError
    print("ok")
```

### `and`/`or` devolvem **valores**, não só `True`/`False`
```python
print("" or "padrão")       # 'padrão'   (primeiro valor verdadeiro)
print("Ada" or "padrão")    # 'Ada'
print(0 and 5)              # 0          (primeiro valor falso)
print(3 and 5)              # 5          (último, se todos verdadeiros)

nome = input_do_usuario = ""
print(nome or "Anônimo")    # 'Anônimo'
```

---

## 5. Operadores de identidade

| Operador | Verifica |
|----------|----------|
| `is` | Se são **o mesmo objeto** |
| `is not` | Se são objetos **diferentes** |

```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b)   # True  (mesmo conteúdo)
print(a is b)   # False (objetos distintos)
print(a is c)   # True  (mesmo objeto)
```

> [!warning] `is` não é "igual"
> ```python
> # ❌ Errado: comparar valores com is
> if nome is "Ada": ...        # SyntaxWarning e resultado imprevisível
>
> # ✅ Correto
> if nome == "Ada": ...
> if valor is None: ...        # is é para None, True, False
> ```
> Regra de bolso: **`==` compara valores; `is` compara identidade.**

---

## 6. Operadores de pertencimento

| Operador | Verifica |
|----------|----------|
| `in` | Se um item **está** na sequência |
| `not in` | Se **não está** |

```python
print("th" in "Python")          # True
print(3 in [1, 2, 3])            # True
print("chave" in {"chave": 1})   # True (procura nas chaves)
print(10 not in [1, 2, 3])       # True
```

---

## 7. Operadores bit a bit (introdução)

Operam sobre os bits dos inteiros. Úteis em baixo nível, flags e otimizações.

| Operador | Nome | Exemplo | Resultado |
|----------|------|---------|-----------|
| `&` | AND | `5 & 3` (`101 & 011`) | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Desloca à esquerda | `1 << 3` | `8` |
| `>>` | Desloca à direita | `16 >> 2` | `4` |

> [!note] Dica
> `bin(5)` → `'0b101'` mostra a representação binária.

---

## 8. Precedência de operadores

Do **maior** para o **menor** (resumo):

| Prioridade | Operadores |
|------------|-----------|
| 1 | `()` parênteses |
| 2 | `**` |
| 3 | `+x`, `-x`, `~x` (unários) |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` → `^` → `\|` |
| 8 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` |
| 9 | `not` |
| 10 | `and` |
| 11 | `or` |

```python
print(2 + 3 * 4)       # 14  (e não 20)
print((2 + 3) * 4)     # 20
print(-2 ** 2)         # -4  (** vem antes do sinal)
print(not True or True)  # True  ((not True) or True)
```

> [!tip] Na dúvida, use parênteses
> Código legível vale mais que decorar a tabela. `(a and b) or c` deixa claro o que você quis dizer.

---

## 9. Operadores com strings e listas (prévia)

```python
print("ha" * 3)            # 'hahaha'
print("Olá, " + "mundo")   # concatenação
print([1, 2] + [3])        # [1, 2, 3]
print([0] * 5)             # [0, 0, 0, 0, 0]
```
Veja mais em [[02 - Controle de Fluxo e Estruturas de Dados/03 - Listas|Listas]].

---

> [!question] Exercícios
> 1. Calcule `17 // 5`, `17 % 5` e `17 / 5` sem rodar o código. Depois confira.
> 2. Escreva uma expressão que seja `True` se `n` for par **e** positivo.
> 3. Qual o resultado de `2 + 3 * 4 ** 2 / 8`?
> 4. O que imprime `print("" or "vazio")`? E `print("oi" and 0)`?
> 5. Qual a diferença entre `a == b` e `a is b`? Dê um exemplo em que dão resultados diferentes.
> 6. Verifique se `x` está entre 10 e 20 (inclusive) usando comparação encadeada.

> [!success]- Soluções
> 1. `3`, `2`, `3.4`
> 2. `n % 2 == 0 and n > 0`
> 3. `4 ** 2 = 16` → `3 * 16 = 48` → `48 / 8 = 6.0` → `2 + 6.0 = 8.0`
> 4. `vazio` e `0`
> 5. `==` compara valores; `is` compara se é o mesmo objeto. `a = [1]; b = [1]` → `a == b` é `True`, `a is b` é `False`.
> 6. `10 <= x <= 20`

---

⬅️ [[01 - Fundamentos/03 - Tipos de Dados Primitivos|Tipos de Dados Primitivos]] | ➡️ [[01 - Fundamentos/05 - Entrada e Saída|Entrada e Saída]]

#python #basico #operadores #aritmetica #logica #comparacao
