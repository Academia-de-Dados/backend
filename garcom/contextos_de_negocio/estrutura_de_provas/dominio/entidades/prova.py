"""
Entidade difere do objeto de valor no quesito de poder ser alterado.
Uma entidade possui igualdade de identidade, ou seja, podemos mudar
seus valores que eles ainda são reconhecidos como a mesma coisa.

Exemplo: Podemos ter uma prova com 5 questoes e outra com 4, ainda assim
ambos ainda vão ser uma prova.
"""
from dataclasses import dataclass, field
from typing import Set

from dataclass_type_validator import dataclass_validate

from garcom.adaptadores.tipos.tipos import ExercicioId, ProvaId


@dataclass_validate
@dataclass
class Prova:
    """
    O metodo magico eq define o comportamento de igualdade.
    """

    id: ProvaId = field(
        default_factory=ProvaId, init=False, repr=False, hash=True
    )
    titulo: str = field(compare=False)
    responsavel: str = field(repr=False, compare=False)
    exercicios: Set[ExercicioId] = field(repr=False, compare=False)
