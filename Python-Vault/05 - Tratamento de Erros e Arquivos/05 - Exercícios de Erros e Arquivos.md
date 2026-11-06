---
titulo: "Exercícios de Tratamento de Erros e Arquivos"
tags: [python, intermediario, exercicios, pratica, excecoes, arquivos]
nivel: intermediario
criado: 2026-10-05
modulo: "05 - Tratamento de Erros e Arquivos"
---

# 🏋️ Exercícios de Tratamento de Erros e Arquivos

Exercícios **progressivos** para fixar o **Módulo 05**. Resolva sozinho(a) antes de abrir cada solução.

> [!tip] Como praticar
> 1. Crie uma pasta `m05/` para os exercícios e use `pathlib` para os caminhos.
> 2. **Provoque** os erros de propósito (arquivo inexistente, JSON quebrado, entrada inválida) e confirme que seu código reage bem.
> 3. Use sempre `with` e `encoding="utf-8"`.
> 4. Rode no **debugger** com *Raised Exceptions* ativado para ver onde cada erro nasce.

**Revise antes:** [[05 - Tratamento de Erros e Arquivos/01 - try except else finally|try/except]] · [[05 - Tratamento de Erros e Arquivos/02 - Exceções Personalizadas|Exceções Personalizadas]] · [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|Arquivos]] · [[05 - Tratamento de Erros e Arquivos/04 - Context Managers com with|Context Managers]]

---

## 🟢 Nível 1: Exceções básicas

> [!question] 1. Calculadora segura
> Peça dois números e uma operação (`+ - * /`). Trate `ValueError` (número inválido), `ZeroDivisionError` e operação desconhecida. O programa deve **repetir** até o usuário acertar.

> [!success]- Solução
> ```python
> OPERACOES = {
>     "+": lambda a, b: a + b,
>     "-": lambda a, b: a - b,
>     "*": lambda a, b: a * b,
>     "/": lambda a, b: a / b,
> }
>
> while True:
>     try:
>         a = float(input("A: ").replace(",", "."))
>         b = float(input("B: ").replace(",", "."))
>         op = input("Operação (+ - * /): ").strip()
>         if op not in OPERACOES:
>             raise KeyError(op)
>         print(f"Resultado: {OPERACOES[op](a, b)}")
>         break
>     except ValueError:
>         print("❌ Digite números válidos.")
>     except ZeroDivisionError:
>         print("❌ Não é possível dividir por zero.")
>     except KeyError as e:
>         print(f"❌ Operação desconhecida: {e}")
> ```

> [!question] 2. `ler_inteiro`
> Escreva `ler_inteiro(mensagem, minimo=None, maximo=None)` que repete até receber um inteiro válido dentro dos limites.

> [!success]- Solução
> ```python
> def ler_inteiro(mensagem, minimo=None, maximo=None):
>     while True:
>         try:
>             n = int(input(mensagem))
>         except ValueError:
>             print("Digite um número inteiro.")
>             continue
>         if minimo is not None and n < minimo:
>             print(f"Mínimo: {minimo}")
>         elif maximo is not None and n > maximo:
>             print(f"Máximo: {maximo}")
>         else:
>             return n
> ```

> [!question] 3. Acesso seguro
> Escreva `acessar(estrutura, *caminho, padrao=None)` que percorra dicts/listas aninhados e devolva `padrao` se qualquer passo falhar (`KeyError`, `IndexError`, `TypeError`).
> ```python
> dados = {"usuarios": [{"nome": "Ada", "emails": ["a@x.com"]}]}
> acessar(dados, "usuarios", 0, "emails", 0)      # 'a@x.com'
> acessar(dados, "usuarios", 5, "nome")           # None
> ```

> [!success]- Solução
> ```python
> def acessar(estrutura, *caminho, padrao=None):
>     atual = estrutura
>     try:
>         for passo in caminho:
>             atual = atual[passo]
>     except (KeyError, IndexError, TypeError):
>         return padrao
>     return atual
> ```

---

## 🟡 Nível 2: `finally`, `raise` e exceções próprias

> [!question] 4. Descubra a saída
> Sem rodar, diga o que cada chamada imprime/retorna:
> ```python
> def f(x):
>     try:
>         if x == 0:
>             raise ValueError("zero")
>         return "ok"
>     except ValueError:
>         return "erro"
>     else:
>         print("else")
>     finally:
>         print("finally")
>
> print(f(0))
> print(f(1))
> ```

> [!success]- Solução
> ```text
> finally
> erro
> finally
> ok
> ```
> O `finally` roda **antes** do `return` ser efetivado. O `else` **nunca** roda aqui: em `f(1)` o `try` termina com `return`, e o `else` só executa se o `try` terminar *sem* `return`/exceção.

> [!question] 5. Exceções de domínio
> Crie `SaldoInsuficienteError` (com `saldo`, `valor`, `faltam`) e `ValorInvalidoError(ValueError)`. Implemente `sacar(saldo, valor)` e trate os dois casos de formas diferentes.

> [!success]- Solução
> ```python
> class ContaError(Exception):
>     """Base dos erros de conta."""
>
> class ValorInvalidoError(ContaError, ValueError):
>     pass
>
> class SaldoInsuficienteError(ContaError):
>     def __init__(self, saldo, valor):
>         self.saldo, self.valor = saldo, valor
>         self.faltam = valor - saldo
>         super().__init__(f"Faltam R$ {self.faltam:.2f} (saldo R$ {saldo:.2f})")
>
> def sacar(saldo, valor):
>     if valor <= 0:
>         raise ValorInvalidoError(f"Valor inválido: {valor}")
>     if valor > saldo:
>         raise SaldoInsuficienteError(saldo, valor)
>     return saldo - valor
>
> for valor in (50, -5, 500):
>     try:
>         print("Novo saldo:", sacar(100, valor))
>     except SaldoInsuficienteError as e:
>         print(f"💸 {e}")
>     except ValorInvalidoError as e:
>         print(f"⚠️  {e}")
> ```

> [!question] 6. Tradução de erros (`raise ... from`)
> Escreva `carregar_usuario(texto_json)` que levante `UsuarioInvalidoError` (com a causa encadeada) se o JSON for inválido **ou** se faltar a chave `"nome"`.

> [!success]- Solução
> ```python
> import json
>
> class UsuarioInvalidoError(Exception):
>     pass
>
> def carregar_usuario(texto_json):
>     try:
>         dados = json.loads(texto_json)
>     except json.JSONDecodeError as e:
>         raise UsuarioInvalidoError("JSON malformado") from e
>     try:
>         return dados["nome"]
>     except (KeyError, TypeError) as e:
>         raise UsuarioInvalidoError("Campo 'nome' ausente") from e
> ```

> [!question] 7. Tentar novamente
> Escreva um decorator `tentar(vezes=3, espera=0.5, excecoes=(ConnectionError,))` que repita a função em caso de falha e relance o último erro. Teste com uma função que falha aleatoriamente.

> [!success]- Solução
> ```python
> import functools, random, time
>
> def tentar(vezes=3, espera=0.5, excecoes=(ConnectionError,)):
>     def decorador(func):
>         @functools.wraps(func)
>         def wrapper(*args, **kwargs):
>             for tentativa in range(1, vezes + 1):
>                 try:
>                     return func(*args, **kwargs)
>                 except excecoes as e:
>                     print(f"Tentativa {tentativa}/{vezes} falhou: {e}")
>                     if tentativa == vezes:
>                         raise
>                     time.sleep(espera)
>         return wrapper
>     return decorador
>
> @tentar(vezes=4, espera=0.1)
> def instavel():
>     if random.random() < 0.7:
>         raise ConnectionError("rede caiu")
>     return "ok"
>
> print(instavel())
> ```
> Decorators com parâmetros em [[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]].

---

## 🟠 Nível 3: Arquivos de texto, CSV e JSON

> [!question] 8. Contador de palavras
> Leia um arquivo de texto e mostre as **10 palavras mais frequentes** (ignorando maiúsculas e pontuação). Trate o arquivo inexistente.

> [!success]- Solução
> ```python
> import re
> from collections import Counter
> from pathlib import Path
>
> def top_palavras(caminho, n=10):
>     try:
>         texto = Path(caminho).read_text(encoding="utf-8").lower()
>     except FileNotFoundError:
>         print(f"Arquivo não encontrado: {caminho}")
>         return []
>     palavras = re.findall(r"\w+", texto)
>     return Counter(palavras).most_common(n)
>
> for palavra, qtd in top_palavras("texto.txt"):
>     print(f"{palavra:<15} {qtd}")
> ```

> [!question] 9. Relatório de vendas (CSV → CSV)
> Dado `vendas.csv` (`produto,quantidade,preco`), gere `resumo.csv` com `produto,faturamento` ordenado do maior para o menor. **Ignore** linhas inválidas (preço/quantidade não numéricos) e mostre quantas foram ignoradas.

> [!success]- Solução
> ```python
> import csv
>
> faturamento, ignoradas = {}, 0
>
> with open("vendas.csv", newline="", encoding="utf-8") as f:
>     for numero, linha in enumerate(csv.DictReader(f), start=2):
>         try:
>             total = int(linha["quantidade"]) * float(linha["preco"])
>         except (ValueError, KeyError, TypeError):
>             ignoradas += 1
>             print(f"Linha {numero} ignorada: {linha}")
>             continue
>         produto = linha["produto"]
>         faturamento[produto] = faturamento.get(produto, 0) + total
>
> with open("resumo.csv", "w", newline="", encoding="utf-8") as f:
>     w = csv.writer(f)
>     w.writerow(["produto", "faturamento"])
>     for produto, total in sorted(faturamento.items(), key=lambda p: p[1], reverse=True):
>         w.writerow([produto, f"{total:.2f}"])
>
> print(f"{ignoradas} linha(s) ignorada(s)")
> ```

> [!question] 10. Configuração com padrões
> Crie `Config` que leia `config.json`, aplique valores padrão para chaves ausentes, e **salve** o arquivo se ele não existir. Se o JSON estiver corrompido, faça **backup** (`config.json.bak`) e recrie com os padrões.

> [!success]- Solução
> ```python
> import json
> from pathlib import Path
>
> PADRAO = {"tema": "claro", "idioma": "pt-BR", "tamanho_fonte": 14}
>
> def carregar_config(caminho="config.json"):
>     caminho = Path(caminho)
>     try:
>         dados = json.loads(caminho.read_text(encoding="utf-8"))
>     except FileNotFoundError:
>         dados = {}
>     except json.JSONDecodeError:
>         caminho.rename(caminho.with_suffix(".json.bak"))
>         print("⚠️  Config corrompida; backup criado.")
>         dados = {}
>     config = {**PADRAO, **dados}
>     caminho.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
>     return config
> ```

> [!question] 11. Agenda persistente com validação
> Evolua a agenda do material: salvar em `agenda.json` de forma **atômica** (arquivo temporário + `os.replace`), validar telefone (somente dígitos, 10 ou 11) com uma exceção `TelefoneInvalidoError`, e permitir **remover** contatos.

> [!success]- Solução
> ```python
> import json, os, re
> from pathlib import Path
>
> ARQUIVO = Path("agenda.json")
>
> class TelefoneInvalidoError(ValueError):
>     pass
>
> def validar_telefone(texto):
>     digitos = re.sub(r"\D", "", texto)
>     if len(digitos) not in (10, 11):
>         raise TelefoneInvalidoError(f"Telefone inválido: {texto!r}")
>     return digitos
>
> def carregar():
>     try:
>         return json.loads(ARQUIVO.read_text(encoding="utf-8"))
>     except (FileNotFoundError, json.JSONDecodeError):
>         return {}
>
> def salvar(agenda):
>     tmp = ARQUIVO.with_suffix(".tmp")
>     tmp.write_text(json.dumps(agenda, ensure_ascii=False, indent=2), encoding="utf-8")
>     os.replace(tmp, ARQUIVO)
>
> def adicionar(agenda, nome, telefone):
>     agenda[nome.strip().title()] = validar_telefone(telefone)
>     salvar(agenda)
>
> def remover(agenda, nome):
>     try:
>         del agenda[nome.strip().title()]
>     except KeyError:
>         raise KeyError(f"Contato {nome!r} não existe") from None
>     salvar(agenda)
> ```

---

## 🔴 Nível 4: Context managers e desafios

> [!question] 12. Context managers
> Crie: (a) `Cronometro` (classe) com `duracao`; (b) `ocultar_prints()` com `@contextmanager`; (c) `arquivo_temporario(conteudo)` que cria um arquivo com o conteúdo, entrega o `Path` e **apaga** ao sair, mesmo com erro.

> [!success]- Solução
> ```python
> import io, os, tempfile, time
> from contextlib import contextmanager, redirect_stdout
> from pathlib import Path
>
> # (a)
> class Cronometro:
>     def __enter__(self):
>         self.inicio = time.perf_counter()
>         return self
>     def __exit__(self, *exc):
>         self.duracao = time.perf_counter() - self.inicio
>         return False
>
> # (b)
> @contextmanager
> def ocultar_prints():
>     with redirect_stdout(io.StringIO()):
>         yield
>
> # (c)
> @contextmanager
> def arquivo_temporario(conteudo, sufixo=".txt"):
>     fd, nome = tempfile.mkstemp(suffix=sufixo)
>     caminho = Path(nome)
>     try:
>         with os.fdopen(fd, "w", encoding="utf-8") as f:
>             f.write(conteudo)
>         yield caminho
>     finally:
>         caminho.unlink(missing_ok=True)
>
> with arquivo_temporario("olá") as p:
>     print(p.read_text(encoding="utf-8"))
> print(p.exists())   # False
> ```

> [!question] 13. Descubra os bugs
> ```python
> # (a)
> try:
>     valor = int(input("N: "))
> except:
>     pass
> print(valor * 2)
>
> # (b)
> f = open("dados.txt", "w")
> f.write(42)
> f.close()
>
> # (c)
> with open("a.csv") as f:
>     for linha in f.read().split(","):
>         ...
>
> # (d)
> def ler(caminho):
>     try:
>         return open(caminho).read()
>     except FileNotFoundError:
>         return None
>     finally:
>         return ""
>
> # (e)
> try:
>     ...
> except Exception:
>     ...
> except ValueError:
>     ...
>
> # (f)
> import json
> json.dumps({"hoje": __import__("datetime").date.today()})
> ```

> [!success]- Solução
> ```python
> # (a) `except:` engole tudo e `valor` pode não existir → NameError.
> #     Capture ValueError e repita/trate; só use `valor` no caminho de sucesso.
>
> # (b) write() só aceita str, e o arquivo pode ficar aberto se falhar.
> with open("dados.txt", "w", encoding="utf-8") as f:
>     f.write(str(42))
>
> # (c) falta encoding/newline; e split(",") não trata aspas/vírgulas internas.
> import csv
> with open("a.csv", newline="", encoding="utf-8") as f:
>     for linha in csv.reader(f):
>         ...
>
> # (d) `return` no finally sobrescreve o retorno e engole exceções.
> #     Remova o finally (e use `with` para fechar o arquivo).
> def ler(caminho):
>     try:
>         with open(caminho, encoding="utf-8") as f:
>             return f.read()
>     except FileNotFoundError:
>         return None
>
> # (e) `except Exception` vem antes de `except ValueError`: o segundo nunca roda.
> #     Ordene do mais específico ao mais geral.
>
> # (f) date não é serializável: json.dumps(..., default=str).
> ```

> [!question] 14. Mini-projeto: Processador de logs resiliente
> Crie um programa que processe um arquivo de log (`app.log`) com linhas no formato:
> ```text
> 2026-10-05 14:03:21 | ERROR | pagamentos | Cartão recusado
> 2026-10-05 14:03:22 | INFO | auth | Login ok
> linha quebrada sem formato
> ```
> Requisitos:
> - Lê **linha a linha** (arquivo pode ser gigante)
> - Linhas inválidas **não derrubam** o programa: conte-as e guarde-as em `invalidas.txt`
> - Define `LogInvalidoError` e a usa internamente com `raise ... from`
> - Gera `relatorio.json` com: total por nível, total por módulo e os 5 erros mais recentes
> - Salva o relatório de forma **atômica**
> - Trata arquivo inexistente e sem permissão com mensagens claras
> - Use `@contextmanager` para cronometrar o processamento

> [!success]- Solução (completa)
> ```python
> import json
> import os
> import time
> from collections import Counter
> from contextlib import contextmanager
> from datetime import datetime
> from pathlib import Path
>
>
> class LogInvalidoError(ValueError):
>     """Linha de log fora do formato esperado."""
>
>
> @contextmanager
> def cronometrar(nome):
>     inicio = time.perf_counter()
>     try:
>         yield
>     finally:
>         print(f"⏱  {nome}: {time.perf_counter() - inicio:.3f}s")
>
>
> def analisar_linha(linha):
>     partes = [p.strip() for p in linha.split("|")]
>     if len(partes) != 4:
>         raise LogInvalidoError(f"Esperava 4 campos, veio {len(partes)}")
>     data_txt, nivel, modulo, mensagem = partes
>     try:
>         data = datetime.strptime(data_txt, "%Y-%m-%d %H:%M:%S")
>     except ValueError as e:
>         raise LogInvalidoError(f"Data inválida: {data_txt!r}") from e
>     return {"data": data, "nivel": nivel.upper(), "modulo": modulo, "mensagem": mensagem}
>
>
> def salvar_json_atomico(caminho, dados):
>     caminho = Path(caminho)
>     tmp = caminho.with_suffix(".tmp")
>     tmp.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
>     os.replace(tmp, caminho)
>
>
> def processar(caminho_log):
>     por_nivel, por_modulo = Counter(), Counter()
>     erros, invalidas = [], 0
>
>     with open(caminho_log, encoding="utf-8") as log, \
>          open("invalidas.txt", "w", encoding="utf-8") as ruins:
>         for numero, linha in enumerate(log, start=1):
>             linha = linha.rstrip("\n")
>             if not linha.strip():
>                 continue
>             try:
>                 registro = analisar_linha(linha)
>             except LogInvalidoError as e:
>                 invalidas += 1
>                 ruins.write(f"{numero}: {linha}  # {e}\n")
>                 continue
>             por_nivel[registro["nivel"]] += 1
>             por_modulo[registro["modulo"]] += 1
>             if registro["nivel"] == "ERROR":
>                 erros.append(registro)
>
>     erros.sort(key=lambda r: r["data"], reverse=True)
>     return {
>         "por_nivel": dict(por_nivel),
>         "por_modulo": dict(por_modulo),
>         "linhas_invalidas": invalidas,
>         "ultimos_erros": [
>             {"data": r["data"].isoformat(sep=" "), "modulo": r["modulo"],
>              "mensagem": r["mensagem"]} for r in erros[:5]
>         ],
>     }
>
>
> def main():
>     try:
>         with cronometrar("processamento"):
>             relatorio = processar("app.log")
>     except FileNotFoundError:
>         print("❌ app.log não encontrado.")
>         return
>     except PermissionError:
>         print("❌ Sem permissão para ler app.log.")
>         return
>     salvar_json_atomico("relatorio.json", relatorio)
>     print("✅ relatorio.json gerado")
>
>
> if __name__ == "__main__":
>     main()
> ```

---

## 🧪 Quiz relâmpago

> [!question] Responda sem rodar o código
> 1. Quando o bloco `else` de um `try` executa?
> 2. O `finally` roda se houver `return` dentro do `try`?
> 3. Por que `except:` (sem tipo) é desencorajado?
> 4. Qual a diferença entre `raise` e `raise e` dentro de um `except`?
> 5. O que `raise X from None` faz?
> 6. Qual modo de `open` **apaga** o conteúdo existente? E qual **falha** se o arquivo existir?
> 7. Por que usar `newline=""` com o módulo `csv`?
> 8. O que `json.dumps({1: "a"})` produz?
> 9. O que é EAFP?
> 10. O que acontece se `__exit__` retornar `True`?

> [!success]- Respostas
> 1. Quando o `try` termina **sem** exceção.
> 2. Sim, sempre (antes de devolver o valor).
> 3. Captura até `KeyboardInterrupt`/`SystemExit` e esconde bugs silenciosamente.
> 4. `raise` relança preservando o traceback original; `raise e` também funciona, mas adiciona o ponto do relançamento ao traceback (prefira `raise`).
> 5. Suprime o encadeamento da causa original no traceback.
> 6. `"w"` apaga; `"x"` falha com `FileExistsError`.
> 7. Para o `csv` controlar as quebras de linha (evita linhas em branco extras e problemas com campos multilinha).
> 8. `'{"1": "a"}'`: chaves viram strings.
> 9. *Easier to Ask Forgiveness than Permission*: tentar e tratar a exceção, em vez de verificar antes.
> 10. A exceção é **suprimida** (o programa continua após o `with`).

---

## ✅ Checklist do módulo

- [ ] Uso `try/except/else/finally` e sei a função de cada bloco
- [ ] Capturo exceções **específicas** (ordem do mais específico ao mais geral)
- [ ] Sei levantar (`raise`), relançar e encadear (`from`) exceções
- [ ] Crio **exceções personalizadas** e hierarquias de domínio
- [ ] Leio e escrevo arquivos com `with`, `encoding` e `pathlib`
- [ ] Manipulo **CSV** (`DictReader`/`DictWriter`, `newline=""`) e **JSON** (`load`/`dump`/`loads`/`dumps`)
- [ ] Faço escrita **atômica** para dados importantes
- [ ] Crio context managers (classe e `@contextmanager`) e conheço `contextlib`
- [ ] Resolvi pelo menos 10 dos exercícios acima

---

## 🚀 Próximo módulo
➡️ [[06 - Módulos da Biblioteca Padrão Essenciais/01 - os pathlib e sys|Módulo 06: Biblioteca Padrão Essencial]]

⬅️ [[05 - Tratamento de Erros e Arquivos/04 - Context Managers com with|Context Managers]] · ⬆️ [[Índice - Python|Índice]]

#python #intermediario #exercicios #pratica #excecoes #arquivos #csv #json #context-managers
