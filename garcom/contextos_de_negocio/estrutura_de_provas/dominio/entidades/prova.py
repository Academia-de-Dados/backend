from dataclasses import asdict, dataclass, field
from typing import Set

from dataclass_type_validator import dataclass_validate

from garcom.adaptadores.tipos.tipos import ProvaId

from ..objeto_de_valor.exercicio import Exercicio


@dataclass_validate
@dataclass
class Prova:
    """
    Modelo de prova.

    Representado como uma entidade, sendo comparada
    pelos seus exercicios.
    """

    id: ProvaId = field(
        default_factory=ProvaId, init=False, repr=False, hash=True
    )
    titulo: str = field(compare=False)
    responsavel: str = field(repr=False, compare=False)
    exercicios: Set[Exercicio] = field(repr=False, compare=False)

    def converter_para_dicionario(
        self,
    ) -> dict[str, ProvaId | str | Set[Exercicio]]:
        """
        Método de conversão.

        Método criado para retornar de forma simples
        um dicionario python com os dados da prova.
        """
        return asdict(self)
