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

from dataclass_type_validator import dataclass_validate

from garcom.adaptadores.tipos.tipos import ExercicioId, ProvaId


@dataclass_validate
@dataclass
class Prova:
    """
    O metodo magico eq define o comportamento de igualdade.
    """

    id: ProvaId
    titulo: str
    responsavel: str
    exercicios: Set[ExercicioId]

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Prova):
            return NotImplemented
        return self.exercicios == other.exercicios

    def __repr__(self) -> str:
        return f'<Prova {self.titulo}>'

    @classmethod
    def criar_novo(
        cls, titulo: str, responsavel: str, exercicios: Set[ExercicioId]
    ) -> 'Prova':
        return cls(
            id=ProvaId(),
            titulo=titulo,
            responsavel=responsavel,
            exercicios=exercicios,
        )
