---
titulo: "Exercícios de Fluxo e Estruturas de Dados"
tags: [python, basico, exercicios, pratica, estruturas-de-dados]
nivel: iniciante
criado: 2026-10-05
modulo: "02 - Controle de Fluxo e Estruturas de Dados"
---

# 🏋️ Exercícios de Fluxo e Estruturas de Dados

Exercícios **progressivos** para fixar o **Módulo 02**. Resolva sozinho(a) antes de abrir cada solução (callouts recolhidos).

> [!tip] Como praticar
> 1. Escreva a solução em um arquivo (`m02_ex01.py`...).
> 2. Teste com entradas normais **e** com casos extremos (lista vazia, zero, texto estranho).
> 3. Use o **debugger** se travar.
> 4. Compare com a solução e tente uma versão mais pythônica.

**Revise antes:** [[02 - Controle de Fluxo e Estruturas de Dados/01 - if elif else e match case|Condicionais]] · [[02 - Controle de Fluxo e Estruturas de Dados/02 - Loops for e while|Loops]] · [[02 - Controle de Fluxo e Estruturas de Dados/03 - Listas|Listas]] · [[02 - Controle de Fluxo e Estruturas de Dados/04 - Tuplas|Tuplas]] · [[02 - Controle de Fluxo e Estruturas de Dados/05 - Sets|Sets]] · [[02 - Controle de Fluxo e Estruturas de Dados/06 - Dicionários|Dicionários]] · [[02 - Controle de Fluxo e Estruturas de Dados/07 - Comprehensions|Comprehensions]]

---

## 🟢 Nível 1: Aquecimento

> [!question] 1. Par ou ímpar
> Leia um inteiro e diga se é par ou ímpar.

> [!success]- Solução
> ```python
> n = int(input("Número: "))
> print("par" if n % 2 == 0 else "ímpar")
> ```

> [!question] 2. Maior de três
> Leia três números e mostre o maior, **sem** usar `max()`.

> [!success]- Solução
> ```python
> a, b, c = (float(input(f"Número {i}: ")) for i in (1, 2, 3))
> if a >= b and a >= c:
>     maior = a
> elif b >= c:
>     maior = b
> else:
>     maior = c
> print(f"Maior: {maior}")
> ```

> [!question] 3. Contagem regressiva
> Mostre a contagem de 10 até 1 e, no final, `Fogo!`.

> [!success]- Solução
> ```python
> for n in range(10, 0, -1):
>     print(n)
> print("Fogo!")
> ```

> [!question] 4. Soma e média de uma lista
> Dada `notas = [7.5, 8, 6.5, 9]`, mostre soma, média e quantas notas estão acima da média.

> [!success]- Solução
> ```python
> notas = [7.5, 8, 6.5, 9]
> soma = sum(notas)
> media = soma / len(notas)
> acima = len([n for n in notas if n > media])
> print(f"Soma: {soma} | Média: {media:.2f} | Acima da média: {acima}")
> ```

---

## 🟡 Nível 2: Fluxo e listas

> [!question] 5. FizzBuzz
> De 1 a 30: imprima `Fizz` para múltiplos de 3, `Buzz` para múltiplos de 5, `FizzBuzz` para múltiplos de ambos e o próprio número nos demais.

> [!success]- Solução
> ```python
> for n in range(1, 31):
>     if n % 15 == 0:
>         print("FizzBuzz")
>     elif n % 3 == 0:
>         print("Fizz")
>     elif n % 5 == 0:
>         print("Buzz")
>     else:
>         print(n)
> ```
> [!warning] Ordem
> O teste do `15` precisa vir **primeiro**, senão `15` cairia em "Fizz".

> [!question] 6. Adivinhe o número
> O programa sorteia um número de 1 a 100 (`random.randint`). O usuário chuta até acertar; a cada chute diga `maior` ou `menor` e, no final, mostre o número de tentativas.

> [!success]- Solução
> ```python
> import random
>
> segredo = random.randint(1, 100)
> tentativas = 0
>
> while True:
>     chute = int(input("Seu chute (1-100): "))
>     tentativas += 1
>     if chute < segredo:
>         print("Maior!")
>     elif chute > segredo:
>         print("Menor!")
>     else:
>         print(f"Acertou em {tentativas} tentativas!")
>         break
> ```

> [!question] 7. Menu de lista de tarefas
> Crie um menu em loop com as opções: adicionar tarefa, listar (numeradas), remover por número e sair. Use `match/case`.

> [!success]- Solução
> ```python
> tarefas = []
>
> while True:
>     print("\n1-Adicionar  2-Listar  3-Remover  4-Sair")
>     match input("Opção: ").strip():
>         case "1":
>             tarefas.append(input("Tarefa: ").strip())
>         case "2":
>             if not tarefas:
>                 print("Nenhuma tarefa.")
>             for i, t in enumerate(tarefas, start=1):
>                 print(f"{i}. {t}")
>         case "3":
>             n = int(input("Número da tarefa: "))
>             if 1 <= n <= len(tarefas):
>                 print(f"Removida: {tarefas.pop(n - 1)}")
>             else:
>                 print("Número inválido")
>         case "4":
>             break
>         case _:
>             print("Opção inválida")
> ```

> [!question] 8. Ordenar sem `sort`
> Implemente o **bubble sort** para ordenar `[5, 2, 9, 1, 7]` em ordem crescente.

> [!success]- Solução
> ```python
> nums = [5, 2, 9, 1, 7]
> n = len(nums)
>
> for i in range(n - 1):
>     trocou = False
>     for j in range(n - 1 - i):
>         if nums[j] > nums[j + 1]:
>             nums[j], nums[j + 1] = nums[j + 1], nums[j]
>             trocou = True
>     if not trocou:
>         break
>
> print(nums)    # [1, 2, 5, 7, 9]
> ```

---

## 🟠 Nível 3: Tuplas, sets e dicionários

> [!question] 9. Estatísticas com tupla
> Escreva `estatisticas(numeros)` que devolva `(menor, maior, média)` e use desempacotamento para exibir o resultado.

> [!success]- Solução
> ```python
> def estatisticas(numeros):
>     return min(numeros), max(numeros), sum(numeros) / len(numeros)
>
> menor, maior, media = estatisticas([4, 9, 1, 7])
> print(f"Menor: {menor} | Maior: {maior} | Média: {media:.2f}")
> ```

> [!question] 10. Frequência de palavras
> Leia um texto e mostre as 3 palavras mais frequentes (ignore maiúsculas e pontuação simples `.,!?`).

> [!success]- Solução
> ```python
> texto = input("Texto: ").lower()
> for p in ".,!?":
>     texto = texto.replace(p, "")
>
> freq = {}
> for palavra in texto.split():
>     freq[palavra] = freq.get(palavra, 0) + 1
>
> top3 = sorted(freq.items(), key=lambda par: par[1], reverse=True)[:3]
> for palavra, qtd in top3:
>     print(f"{palavra}: {qtd}")
> ```
> Versão curta: `Counter(texto.split()).most_common(3)` ([[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|collections]]).

> [!question] 11. Comparando turmas
> Dados `turma_a = {"Ana", "Bia", "Caio", "Davi"}` e `turma_b = {"Bia", "Davi", "Eva"}`, mostre: quem está nas duas, quem está só na A, quem está só em uma delas e o total de alunos distintos.

> [!success]- Solução
> ```python
> print(turma_a & turma_b)    # nas duas
> print(turma_a - turma_b)    # só na A
> print(turma_a ^ turma_b)    # em apenas uma
> print(len(turma_a | turma_b))   # total distinto: 5
> ```

> [!question] 12. Anagramas
> Escreva `eh_anagrama(p1, p2)` que ignore maiúsculas e espaços.

> [!success]- Solução
> ```python
> def eh_anagrama(p1, p2):
>     limpa = lambda s: sorted(s.lower().replace(" ", ""))
>     return limpa(p1) == limpa(p2)
>
> print(eh_anagrama("Amor", "Roma"))        # True
> print(eh_anagrama("Python", "Typhon"))    # True
> ```

> [!question] 13. Boletim
> Dado o dicionário abaixo, mostre cada aluno com a média (1 casa decimal) e a situação (`Aprovado` se média ≥ 6, senão `Reprovado`), além do melhor aluno.
> ```python
> alunos = {
>     "Ana": [8, 9, 7],
>     "Bruno": [5, 6, 4],
>     "Carla": [10, 9, 9],
> }
> ```

> [!success]- Solução
> ```python
> medias = {nome: sum(ns) / len(ns) for nome, ns in alunos.items()}
>
> for nome, media in medias.items():
>     situacao = "Aprovado" if media >= 6 else "Reprovado"
>     print(f"{nome:<8}{media:>5.1f}  {situacao}")
>
> melhor = max(medias, key=medias.get)
> print(f"\nMelhor aluno: {melhor} ({medias[melhor]:.1f})")
> ```

---

## 🔴 Nível 4: Desafios

> [!question] 14. Matriz identidade e transposta
> Crie uma matriz identidade 4×4 com comprehension e depois a transposta de `[[1, 2, 3], [4, 5, 6]]`.

> [!success]- Solução
> ```python
> identidade = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
>
> m = [[1, 2, 3], [4, 5, 6]]
> transposta = [[linha[c] for linha in m] for c in range(len(m[0]))]
> # ou: [list(col) for col in zip(*m)]
> ```

> [!question] 15. Verificador de parênteses
> Verifique se uma string de parênteses/colchetes/chaves está balanceada (`"{[()]}"` → `True`, `"{[(])}"` → `False`). Dica: use uma lista como **pilha** e um dicionário para os pares.

> [!success]- Solução
> ```python
> def balanceado(texto):
>     pares = {")": "(", "]": "[", "}": "{"}
>     pilha = []
>     for c in texto:
>         if c in "([{":
>             pilha.append(c)
>         elif c in pares:
>             if not pilha or pilha.pop() != pares[c]:
>                 return False
>     return not pilha
>
> print(balanceado("{[()]}"))    # True
> print(balanceado("{[(])}"))    # False
> ```

> [!question] 16. Agrupar por inicial
> Dada a lista de nomes `["Ana", "Alice", "Bruno", "Bia", "Carla"]`, produza `{"A": [...], "B": [...], "C": [...]}` com os nomes ordenados em cada grupo.

> [!success]- Solução
> ```python
> nomes = ["Ana", "Alice", "Bruno", "Bia", "Carla"]
> grupos = {}
> for nome in nomes:
>     grupos.setdefault(nome[0], []).append(nome)
>
> grupos = {inicial: sorted(lista) for inicial, lista in sorted(grupos.items())}
> print(grupos)
> ```

> [!question] 17. Descubra os bugs
> Cada trecho abaixo tem um erro. Encontre e corrija **sem rodar**.
> ```python
> # (a)
> vazio = {}
> vazio.add(1)
>
> # (b)
> matriz = [[0] * 3] * 3
> matriz[0][0] = 1          # queria mudar só a 1ª linha
>
> # (c)
> t = (5)
> print(len(t))
>
> # (d)
> numeros = [1, 2, 3, 4]
> for n in numeros:
>     if n % 2 == 0:
>         numeros.remove(n)
>
> # (e)
> lista = [3, 1, 2]
> lista = lista.sort()
> print(lista[0])
> ```

> [!success]- Solução
> ```python
> # (a) {} é um dict; set vazio é set()
> vazio = set()
> vazio.add(1)
>
> # (b) todas as linhas são a mesma lista
> matriz = [[0] * 3 for _ in range(3)]
>
> # (c) falta a vírgula: (5) é int
> t = (5,)
>
> # (d) modifica a lista enquanto percorre
> numeros = [n for n in numeros if n % 2 != 0]
>
> # (e) sort() devolve None
> lista.sort()          # ou lista = sorted(lista)
> ```

> [!question] 18. Mini-projeto: Jogo da Forca
> Escolha uma palavra de uma lista; o jogador tem 6 erros. A cada rodada mostre a palavra com `_` nas letras não descobertas, as letras já tentadas (set) e as vidas restantes. Termine com vitória ou derrota.

> [!success]- Solução
> ```python
> import random
>
> palavras = ["python", "variavel", "funcao", "dicionario", "lista"]
> segredo = random.choice(palavras)
> tentadas = set()
> vidas = 6
>
> while vidas > 0:
>     painel = " ".join(c if c in tentadas else "_" for c in segredo)
>     print(f"\n{painel}")
>     print(f"Tentadas: {sorted(tentadas)} | Vidas: {vidas}")
>
>     if "_" not in painel:
>         print("🎉 Você venceu!")
>         break
>
>     letra = input("Letra: ").strip().lower()
>     if len(letra) != 1 or not letra.isalpha():
>         print("Digite UMA letra.")
>         continue
>     if letra in tentadas:
>         print("Você já tentou essa.")
>         continue
>
>     tentadas.add(letra)
>     if letra not in segredo:
>         vidas -= 1
>         print("Errou!")
> else:
>     print(f"💀 Fim de jogo! A palavra era: {segredo}")
> ```
> Note o `else` do `while`: roda quando o laço termina **sem** `break` (as vidas acabaram).

---

## 🧪 Quiz relâmpago

> [!question] Responda sem rodar o código
> 1. `print(list(range(10, 0, -3)))`
> 2. `print({1, 2, 2, 3} == {3, 2, 1})`
> 3. `print([x for x in "banana" if x != "a"])`
> 4. `d = {"a": 1}; print(d.get("b", 0))`
> 5. `print(type((1)), type((1,)))`
> 6. `a = [1, 2]; b = a; b.append(3); print(a)`
> 7. `print({k: v for k, v in zip("ab", [1, 2])})`
> 8. `for i in range(3): pass` → quanto vale `i` depois?

> [!success]- Respostas
> 1. `[10, 7, 4, 1]`
> 2. `True`
> 3. `['b', 'n', 'n']`
> 4. `0`
> 5. `<class 'int'> <class 'tuple'>`
> 6. `[1, 2, 3]`
> 7. `{'a': 1, 'b': 2}`
> 8. `2`

---

## ✅ Checklist do módulo

- [ ] Uso `if/elif/else` e sei quando preferir `match/case`
- [ ] Evito loops infinitos e uso `break`, `continue` e `else` de laços
- [ ] Domino `range`, `enumerate` e `zip`
- [ ] Sei criar, fatiar, ordenar e copiar **listas** (e evito as armadilhas de cópia)
- [ ] Reconheço quando usar **tupla** (e sei a vírgula da tupla de 1 item)
- [ ] Uso **sets** para unicidade e buscas rápidas
- [ ] Manipulo **dicionários** (`get`, `items`, `setdefault`, mesclagem)
- [ ] Escrevo **comprehensions** legíveis (list, dict, set e geradoras)
- [ ] Resolvi pelo menos 12 dos exercícios acima

---

## 🚀 Próximo módulo
➡️ [[03 - Funções e Modularização/01 - Definindo Funções|Módulo 03: Funções e Modularização]]

⬅️ [[02 - Controle de Fluxo e Estruturas de Dados/07 - Comprehensions|Comprehensions]] · ⬆️ [[Índice - Python|Índice]]

#python #basico #exercicios #pratica #estruturas-de-dados #fluxo
