from dataclasses import dataclass
from datetime import datetime

from garcom.adaptadores.tipos.tipos import ExercicioId


@dataclass(unsafe_hash=True)
class Exercicio:
    """
    Modelo de exercicio.

    Representado como um objeto de valor,
    para que seja identificado por seus atributos.
    """

    materia: str
    assunto: str
    dificuldade: str
    enunciado: str
    alternativas: list[str] | None
    origem: str | None = None
    multipla_escolha: bool = False
    id: ExercicioId = ExercicioId()
    data_lancamento: datetime | None = None
