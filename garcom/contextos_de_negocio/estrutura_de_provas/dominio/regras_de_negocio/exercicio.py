from enum import Enum

from .....adaptadores.tipos_nao_primitivos.exercicio import (
    AssuntosMatematica,
    AssuntosPortugues,
)
from ...execessoes import AssuntoNaoEncontrado


def remove_acentos_e_deixa_caixa_baixa(texto: str) -> str:
    """
    Sim, essa função é um exemplo do python fluente.
    """
    from unicodedata import combining, normalize

    texto_normalizado = normalize("NFD", texto)
    filtrar = "".join(c for c in texto_normalizado if not combining(c))

    return normalize("NFC", filtrar).lower().strip().replace(" ", "_")


def verificar_qual_o_tipo_enum_do_assunto(assunto: str) -> Enum:
    """Função que verifica se o assunto existe nos assuntos disponíveis."""

    if assunto in AssuntosMatematica:
        return AssuntosMatematica(assunto)

    elif assunto in AssuntosPortugues:
        return AssuntosPortugues(assunto)

    else:
        raise AssuntoNaoEncontrado(
            "O assunto passado não foi encontrado nos assuntos existentes!"
        )
