"""Ferramentas SIMULADAS e camada de política. Nenhuma ação real acontece aqui."""

import re

# Ferramentas com efeito (em produção seriam reais); "resumir" é somente leitura.
COM_EFEITO = {"criar_evento", "enviar_email", "salvar_nota"}

_TOOL_RE = re.compile(r"^\s*TOOL:\s*([a-z_]+)\((.*)\)\s*$", re.MULTILINE)


def extrair_chamadas(texto: str) -> list[dict]:
    """Extrai linhas no formato 'TOOL: nome(args)' da saída do modelo."""
    return [{"nome": m.group(1), "args": m.group(2)} for m in _TOOL_RE.finditer(texto)]


def decidir(chamada: dict, ha_conteudo_externo: bool, intencao_do_usuario: list[str],
            modo: str | None):
    """Decide se uma chamada é executada.

    modo None: executa tudo. 'negar': nega ferramentas com efeito quando houve conteúdo
    externo no turno. 'confirmar': idem, mas simula um humano que vê a ação e os parâmetros
    reais e aprova só o que o próprio usuário pediu (intencao_do_usuario).
    Retorna (executar: bool, motivo: str).
    """
    nome = chamada["nome"]
    if modo is None or nome not in COM_EFEITO or not ha_conteudo_externo:
        return True, "permitida"
    if modo == "negar":
        return False, "negada: ferramenta com efeito após conteúdo externo"
    if modo == "confirmar":
        if nome in intencao_do_usuario:
            return True, "confirmada pelo usuário"
        return False, "recusada pelo usuário na confirmação"
    raise ValueError(f"modo de política desconhecido: {modo}")


class FerramentasSimuladas:
    """Registra chamadas executadas; não faz nada além disso."""

    def __init__(self):
        self.executadas: list[dict] = []

    def executar(self, chamada: dict) -> None:
        self.executadas.append(dict(chamada))
