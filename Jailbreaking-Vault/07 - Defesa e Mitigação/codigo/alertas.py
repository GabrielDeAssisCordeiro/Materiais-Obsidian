"""Regras simples de alerta sobre logs de decisões (formato de politica_ferramentas.Sessao.log).

Biblioteca padrão apenas. Material didático do curso. São SINAIS para investigação,
não provas: toda regra tem falsos positivos e falsos negativos.
"""
from __future__ import annotations

from collections import Counter


def regra_leitura_externa_seguida_de_acao(log: list[dict]) -> list[str]:
    """Sessão contaminada pediu ferramenta de efeito logo depois: padrão típico de injeção indireta."""
    return [
        f"{e['ferramenta']} pedida com conteúdo não confiável na sessão ({e['veredito']})"
        for e in log
        if e["contaminada"] and e["veredito"] in ("negar", "confirmar")
        and e["motivo"].startswith(("efeito externo", "escrita"))
    ]


def regra_muitas_negativas(log: list[dict], limite: int = 3) -> list[str]:
    """Muitas negativas na mesma sessão: alguém (ou algo) está tentando repetidamente."""
    negadas = sum(e["veredito"] == "negar" for e in log)
    return [f"{negadas} chamadas negadas na sessão (limite {limite})"] if negadas >= limite else []


def regra_canario_em_saida(saida: str, canarios: list[str], normalizar) -> list[str]:
    """Um canário plantado (em prompt, documento ou base RAG) apareceu numa saída ou numa chamada."""
    alvo = normalizar(saida)
    return [f"canário detectado: {c}" for c in canarios if normalizar(c) in alvo]


def resumo(log: list[dict]) -> dict:
    return dict(Counter(e["veredito"] for e in log))
