---
titulo: "Documentação com Docstrings"
tags: [python, basico, documentacao]
nivel: iniciante
criado: 2026-10-05
modulo: "03 - Funções e Modularização"
---

# 📝 Documentação com Docstrings

Uma **docstring** é uma string de documentação colocada **logo no início** de um módulo, função, classe ou método. Diferente de um comentário `#`, ela **fica disponível em tempo de execução** e é usada por `help()`, editores e geradores de documentação.

> [!note] Comentário vs docstring
> | | Comentário `#` | Docstring `""" """` |
> |---|---|---|
> | Para quem? | Quem lê o **código** | Quem **usa** a função/classe |
> | Explica | O **porquê** de uma decisão | **O que faz**, parâmetros, retorno, erros |
> | Acessível em runtime | ❌ | ✅ (`__doc__`, `help()`) |

---

## 1. Primeira docstring

```python
def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b

print(somar.__doc__)      # Retorna a soma de a e b.
help(somar)
```

Saída do `help`:
```text
Help on function somar in module __main__:

somar(a, b)
    Retorna a soma de a e b.
```

> [!tip] No editor
> Passe o mouse sobre a função no VS Code (ou `Ctrl+K Ctrl+I`) e a docstring aparece. No REPL, `help(funcao)` ou `funcao?` no IPython.

---

## 2. Regras da PEP 257

| Regra | Exemplo |
|-------|---------|
| Use **aspas triplas duplas** `"""` | `"""Texto."""` |
| Primeira linha: **resumo curto**, no imperativo, terminando em ponto | `"""Calcula a média das notas."""` |
| Se houver mais detalhes: **linha em branco** após o resumo | — |
| Docstrings de uma linha: aspas de abertura e fechamento na **mesma linha** | — |
| Docstrings de várias linhas: aspas de fechamento em **linha própria** | — |

```python
# Uma linha
def eh_par(n):
    """Retorna True se n for par."""
    return n % 2 == 0

# Várias linhas
def media(notas):
    """Calcula a média aritmética das notas.

    Ignora valores None e devolve 0.0 se não houver notas válidas.
    """
    validas = [n for n in notas if n is not None]
    return sum(validas) / len(validas) if validas else 0.0
```

> [!warning] Erros comuns
> ```python
> # ❌ Descreve COMO, repete o código
> def dobro(n):
>     """Multiplica n por 2 e retorna o resultado."""
>
> # ✅ Descreve O QUÊ e o contrato
> def dobro(n):
>     """Retorna o dobro de n."""
>
> # ❌ Docstring depois do código = vira uma string solta, não docstring
> def f():
>     x = 1
>     """Isto NÃO é a docstring"""
> ```

---

## 3. Formatos de docstring detalhada

Para documentar **parâmetros, retorno e exceções**, existem convenções. Escolha **uma** e use em todo o projeto.

### 3.1 Estilo Google (legível e popular)
```python
def dividir(a, b):
    """Divide a por b.

    Args:
        a (float): Dividendo.
        b (float): Divisor. Não pode ser zero.

    Returns:
        float: O resultado da divisão.

    Raises:
        ZeroDivisionError: Se b for zero.

    Example:
        >>> dividir(10, 2)
        5.0
    """
    return a / b
```

### 3.2 Estilo NumPy (comum em ciência de dados)
```python
def dividir(a, b):
    """
    Divide a por b.

    Parameters
    ----------
    a : float
        Dividendo.
    b : float
        Divisor. Não pode ser zero.

    Returns
    -------
    float
        O resultado da divisão.

    Raises
    ------
    ZeroDivisionError
        Se b for zero.
    """
    return a / b
```

### 3.3 Estilo reStructuredText (Sphinx clássico)
```python
def dividir(a, b):
    """Divide a por b.

    :param a: Dividendo.
    :type a: float
    :param b: Divisor.
    :type b: float
    :returns: O resultado da divisão.
    :rtype: float
    :raises ZeroDivisionError: Se b for zero.
    """
    return a / b
```

| Estilo | Quando usar |
|--------|-------------|
| **Google** | Projetos gerais, boa legibilidade no código |
| **NumPy** | Bibliotecas científicas |
| **reST** | Projetos que já usam Sphinx desse jeito |

> [!tip] Com type hints, não repita os tipos
> Se você já usa [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|type hints]], pode omitir os tipos na docstring:
> ```python
> def dividir(a: float, b: float) -> float:
>     """Divide a por b.
>
>     Args:
>         a: Dividendo.
>         b: Divisor. Não pode ser zero.
>
>     Returns:
>         O resultado da divisão.
>     """
>     return a / b
> ```

---

## 4. Docstrings de módulo, classe e método

### Módulo (no topo do arquivo, antes dos imports)
```python
"""Utilitários de geometria.

Contém funções para calcular áreas e perímetros de figuras planas.
"""

import math
```

### Classe e métodos
```python
class ContaBancaria:
    """Representa uma conta bancária simples.

    Attributes:
        titular: Nome do titular da conta.
        saldo: Saldo atual em reais.
    """

    def __init__(self, titular, saldo=0.0):
        """Cria uma conta.

        Args:
            titular: Nome do titular.
            saldo: Saldo inicial (padrão 0.0).
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """Adiciona valor ao saldo.

        Raises:
            ValueError: Se valor não for positivo.
        """
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        self.saldo += valor
```
Aprofunde em [[04 - Programação Orientada a Objetos/01 - Classes e Objetos|Classes e Objetos]].

### Onde ficam guardadas
```python
print(__doc__)                  # docstring do módulo atual
print(ContaBancaria.__doc__)
print(ContaBancaria.depositar.__doc__)
```

---

## 5. O que escrever (e o que não escrever)

### Boa docstring responde:
1. **O que** faz? (resumo)
2. **O que recebe?** (parâmetros, tipos, unidades, restrições)
3. **O que devolve?**
4. **O que pode dar errado?** (exceções)
5. **Como usar?** (exemplo, quando não for óbvio)

> [!tip] Exemplo de unidade
> `Args: altura: Altura em metros.` evita bugs como passar centímetros.

### Não escreva
- ❌ O óbvio: `"""Função que soma."""` em `def soma(a, b)`
- ❌ Detalhes da **implementação** que podem mudar
- ❌ Docstrings desatualizadas (pior do que nenhuma!)

```python
# ❌ Inútil
def get_nome(self):
    """Retorna o nome."""
    return self.nome

# ✅ Útil
def calcular_frete(peso_kg, cep_destino):
    """Calcula o frete em reais.

    Args:
        peso_kg: Peso do pacote em quilos (máx. 30).
        cep_destino: CEP no formato '12345-678'.

    Returns:
        Valor do frete em reais, arredondado a 2 casas.

    Raises:
        ValueError: Se o peso exceder 30 kg.
    """
```

---

## 6. Doctests: exemplos que viram testes

Exemplos no formato do REPL (`>>>`) podem ser **executados** como testes:

```python
def fatorial(n):
    """Calcula n!.

    >>> fatorial(5)
    120
    >>> fatorial(0)
    1
    """
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
```bash
python -m doctest -v arquivo.py
```
Se a saída real for diferente da documentada, o teste falha. Assim, seus **exemplos nunca ficam desatualizados**. Para suítes maiores, veja [[08 - Avançado/06 - Testes com unittest e pytest|pytest]].

---

## 7. Gerando documentação automaticamente

| Ferramenta | O que faz |
|------------|-----------|
| `help()` / `pydoc` | Mostra docstrings no terminal (`python -m pydoc math`) |
| **Sphinx** | Gera sites/PDFs de documentação a partir das docstrings |
| **MkDocs + mkdocstrings** | Documentação em Markdown (muito popular) |
| **pdoc** | Gera HTML de API sem configuração |
| **Editores/IDEs** | Mostram docstrings em tooltips e autocompletar |

```bash
python -m pydoc -b        # abre documentação no navegador
python -m pydoc geometria # documentação de um módulo seu
```

> [!tip] Verificadores de estilo
> O **Ruff** (regras `D`, que implementam o pydocstyle) verifica se as docstrings seguem a PEP 257:
> ```bash
> ruff check --select D .
> ```

---

## 8. Docstring ou comentário?

```python
def aplicar_desconto(preco, cliente_vip):
    """Retorna o preço com desconto.

    Clientes VIP recebem 20%; os demais, 5%.
    """
    # Regra comercial 2024: o desconto VIP não acumula com cupons
    taxa = 0.20 if cliente_vip else 0.05
    return preco * (1 - taxa)
```
- **Docstring** → contrato público: *o que a função faz*
- **Comentário** → *por que* o código faz algo de forma específica

Revise em [[01 - Fundamentos/06 - Comentários e Boas Práticas|Comentários e Boas Práticas]].

---

> [!question] Exercícios
> 1. Escreva uma docstring (estilo Google) para `def celsius_para_fahrenheit(c)`.
> 2. Corrija: por que `help(f)` não mostra nada?
>    ```python
>    def f(x):
>        y = x * 2
>        """Dobra x."""
>        return y
>    ```
> 3. Acrescente um doctest a `eh_palindromo(texto)` e rode com `python -m doctest -v`.
> 4. Documente o módulo `geometria.py` e uma classe `Retangulo` com atributos e métodos.
> 5. Qual é a melhor primeira linha? (a) `"""Esta função calcula o IMC."""` (b) `"""Calcula o IMC."""`
> 6. Use `help()` e `__doc__` para ler a documentação de `str.split`.

> [!success]- Soluções
> 1. ```python
>    def celsius_para_fahrenheit(c):
>        """Converte graus Celsius em Fahrenheit.
>
>        Args:
>            c: Temperatura em graus Celsius.
>
>        Returns:
>            Temperatura equivalente em graus Fahrenheit.
>        """
>        return c * 9 / 5 + 32
>    ```
> 2. A string vem **depois** de uma instrução; só é docstring se for a **primeira** instrução do corpo. Mova-a para a linha logo abaixo do `def`.
> 3. ```python
>    def eh_palindromo(texto):
>        """Indica se o texto é palíndromo (ignora maiúsculas e espaços).
>
>        >>> eh_palindromo("Socorram me subi no onibus em marrocos")
>        True
>        >>> eh_palindromo("Python")
>        False
>        """
>        limpo = texto.replace(" ", "").lower()
>        return limpo == limpo[::-1]
>    ```
> 4. ```python
>    """Geometria básica."""
>
>    class Retangulo:
>        """Retângulo definido por base e altura.
>
>        Attributes:
>            base: Comprimento da base.
>            altura: Comprimento da altura.
>        """
>
>        def __init__(self, base, altura):
>            self.base = base
>            self.altura = altura
>
>        def area(self):
>            """Retorna a área do retângulo."""
>            return self.base * self.altura
>    ```
> 5. **(b)**: imperativo, curto e direto (PEP 257).
> 6. `help(str.split)` e `print(str.split.__doc__)`.

---

⬅️ [[03 - Funções e Modularização/05 - Virtual Environments e pip|Virtual Environments e pip]] | ➡️ [[03 - Funções e Modularização/07 - Exercícios de Funções e Modularização|Exercícios do Módulo 03]]

#python #basico #docstrings #documentacao #pep257 #doctest
