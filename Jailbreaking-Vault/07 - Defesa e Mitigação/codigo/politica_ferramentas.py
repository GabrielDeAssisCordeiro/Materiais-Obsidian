"""Política de ferramentas para agentes, decidida por CÓDIGO e não pelo modelo.

Biblioteca padrão apenas. Material didático do curso: não é uma biblioteca de produção.

Ideias implementadas:
  * negar por padrão: ferramenta desconhecida não executa;
  * classificação por efeito (leitura, escrita local, externo);
  * proveniência: depois que conteúdo NÃO CONFIÁVEL entra na sessão, ações com efeito externo
    ficam restritas (negar, ou pedir confirmação que mostra a AÇÃO REAL e os parâmetros);
  * listas de permissão para destinatários e limite de chamadas por sessão;
  * log de cada decisão, para auditoria e monitoramento.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from enum import Enum


class Efeito(Enum):
    LEITURA = "leitura"
    ESCRITA_LOCAL = "escrita_local"
    EXTERNO = "externo"          # sai do sistema: e-mail, requisição de rede, publicação


class Veredito(Enum):
    PERMITIR = "permitir"
    NEGAR = "negar"
    CONFIRMAR = "confirmar"      # exige aprovação humana vendo a ação real


@dataclass(frozen=True)
class Ferramenta:
    nome: str
    efeito: Efeito
    # parâmetros cujo valor só pode vir de uma lista de permissão (ex.: destinatários)
    restringir: dict[str, frozenset[str]] = field(default_factory=dict)
    max_chamadas: int = 10


@dataclass
class Sessao:
    """Estado de uma sessão: o que entrou no contexto e o que já foi chamado."""
    origens_nao_confiaveis: list[str] = field(default_factory=list)
    chamadas: dict[str, int] = field(default_factory=dict)
    log: list[dict] = field(default_factory=list)

    @property
    def contaminada(self) -> bool:
        return bool(self.origens_nao_confiaveis)

    def registrar_entrada(self, origem: str, confiavel: bool) -> None:
        if not confiavel:
            self.origens_nao_confiaveis.append(origem)


class Politica:
    def __init__(self, ferramentas: list[Ferramenta], apos_contaminacao: Veredito = Veredito.CONFIRMAR):
        if apos_contaminacao is Veredito.PERMITIR:
            raise ValueError("a política pós-contaminação precisa ser NEGAR ou CONFIRMAR")
        self.ferramentas = {f.nome: f for f in ferramentas}
        self.apos_contaminacao = apos_contaminacao

    def decidir(self, sessao: Sessao, nome: str, args: dict) -> tuple[Veredito, str]:
        v, motivo = self._avaliar(sessao, nome, args)
        sessao.log.append({
            "t": time.time(), "ferramenta": nome, "args": args, "veredito": v.value,
            "motivo": motivo, "contaminada": sessao.contaminada,
            "origens_nao_confiaveis": list(sessao.origens_nao_confiaveis),
        })
        if v is Veredito.PERMITIR:
            sessao.chamadas[nome] = sessao.chamadas.get(nome, 0) + 1
        return v, motivo

    def _avaliar(self, sessao: Sessao, nome: str, args: dict) -> tuple[Veredito, str]:
        f = self.ferramentas.get(nome)
        if f is None:
            return Veredito.NEGAR, "ferramenta desconhecida (negar por padrão)"
        if sessao.chamadas.get(nome, 0) >= f.max_chamadas:
            return Veredito.NEGAR, "limite de chamadas da sessão atingido"
        for param, permitidos in f.restringir.items():
            if args.get(param) not in permitidos:
                return Veredito.NEGAR, f"parâmetro '{param}' fora da lista de permissão"
        if f.efeito is Efeito.EXTERNO and sessao.contaminada:
            return self.apos_contaminacao, "efeito externo após conteúdo não confiável na sessão"
        if f.efeito is Efeito.ESCRITA_LOCAL and sessao.contaminada:
            return Veredito.CONFIRMAR, "escrita após conteúdo não confiável (possível persistência)"
        return Veredito.PERMITIR, "dentro da política"


def texto_de_confirmacao(nome: str, args: dict, origens: list[str]) -> str:
    """O texto que o humano vê. Mostra a AÇÃO REAL e os parâmetros exatos, nunca um resumo do modelo.

    Resumos escritos pelo modelo podem ser enganosos: se o contexto foi manipulado, o resumo também.
    """
    linhas = [f"Ação solicitada: {nome}", "Parâmetros exatos:", json.dumps(args, ensure_ascii=False, indent=2)]
    if origens:
        linhas.append("Conteúdo não confiável presente na sessão: " + "; ".join(origens))
    return "\n".join(linhas)
