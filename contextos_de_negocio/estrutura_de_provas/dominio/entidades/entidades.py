"""
Entidade difere do objeto de valor no quesito de poder ser alterado.
Uma entidade possui igualdade de identidade, ou seja, podemos mudar
seus valores que eles ainda são reconhecidos como a mesma coisa.

Exemplo: Podemos ter uma prova com 5 questoes e outra com 4, ainda assim
ambos ainda vão ser uma prova.

* Tornamos explicito que se trata de uma entidade implementando os métodos
* mágicos __eq__ e __hash__
"""

from dataclasses import dataclass
from typing import Set

from ..objeto_de_valor.objeto_de_valor import Exercicio


@dataclass
class Prova:
    """
    O metodo magico eq define o comportamento de igualdade.
    """

    def __init__(self, data: str | None = None):
        self._exercicios: Set[Exercicio] = set()

    @property
    def exercicios(self) -> Set[Exercicio]:
        return self._exercicios

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Prova):
            return NotImplemented
        return self.exercicios == other.exercicios
