---
titulo: "Exercícios de Programação Orientada a Objetos"
tags: [python, intermediario, exercicios, pratica, poo]
nivel: intermediario
criado: 2026-10-05
modulo: "04 - Programação Orientada a Objetos"
---

# 🏋️ Exercícios de Programação Orientada a Objetos

Exercícios **progressivos** para fixar o **Módulo 04**. Resolva sozinho(a) antes de abrir cada solução.

> [!tip] Como praticar
> 1. Escreva cada solução em um arquivo próprio (`m04_ex01.py`...).
> 2. Faça **diagramas rápidos** (papel ou Mermaid) antes de codar: quais classes? quais relações ("é um" ou "tem um")?
> 3. Teste os **casos de erro** (valores inválidos, estados impossíveis).
> 4. Use o **debugger** e inspecione `obj.__dict__`.

**Revise antes:** [[04 - Programação Orientada a Objetos/01 - Classes e Objetos|Classes]] · [[04 - Programação Orientada a Objetos/02 - Atributos e Métodos|Atributos e Métodos]] · [[04 - Programação Orientada a Objetos/03 - Herança Polimorfismo e Encapsulamento|Herança/Polimorfismo]] · [[04 - Programação Orientada a Objetos/04 - Propriedades e Métodos Mágicos|Property/Dunder]] · [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots|Dataclasses]] · [[04 - Programação Orientada a Objetos/06 - Design Patterns Básicos|Patterns]]

---

## 🟢 Nível 1: Classes e objetos

> [!question] 1. Pessoa
> Crie `Pessoa` com `nome` e `idade`, o método `apresentar()` (`"Olá, sou Ada e tenho 36 anos"`) e `fazer_aniversario()` (+1 ano). Crie `__repr__`.

> [!success]- Solução
> ```python
> class Pessoa:
>     def __init__(self, nome, idade):
>         self.nome = nome
>         self.idade = idade
>
>     def apresentar(self):
>         return f"Olá, sou {self.nome} e tenho {self.idade} anos"
>
>     def fazer_aniversario(self):
>         self.idade += 1
>
>     def __repr__(self):
>         return f"Pessoa(nome={self.nome!r}, idade={self.idade})"
>
> p = Pessoa("Ada", 36)
> p.fazer_aniversario()
> print(p.apresentar(), p)
> ```

> [!question] 2. Conta bancária
> Crie `ContaBancaria` (titular, saldo inicial 0) com `depositar`, `sacar` e `extrato`. Levante `ValueError` para valor ≤ 0 e para saque acima do saldo. Guarde as **transações** em uma lista.

> [!success]- Solução
> ```python
> class ContaBancaria:
>     def __init__(self, titular, saldo=0.0):
>         self.titular = titular
>         self._saldo = saldo
>         self._transacoes = []
>
>     @property
>     def saldo(self):
>         return self._saldo
>
>     def depositar(self, valor):
>         if valor <= 0:
>             raise ValueError("Valor deve ser positivo")
>         self._saldo += valor
>         self._transacoes.append(("depósito", valor))
>
>     def sacar(self, valor):
>         if valor <= 0:
>             raise ValueError("Valor deve ser positivo")
>         if valor > self._saldo:
>             raise ValueError("Saldo insuficiente")
>         self._saldo -= valor
>         self._transacoes.append(("saque", valor))
>
>     def extrato(self):
>         linhas = [f"{tipo:<9} R$ {valor:>9.2f}" for tipo, valor in self._transacoes]
>         linhas.append(f"{'Saldo':<9} R$ {self._saldo:>9.2f}")
>         return "\n".join(linhas)
> ```

> [!question] 3. Contador de instâncias
> Crie `Aluno` que conte quantas instâncias existem com um atributo de **classe**, e um método de classe `total()`.

> [!success]- Solução
> ```python
> class Aluno:
>     _total = 0
>
>     def __init__(self, nome):
>         self.nome = nome
>         Aluno._total += 1
>
>     @classmethod
>     def total(cls):
>         return cls._total
>
> Aluno("Ana"); Aluno("Bruno")
> print(Aluno.total())    # 2
> ```

---

## 🟡 Nível 2: Herança e polimorfismo

> [!question] 4. Formas geométricas
> Crie a classe abstrata `Forma` com `area()` e `perimetro()` abstratos, e `Retangulo`, `Circulo` e `Triangulo` (3 lados, fórmula de Heron). Itere sobre uma lista e imprima as áreas ordenadas.

> [!success]- Solução
> ```python
> import math
> from abc import ABC, abstractmethod
>
> class Forma(ABC):
>     @abstractmethod
>     def area(self): ...
>     @abstractmethod
>     def perimetro(self): ...
>     def __repr__(self):
>         return f"{type(self).__name__}(área={self.area():.2f})"
>
> class Retangulo(Forma):
>     def __init__(self, b, h): self.b, self.h = b, h
>     def area(self): return self.b * self.h
>     def perimetro(self): return 2 * (self.b + self.h)
>
> class Circulo(Forma):
>     def __init__(self, r): self.r = r
>     def area(self): return math.pi * self.r ** 2
>     def perimetro(self): return 2 * math.pi * self.r
>
> class Triangulo(Forma):
>     def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
>     def perimetro(self): return self.a + self.b + self.c
>     def area(self):
>         p = self.perimetro() / 2
>         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
>
> formas = [Retangulo(3, 4), Circulo(2), Triangulo(3, 4, 5)]
> for f in sorted(formas, key=lambda f: f.area()):
>     print(f)
> ```

> [!question] 5. Animais
> Crie `Animal` (nome, `emitir_som()`) e subclasses `Cachorro`, `Gato`, `Vaca`. Escreva uma função `coro(animais)` que junte todos os sons **sem usar `isinstance`**. Mostre o *duck typing* adicionando uma classe `Robo` (que **não** herda de `Animal`).

> [!success]- Solução
> ```python
> class Animal:
>     def __init__(self, nome): self.nome = nome
>     def emitir_som(self): return "..."
>
> class Cachorro(Animal):
>     def emitir_som(self): return "Au!"
> class Gato(Animal):
>     def emitir_som(self): return "Miau!"
> class Vaca(Animal):
>     def emitir_som(self): return "Muuu!"
>
> class Robo:                          # não herda de Animal
>     def emitir_som(self): return "Bip!"
>
> def coro(seres):
>     return " ".join(s.emitir_som() for s in seres)
>
> print(coro([Cachorro("Rex"), Gato("Mia"), Vaca("Mimosa"), Robo()]))
> ```

> [!question] 6. Funcionários
> Crie `Funcionario` (nome, salário base) com `salario_final()`. Derive `Gerente` (bônus fixo), `Vendedor` (comissão de 5% sobre vendas) e `Estagiario` (salário final = 80% do base). Imprima a folha de pagamento e o total. Use `super().__init__`.

> [!success]- Solução
> ```python
> class Funcionario:
>     def __init__(self, nome, base):
>         self.nome, self.base = nome, base
>     def salario_final(self):
>         return self.base
>
> class Gerente(Funcionario):
>     def __init__(self, nome, base, bonus):
>         super().__init__(nome, base)
>         self.bonus = bonus
>     def salario_final(self):
>         return self.base + self.bonus
>
> class Vendedor(Funcionario):
>     def __init__(self, nome, base, vendas):
>         super().__init__(nome, base)
>         self.vendas = vendas
>     def salario_final(self):
>         return self.base + 0.05 * self.vendas
>
> class Estagiario(Funcionario):
>     def salario_final(self):
>         return self.base * 0.8
>
> equipe = [Gerente("Ana", 6000, 2000), Vendedor("Bruno", 2500, 30000), Estagiario("Carla", 1500)]
> for f in equipe:
>     print(f"{f.nome:<8} R$ {f.salario_final():>9,.2f}")
> print(f"Total: R$ {sum(f.salario_final() for f in equipe):,.2f}")
> ```

> [!question] 7. Composição
> Modele `Carro` que **tem um** `Motor` e **4** `Pneu`s. `Motor` tem `ligar()` e `desligar()`; `Pneu` tem `calibragem`. O `Carro` só anda (`andar()`) se o motor estiver ligado e todos os pneus tiverem calibragem entre 28 e 36.

> [!success]- Solução
> ```python
> class Motor:
>     def __init__(self):
>         self.ligado = False
>     def ligar(self):    self.ligado = True
>     def desligar(self): self.ligado = False
>
> class Pneu:
>     def __init__(self, calibragem=32):
>         self.calibragem = calibragem
>     @property
>     def ok(self):
>         return 28 <= self.calibragem <= 36
>
> class Carro:
>     def __init__(self, modelo):
>         self.modelo = modelo
>         self.motor = Motor()
>         self.pneus = [Pneu() for _ in range(4)]
>
>     def andar(self):
>         if not self.motor.ligado:
>             return "Ligue o motor primeiro"
>         if not all(p.ok for p in self.pneus):
>             return "Calibre os pneus"
>         return f"{self.modelo} em movimento"
> ```

---

## 🟠 Nível 3: Property, dunder e dataclasses

> [!question] 8. `Temperatura` com property
> Crie `Temperatura` com `celsius` (validado ≥ -273.15) e propriedades `fahrenheit` e `kelvin` **com setter** (alterar uma atualiza a outra).

> [!success]- Solução
> ```python
> class Temperatura:
>     def __init__(self, celsius=0.0):
>         self.celsius = celsius
>
>     @property
>     def celsius(self):
>         return self._c
>     @celsius.setter
>     def celsius(self, v):
>         if v < -273.15:
>             raise ValueError("Abaixo do zero absoluto")
>         self._c = float(v)
>
>     @property
>     def fahrenheit(self):
>         return self._c * 9 / 5 + 32
>     @fahrenheit.setter
>     def fahrenheit(self, f):
>         self.celsius = (f - 32) * 5 / 9
>
>     @property
>     def kelvin(self):
>         return self._c + 273.15
>     @kelvin.setter
>     def kelvin(self, k):
>         self.celsius = k - 273.15
> ```

> [!question] 9. `Vetor2D`
> Implemente `Vetor2D` com `+`, `-`, `*` por escalar (nos dois lados), `==`, `abs()`, `bool()`, `__repr__`, `__iter__` (para desempacotar `x, y = v`) e `__hash__`. Teste `sum([v1, v2, v3], Vetor2D(0, 0))`.

> [!success]- Solução
> ```python
> import math
>
> class Vetor2D:
>     def __init__(self, x, y):
>         self.x, self.y = x, y
>     def __add__(self, o):
>         if not isinstance(o, Vetor2D): return NotImplemented
>         return Vetor2D(self.x + o.x, self.y + o.y)
>     def __sub__(self, o):
>         if not isinstance(o, Vetor2D): return NotImplemented
>         return Vetor2D(self.x - o.x, self.y - o.y)
>     def __mul__(self, k):
>         if not isinstance(k, (int, float)): return NotImplemented
>         return Vetor2D(self.x * k, self.y * k)
>     __rmul__ = __mul__
>     def __eq__(self, o):
>         return isinstance(o, Vetor2D) and (self.x, self.y) == (o.x, o.y)
>     def __hash__(self):
>         return hash((self.x, self.y))
>     def __abs__(self):
>         return math.hypot(self.x, self.y)
>     def __bool__(self):
>         return bool(self.x or self.y)
>     def __iter__(self):
>         yield self.x
>         yield self.y
>     def __repr__(self):
>         return f"Vetor2D({self.x}, {self.y})"
>
> v1, v2, v3 = Vetor2D(1, 2), Vetor2D(3, 4), Vetor2D(-1, 0)
> print(sum([v1, v2, v3], Vetor2D(0, 0)))   # Vetor2D(3, 6)
> x, y = v2
> print(2 * v1, abs(v2))                    # Vetor2D(2, 4) 5.0
> ```

> [!question] 10. Coleção personalizada
> Crie `Estoque` que guarda produtos (`dict nome → quantidade`) e implemente `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__iter__` e `__repr__`. Uma consulta a produto inexistente deve devolver `0` em `estoque["x"]`.

> [!success]- Solução
> ```python
> class Estoque:
>     def __init__(self):
>         self._itens = {}
>     def __len__(self):
>         return len(self._itens)
>     def __getitem__(self, nome):
>         return self._itens.get(nome, 0)
>     def __setitem__(self, nome, qtd):
>         if qtd < 0:
>             raise ValueError("Quantidade negativa")
>         self._itens[nome] = qtd
>     def __contains__(self, nome):
>         return nome in self._itens
>     def __iter__(self):
>         return iter(self._itens)
>     def __repr__(self):
>         return f"Estoque({self._itens})"
>
> e = Estoque()
> e["café"] = 10
> e["café"] += 5
> print(e["café"], e["pão"], "café" in e, len(e))   # 15 0 True 1
> ```

> [!question] 11. Dataclasses
> Modele com dataclasses: `Endereco(rua, cidade)` imutável e `Cliente(nome, email, endereco, pedidos)` com `pedidos` lista (use `default_factory`), `email` fora do `repr` e validação de e-mail (`"@"` presente) em `__post_init__`. Converta com `asdict` e mostre `replace`.

> [!success]- Solução
> ```python
> from dataclasses import dataclass, field, asdict, replace
>
> @dataclass(frozen=True)
> class Endereco:
>     rua: str
>     cidade: str
>
> @dataclass
> class Cliente:
>     nome: str
>     email: str = field(repr=False)
>     endereco: Endereco
>     pedidos: list[int] = field(default_factory=list)
>
>     def __post_init__(self):
>         if "@" not in self.email:
>             raise ValueError("E-mail inválido")
> ```
> **Ordem dos campos:** `field(repr=False)` sem `default` continua sendo um campo **obrigatório**, então `endereco` pode vir logo depois dele. O que daria erro seria colocar `endereco` depois de `pedidos`, que tem valor padrão. Uso:
> ```python
> c = Cliente("Ada", "ada@x.com", Endereco("Rua A, 1", "Londres"))
> print(c)                         # e-mail não aparece
> print(asdict(c))
> c2 = replace(c, nome="Ada L.")
> ```

---

## 🔴 Nível 4: Desafios e padrões

> [!question] 12. Descubra os bugs
> ```python
> # (a)
> class Fila:
>     itens = []
>     def entrar(self, x): self.itens.append(x)
>
> # (b)
> class Base:
>     def __init__(self): self.x = 1
> class Filha(Base):
>     def __init__(self): self.y = 2
>
> # (c)
> class Conta:
>     @property
>     def saldo(self): return self.saldo
>
> # (d)
> class P:
>     def __init__(self, v): self.v = v
>     def __eq__(self, o): return self.v == o.v
> print({P(1)})
>
> # (e)
> class Contador:
>     total = 0
>     def __init__(self): self.total += 1
>
> # (f)
> class Forma(ABC):
>     @abstractmethod
>     def area(self): ...
> class Tri(Forma): pass
> Tri()
> ```

> [!success]- Solução
> ```python
> # (a) lista de CLASSE compartilhada → crie em __init__ (self.itens = [])
> # (b) falta super().__init__() → Filha().x dá AttributeError
> class Filha(Base):
>     def __init__(self):
>         super().__init__()
>         self.y = 2
> # (c) recursão infinita no getter → use self._saldo
> # (d) __eq__ sem __hash__ → TypeError: unhashable type; defina __hash__
> # (e) self.total += 1 cria atributo de INSTÂNCIA; use Contador.total += 1
> # (f) Tri não implementa 'area' → TypeError ao instanciar; implemente area()
> ```

> [!question] 13. Sistema de pagamento (Strategy + Factory)
> Crie uma `Compra` que receba o método de pagamento. Implemente `Cartao`, `Pix` (5% de desconto) e `Boleto` (taxa fixa de R$ 3,50) como **estratégias**; use uma **factory** (dict) para criar a estratégia a partir de um texto (`"pix"`) e trate método desconhecido com `ValueError`.

> [!success]- Solução
> ```python
> from abc import ABC, abstractmethod
>
> class Pagamento(ABC):
>     @abstractmethod
>     def total(self, valor): ...
>
> class Cartao(Pagamento):
>     def total(self, valor): return valor
> class Pix(Pagamento):
>     def total(self, valor): return valor * 0.95
> class Boleto(Pagamento):
>     def total(self, valor): return valor + 3.50
>
> METODOS = {"cartao": Cartao, "pix": Pix, "boleto": Boleto}
>
> def criar_pagamento(nome):
>     try:
>         return METODOS[nome.lower()]()
>     except KeyError:
>         raise ValueError(f"Método desconhecido: {nome!r}") from None
>
> class Compra:
>     def __init__(self, valor, pagamento):
>         self.valor, self.pagamento = valor, pagamento
>     def total(self):
>         return self.pagamento.total(self.valor)
>
> print(Compra(100, criar_pagamento("pix")).total())    # 95.0
> ```

> [!question] 14. Observer: loja com estoque
> `Produto` com `estoque` (property). Sempre que o estoque cair abaixo de 5, notifique observadores (`email_compras`, `log`). Implemente com uma lista de callbacks.

> [!success]- Solução
> ```python
> class Produto:
>     LIMITE = 5
>
>     def __init__(self, nome, estoque):
>         self.nome = nome
>         self._estoque = estoque
>         self._observadores = []
>
>     def observar(self, cb):
>         self._observadores.append(cb)
>
>     @property
>     def estoque(self):
>         return self._estoque
>
>     @estoque.setter
>     def estoque(self, valor):
>         self._estoque = valor
>         if valor < self.LIMITE:
>             for cb in self._observadores:
>                 cb(self)
>
> def email_compras(p): print(f"📧 Comprar mais {p.nome}! Restam {p.estoque}")
> def log(p): print(f"[log] estoque baixo: {p.nome}={p.estoque}")
>
> cafe = Produto("Café", 10)
> cafe.observar(email_compras)
> cafe.observar(log)
> cafe.estoque = 3
> ```

> [!question] 15. Mini-projeto: Biblioteca
> Modele um sistema de **biblioteca** com: `Livro` (dataclass: título, autor, ISBN, disponível), `Membro` (nome, empréstimos, limite de 3) e `Biblioteca` (acervo, membros). Operações: `emprestar(isbn, membro)`, `devolver(isbn, membro)`, `buscar(termo)` e relatório. Use exceções próprias (`LivroIndisponivel`, `LimiteExcedido`), `__repr__`, `property` e um **Observer** que registre cada evento num log.
>
> Dica de modelagem:
> ```mermaid
> classDiagram
>     class Biblioteca {
>         -dict acervo
>         -dict membros
>         +emprestar(isbn, membro)
>         +devolver(isbn, membro)
>         +buscar(termo)
>     }
>     class Livro {
>         +str titulo
>         +str autor
>         +str isbn
>         +bool disponivel
>     }
>     class Membro {
>         +str nome
>         +list emprestimos
>         +pode_emprestar() bool
>     }
>     Biblioteca "1" o-- "*" Livro
>     Biblioteca "1" o-- "*" Membro
>     Membro "1" --> "*" Livro : possui
> ```

> [!success]- Solução (completa)
> ```python
> from dataclasses import dataclass, field
>
> class BibliotecaError(Exception):
>     """Erro base do domínio."""
>
> class LivroIndisponivel(BibliotecaError):
>     pass
>
> class LimiteExcedido(BibliotecaError):
>     pass
>
>
> @dataclass
> class Livro:
>     titulo: str
>     autor: str
>     isbn: str
>     disponivel: bool = True
>
>
> @dataclass
> class Membro:
>     nome: str
>     emprestimos: list[Livro] = field(default_factory=list)
>     LIMITE = 3            # sem anotação: atributo de classe, não campo
>
>     @property
>     def pode_emprestar(self):
>         return len(self.emprestimos) < self.LIMITE
>
>
> class Biblioteca:
>     def __init__(self):
>         self._acervo: dict[str, Livro] = {}
>         self._observadores = []
>
>     def observar(self, callback):
>         self._observadores.append(callback)
>
>     def _notificar(self, evento, livro, membro):
>         for cb in self._observadores:
>             cb(evento, livro, membro)
>
>     def adicionar(self, livro):
>         self._acervo[livro.isbn] = livro
>
>     def buscar(self, termo):
>         t = termo.lower()
>         return [l for l in self._acervo.values()
>                 if t in l.titulo.lower() or t in l.autor.lower()]
>
>     def emprestar(self, isbn, membro):
>         livro = self._acervo[isbn]
>         if not livro.disponivel:
>             raise LivroIndisponivel(livro.titulo)
>         if not membro.pode_emprestar:
>             raise LimiteExcedido(membro.nome)
>         livro.disponivel = False
>         membro.emprestimos.append(livro)
>         self._notificar("emprestimo", livro, membro)
>
>     def devolver(self, isbn, membro):
>         livro = self._acervo[isbn]
>         membro.emprestimos.remove(livro)
>         livro.disponivel = True
>         self._notificar("devolucao", livro, membro)
>
>
> def log(evento, livro, membro):
>     print(f"[{evento}] {livro.titulo!r} ↔ {membro.nome}")
>
> bib = Biblioteca()
> bib.observar(log)
> bib.adicionar(Livro("Dom Casmurro", "Machado de Assis", "111"))
> bib.adicionar(Livro("O Cortiço", "Aluísio Azevedo", "222"))
>
> ada = Membro("Ada")
> bib.emprestar("111", ada)
> try:
>     bib.emprestar("111", Membro("Alan"))
> except LivroIndisponivel as e:
>     print("Indisponível:", e)
> bib.devolver("111", ada)
> ```
> Exceções próprias serão aprofundadas em [[05 - Tratamento de Erros e Arquivos/02 - Exceções Personalizadas|Exceções Personalizadas]].

---

## 🧪 Quiz relâmpago

> [!question] Responda sem rodar o código
> 1. Qual a diferença entre `@classmethod` e `@staticmethod`?
> 2. O que `super().__init__()` faz? O que acontece se esquecer?
> 3. Qual a diferença entre `__str__` e `__repr__`?
> 4. Por que `class A: itens = []` é perigoso?
> 5. O que `@dataclass(frozen=True)` altera?
> 6. Em `class D(B, C)`, quem o Python procura primeiro: `B` ou `C`? Como inspecionar?
> 7. Para que serve `__slots__`? Qual o custo?
> 8. Quando preferir **composição** à herança?
> 9. O que é *duck typing*?
> 10. Por que definir `__eq__` sem `__hash__` torna o objeto "unhashable"?

> [!success]- Respostas
> 1. `@classmethod` recebe `cls` (classe); `@staticmethod` não recebe nada (função agrupada na classe).
> 2. Chama o inicializador da classe mãe; esquecer deixa os atributos da mãe sem existir (`AttributeError`).
> 3. `__str__` é para o usuário final; `__repr__` é para o desenvolvedor (inequívoco, aparece no REPL/listas).
> 4. A lista é de **classe**, compartilhada por todas as instâncias.
> 5. Torna os campos somente leitura (`FrozenInstanceError`) e gera `__hash__` (objeto hasheável).
> 6. `B` primeiro (esquerda → direita); veja `D.__mro__`.
> 7. Reduz memória e impede atributos extras; custo: sem `__dict__` dinâmico, atenção com herança.
> 8. Quando a relação é "tem um", quando quer flexibilidade/baixo acoplamento ou quando a herança expõe métodos que não fazem sentido.
> 9. Tratar um objeto pelo que ele **faz** (métodos que possui), não pelo seu tipo/herança.
> 10. O Python define `__hash__ = None` ao ver `__eq__` customizado, evitando hashes inconsistentes com a igualdade.

---

## ✅ Checklist do módulo

- [ ] Crio classes com `__init__`, atributos e métodos corretamente (`self`)
- [ ] Diferencio atributos de **instância** e de **classe**
- [ ] Uso `@classmethod` (fábricas) e `@staticmethod` (utilitários)
- [ ] Aplico **herança**, `super()` e **polimorfismo** (e prefiro **composição** quando cabe)
- [ ] Uso classes abstratas (`ABC`) e *duck typing*
- [ ] Encapsulo com `_x` e `@property` (validação e atributos calculados)
- [ ] Implemento métodos mágicos úteis (`__repr__`, `__eq__`, `__lt__`, `__add__`, `__len__`, `__iter__`...)
- [ ] Uso `@dataclass` (`frozen`, `order`, `slots`, `field`, `__post_init__`)
- [ ] Reconheço Factory, Strategy, Observer, Decorator e Singleton
- [ ] Resolvi pelo menos 10 dos exercícios acima

---

## 🚀 Próximo módulo
➡️ [[05 - Tratamento de Erros e Arquivos/01 - try except else finally|Módulo 05: Tratamento de Erros e Arquivos]]

⬅️ [[04 - Programação Orientada a Objetos/06 - Design Patterns Básicos|Design Patterns Básicos]] · ⬆️ [[00 - Índice Python|Índice]]

#python #intermediario #exercicios #pratica #poo #dataclasses #design-patterns
