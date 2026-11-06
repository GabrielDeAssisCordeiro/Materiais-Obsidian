---
titulo: "Exercícios de Fundamentos"
tags: [python, basico, exercicios, pratica]
nivel: iniciante
criado: 2026-10-05
modulo: "01 - Fundamentos"
---

# 🏋️ Exercícios de Fundamentos

Exercícios progressivos para fixar o **Módulo 01**. Tente resolver **sozinho(a)** antes de abrir cada solução (callouts recolhidos).

> [!tip] Como praticar
> 1. Escreva a solução em um arquivo `.py` (ex.: `ex01.py`).
> 2. Rode, teste com valores diferentes e use o **debugger** se travar.
> 3. Só então compare com a solução.
> 4. Se errou, volte à nota indicada e releia.

**Revise antes:** [[01 - Fundamentos/02 - Sintaxe Básica e Variáveis|Variáveis]] · [[01 - Fundamentos/03 - Tipos de Dados Primitivos|Tipos]] · [[01 - Fundamentos/04 - Operadores|Operadores]] · [[01 - Fundamentos/05 - Entrada e Saída|Entrada e Saída]]

---

## 🟢 Nível 1: Aquecimento

> [!question] Exercício 1: Olá, personalizado
> Peça o nome do usuário e imprima `Olá, <nome>! Bem-vindo(a) ao Python.`

> [!success]- Solução
> ```python
> nome = input("Qual é o seu nome? ")
> print(f"Olá, {nome}! Bem-vindo(a) ao Python.")
> ```

> [!question] Exercício 2: Soma de dois números
> Peça dois números inteiros e mostre a soma no formato `A + B = C`.

> [!success]- Solução
> ```python
> a = int(input("Primeiro número: "))
> b = int(input("Segundo número: "))
> print(f"{a} + {b} = {a + b}")
> ```
> [!warning] Lembrete
> Sem o `int()`, `input()` devolve texto e `"3" + "4"` daria `"34"`.

> [!question] Exercício 3: Troca de variáveis
> Dadas `a = "esquerda"` e `b = "direita"`, troque seus valores **sem** variável auxiliar e imprima ambas.

> [!success]- Solução
> ```python
> a, b = "esquerda", "direita"
> a, b = b, a
> print(a, b)   # direita esquerda
> ```

---

## 🟡 Nível 2: Cálculos

> [!question] Exercício 4: Média de três notas
> Leia três notas (`float`) e mostre a média com **1 casa decimal**. Se a média for `>= 6`, imprima também `Aprovado: True`, senão `Aprovado: False` (use um operador de comparação, ainda sem `if`).

> [!success]- Solução
> ```python
> n1 = float(input("Nota 1: "))
> n2 = float(input("Nota 2: "))
> n3 = float(input("Nota 3: "))
>
> media = (n1 + n2 + n3) / 3
> print(f"Média: {media:.1f}")
> print(f"Aprovado: {media >= 6}")
> ```
> [!warning] Armadilha
> `n1 + n2 + n3 / 3` divide só a última nota (precedência!). Os parênteses são obrigatórios.

> [!question] Exercício 5: Conversor de temperatura
> Leia uma temperatura em °C e mostre em °F (`F = C × 9/5 + 32`) e em Kelvin (`K = C + 273.15`).

> [!success]- Solução
> ```python
> c = float(input("Temperatura em °C: "))
> print(f"{c:.1f} °C = {c * 9 / 5 + 32:.1f} °F = {c + 273.15:.2f} K")
> ```

> [!question] Exercício 6: Segundos para horas
> Leia um total de segundos (inteiro) e mostre no formato `HH:MM:SS` (ex.: `3725` → `01:02:05`). Dica: `//`, `%` e formatação `02d`.

> [!success]- Solução
> ```python
> total = int(input("Segundos: "))
>
> horas = total // 3600
> minutos = (total % 3600) // 60
> segundos = total % 60
>
> print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
> ```
> Ou com `divmod`:
> ```python
> horas, resto = divmod(total, 3600)
> minutos, segundos = divmod(resto, 60)
> ```

> [!question] Exercício 7: Área e perímetro
> Leia a base e a altura de um retângulo e mostre área e perímetro, cada um em uma linha, com 2 casas decimais.

> [!success]- Solução
> ```python
> base = float(input("Base: "))
> altura = float(input("Altura: "))
> print(f"Área: {base * altura:.2f}")
> print(f"Perímetro: {2 * (base + altura):.2f}")
> ```

---

## 🟠 Nível 3: Textos

> [!question] Exercício 8: Análise de texto
> Leia uma frase e mostre: (a) quantidade de caracteres, (b) a frase em maiúsculas, (c) a frase invertida, (d) quantas vezes a letra `a` aparece (ignorando maiúsculas/minúsculas).

> [!success]- Solução
> ```python
> frase = input("Digite uma frase: ")
>
> print(f"Caracteres: {len(frase)}")
> print(f"Maiúsculas: {frase.upper()}")
> print(f"Invertida: {frase[::-1]}")
> print(f"Letras 'a': {frase.lower().count('a')}")
> ```

> [!question] Exercício 9: Nome limpo
> Leia o nome completo de uma pessoa (pode vir com espaços extras e maiúsculas/minúsculas bagunçadas, ex.: `"  jOÃO   da silva "`). Mostre o nome formatado como `João Da Silva` e a quantidade de letras (sem contar espaços).

> [!success]- Solução
> ```python
> nome = input("Nome completo: ")
> nome_limpo = " ".join(nome.split()).title()   # split() sem argumento remove espaços extras
>
> print(f"Nome: {nome_limpo}")
> print(f"Letras: {len(nome_limpo.replace(' ', ''))}")
> ```

> [!question] Exercício 10: Iniciais
> Leia nome e sobrenome em duas entradas e imprima as iniciais em maiúsculas (ex.: `ada` / `lovelace` → `A.L.`).

> [!success]- Solução
> ```python
> nome = input("Nome: ").strip()
> sobrenome = input("Sobrenome: ").strip()
> print(f"{nome[0].upper()}.{sobrenome[0].upper()}.")
> ```

---

## 🔴 Nível 4: Desafios

> [!question] Exercício 11: Troco
> O usuário informa o valor da compra e o valor pago (ambos inteiros em reais). Mostre o troco e **quantas notas** de 100, 50, 20, 10, 5 e 2 e quantas moedas de 1 real são necessárias (use `//` e `%`).

> [!success]- Solução
> ```python
> compra = int(input("Valor da compra: "))
> pago = int(input("Valor pago: "))
> troco = pago - compra
> print(f"Troco: R$ {troco}")
>
> for nota in (100, 50, 20, 10, 5, 2, 1):
>     quantidade, troco = divmod(troco, nota)
>     if quantidade:
>         print(f"{quantidade} x R$ {nota}")
> ```
> O `for` e o `if` ainda não foram vistos em detalhe: espie [[02 - Controle de Fluxo e Estruturas de Dados/02 - Loops for e while|Loops]]. Sem eles, daria para repetir `divmod` seis vezes, o que mostra por que laços existem.

> [!question] Exercício 12: Juros compostos
> Leia o capital inicial, a taxa de juros mensal (em %) e o número de meses. Calcule o montante com `M = C × (1 + i)^n` e mostre `Montante: R$ 1,234.56` (com separador de milhar e 2 casas).

> [!success]- Solução
> ```python
> capital = float(input("Capital inicial: R$ "))
> taxa = float(input("Taxa mensal (%): ")) / 100
> meses = int(input("Meses: "))
>
> montante = capital * (1 + taxa) ** meses
> print(f"Montante: R$ {montante:,.2f}")
> ```
> Para valores monetários reais, considere `Decimal` (veja [[01 - Fundamentos/03 - Tipos de Dados Primitivos|a armadilha do float]]).

> [!question] Exercício 13: Descubra o erro
> Cada trecho abaixo tem um bug. Encontre e corrija sem rodar.
> ```python
> # (a)
> idade = input("Idade: ")
> print("Daqui a 5 anos:", idade + 5)
>
> # (b)
> media = 7 + 8 + 9 / 3
>
> # (c)
> list = [1, 2, 3]
> outra = list("abc")
>
> # (d)
> if nome = "Ada":
>     print("Oi")
>
> # (e)
> contador = 0
> contador++
> ```

> [!success]- Solução
> ```python
> # (a) input devolve str
> idade = int(input("Idade: "))
>
> # (b) precedência: / vem antes de +
> media = (7 + 8 + 9) / 3
>
> # (c) "list" sobrescreveu a função nativa
> numeros = [1, 2, 3]
> outra = list("abc")
>
> # (d) = é atribuição; == é comparação (e faltam os dois-pontos corretos)
> if nome == "Ada":
>     print("Oi")
>
> # (e) Python não tem ++
> contador += 1
> ```

> [!question] Exercício 14: Mini ficha
> Leia nome, idade, altura (m) e peso (kg) e imprima uma ficha alinhada. Calcule o IMC (`peso / altura²`):
> ```text
> ========== FICHA ==========
> Nome   : Ada Lovelace
> Idade  : 28 anos
> Altura : 1.68 m
> Peso   : 60.0 kg
> IMC    : 21.26
> ===========================
> ```

> [!success]- Solução
> ```python
> nome = input("Nome: ").strip().title()
> idade = int(input("Idade: "))
> altura = float(input("Altura (m): "))
> peso = float(input("Peso (kg): "))
>
> imc = peso / altura ** 2
>
> print(" FICHA ".center(27, "="))
> print(f"Nome   : {nome}")
> print(f"Idade  : {idade} anos")
> print(f"Altura : {altura:.2f} m")
> print(f"Peso   : {peso:.1f} kg")
> print(f"IMC    : {imc:.2f}")
> print("=" * 27)
> ```

---

## 🧪 Quiz relâmpago

> [!question] Responda sem rodar o código
> 1. `print(7 // 2, 7 % 2, 7 / 2)`
> 2. `print(type(10 / 5))`
> 3. `print("ab" * 3)`
> 4. `print(bool("0"), bool(0))`
> 5. `print("Python"[1:4])`
> 6. `print(2 ** 3 ** 2)`
> 7. `print(not 0 and 5)`
> 8. `a = [1]; b = a; b.append(2); print(a)`

> [!success]- Respostas
> 1. `3 1 3.5`
> 2. `<class 'float'>`
> 3. `ababab`
> 4. `True False`
> 5. `yth`
> 6. `512` (`**` associa da direita para a esquerda: `3 ** 2 = 9`, `2 ** 9 = 512`)
> 7. `5` (`not 0` é `True`; `True and 5` devolve `5`)
> 8. `[1, 2]` (mesma lista, duas referências)

---

## ✅ Checklist do módulo

- [ ] Instalei o Python e rodei um script pelo terminal
- [ ] Usei o REPL para experimentar
- [ ] Sei criar variáveis e escolho bons nomes
- [ ] Conheço `int`, `float`, `str`, `bool` e `None`
- [ ] Domino f-strings e fatiamento de strings
- [ ] Entendo a precedência de operadores e a diferença entre `==` e `is`
- [ ] Sei usar `input()` convertendo o tipo
- [ ] Sigo a PEP 8 básica e comento o *porquê*
- [ ] Resolvi pelo menos 10 exercícios deste arquivo

---

## 🚀 Próximo módulo
➡️ [[02 - Controle de Fluxo e Estruturas de Dados/01 - if elif else e match case|Módulo 02: Controle de Fluxo e Estruturas de Dados]]

⬅️ [[01 - Fundamentos/06 - Comentários e Boas Práticas|Comentários e Boas Práticas]] · ⬆️ [[Índice - Python|Índice]]

#python #basico #exercicios #pratica #fundamentos
