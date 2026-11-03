---
titulo: "Projeto 02 – Solução: To-Do com Arquivos"
tags: [python, projeto, solucao, arquivos, json, argparse]
nivel: iniciante
criado: 2026-10-14
projeto: 2
---

# ✅ Projeto 02 – Solução: To-Do com Arquivos

Enunciado: [[09 - Projetos Práticos/Projeto 02 - To-Do com Arquivos|Projeto 02]].

## 💻 Código completo

```python
# arquivo: todo.py
"""Gerenciador de tarefas em linha de comando com persistência em JSON."""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

PRIORIDADES = {"alta": 0, "media": 1, "baixa": 2}  # menor = mais importante


def caminho_padrao() -> Path:
    return Path(os.environ.get("TODO_ARQUIVO", Path.home() / ".todo.json"))


@dataclass
class Tarefa:
    id: int
    titulo: str
    prioridade: str = "media"
    feita: bool = False
    criada_em: str = ""


class Repositorio:
    """Cuida apenas de ler/gravar o arquivo."""

    def __init__(self, caminho: Path):
        self.caminho = caminho

    def carregar(self) -> list[Tarefa]:
        if not self.caminho.exists():
            return []
        try:
            bruto = json.loads(self.caminho.read_text(encoding="utf-8"))
            return [Tarefa(**item) for item in bruto]
        except (json.JSONDecodeError, TypeError, OSError) as erro:
            backup = self.caminho.with_suffix(".bak")
            os.replace(self.caminho, backup)
            print(f"Aviso: arquivo corrompido ({erro}). Backup em {backup}.", file=sys.stderr)
            return []

    def salvar(self, tarefas: list[Tarefa]) -> None:
        tmp = self.caminho.with_suffix(".tmp")
        tmp.write_text(
            json.dumps([asdict(t) for t in tarefas], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        os.replace(tmp, self.caminho)  # troca atômica


class TarefaNaoEncontrada(Exception):
    pass


class Servico:
    """Regras de negócio."""

    def __init__(self, repo: Repositorio):
        self.repo = repo

    def adicionar(self, titulo: str, prioridade: str = "media") -> Tarefa:
        tarefas = self.repo.carregar()
        novo_id = max((t.id for t in tarefas), default=0) + 1
        tarefa = Tarefa(
            id=novo_id,
            titulo=titulo.strip(),
            prioridade=prioridade,
            criada_em=datetime.now().isoformat(timespec="seconds"),
        )
        tarefas.append(tarefa)
        self.repo.salvar(tarefas)
        return tarefa

    def _achar(self, tarefas: list[Tarefa], id_: int) -> Tarefa:
        for t in tarefas:
            if t.id == id_:
                return t
        raise TarefaNaoEncontrada(f"tarefa {id_} não existe")

    def concluir(self, id_: int) -> Tarefa:
        tarefas = self.repo.carregar()
        t = self._achar(tarefas, id_)
        t.feita = True
        self.repo.salvar(tarefas)
        return t

    def remover(self, id_: int) -> None:
        tarefas = self.repo.carregar()
        t = self._achar(tarefas, id_)
        tarefas.remove(t)
        self.repo.salvar(tarefas)

    def listar(self, so_pendentes: bool = False) -> list[Tarefa]:
        tarefas = self.repo.carregar()
        if so_pendentes:
            tarefas = [t for t in tarefas if not t.feita]
        return sorted(tarefas, key=lambda t: (t.feita, PRIORIDADES[t.prioridade], t.id))


def montar_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="todo", description="Gerenciador de tarefas")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="adiciona tarefa")
    a.add_argument("titulo")
    a.add_argument("-p", "--prioridade", choices=PRIORIDADES, default="media")

    l = sub.add_parser("list", help="lista tarefas")
    l.add_argument("--pendentes", action="store_true")

    d = sub.add_parser("done", help="conclui tarefa")
    d.add_argument("id", type=int)

    r = sub.add_parser("rm", help="remove tarefa")
    r.add_argument("id", type=int)
    return p


def main(argv: list[str] | None = None) -> int:
    args = montar_parser().parse_args(argv)
    servico = Servico(Repositorio(caminho_padrao()))
    try:
        match args.cmd:
            case "add":
                t = servico.adicionar(args.titulo, args.prioridade)
                print(f"Criada #{t.id}: {t.titulo}")
            case "list":
                tarefas = servico.listar(args.pendentes)
                if not tarefas:
                    print("Nenhuma tarefa.")
                for t in tarefas:
                    marca = "x" if t.feita else " "
                    print(f"[{marca}] {t.id:>3} ({t.prioridade:<5}) {t.titulo}")
            case "done":
                print(f"Concluída: {servico.concluir(args.id).titulo}")
            case "rm":
                servico.remover(args.id)
                print(f"Removida #{args.id}")
    except TarefaNaoEncontrada as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 🔍 Pontos importantes

- **Três camadas** (`Repositorio` → `Servico` → CLI): trocar JSON por SQLite mexe só no repositório.
- **`os.replace`** é atômico no mesmo volume: ou o arquivo antigo, ou o novo — nunca meio-termo.
- **`dataclass`**: `asdict` serializa, `Tarefa(**item)` desserializa.
- **`choices=PRIORIDADES`** faz o argparse validar a prioridade e gerar a ajuda.
- Teste isolado usando `TODO_ARQUIVO=/tmp/teste.json python todo.py list`.

## 🧪 Teste com pytest

```python
# arquivo: test_todo.py
from todo import Repositorio, Servico, TarefaNaoEncontrada
import pytest


def test_fluxo(tmp_path):
    s = Servico(Repositorio(tmp_path / "t.json"))
    t = s.adicionar("estudar", "alta")
    assert t.id == 1
    s.concluir(1)
    assert s.listar(so_pendentes=True) == []
    s.remover(1)
    with pytest.raises(TarefaNaoEncontrada):
        s.remover(1)


def test_arquivo_corrompido(tmp_path):
    arq = tmp_path / "t.json"
    arq.write_text("{lixo")
    assert Servico(Repositorio(arq)).listar() == []
    assert arq.with_suffix(".bak").exists()
```

---

⬅️ [[09 - Projetos Práticos/Projeto 02 - To-Do com Arquivos|Projeto 02]] | ➡️ [[09 - Projetos Práticos/Projeto 03 - Análise de Dados com CSV|Projeto 03]]

#python #projeto #solucao #arquivos #json #argparse
