from dataclasses import dataclass
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

    titulo: str
    responsavel: str
    exercicios: Set[Exercicio]
    id: ProvaId = ProvaId()

    def __eq__(self, other: object) -> bool:
        """
        Método de igualdade.

        Dunder eq utiliza o operador 'is' para comparar objetos.
        Nesse caso, estamos comparando duas provas pelo exercicios
        que ela contém. Atente-se que, implementar eq faz com que o
        python defina __hash__ igual a None.
        """
        if not isinstance(other, Prova):
            return NotImplemented
        return self.exercicios == other.exercicios

    def __hash__(self) -> int:
        """
        Método de comparação.

        Como o método dunder eq foi implementado, precisamos implementar
        o método hash para que nossa classe possa ser usada em dicionarios
        e conjuntos.
        """
        return hash(self.id)

    def __repr__(self) -> str:
        """
        Método de representação.

        Implementado para representar a prova
        pelo titulo.
        """
        return f'<Prova {self.titulo}>'

    def converter_para_dicionario(self) -> dict[str, str | set[Exercicio]]:
        """
        Método de conversão.

        Método criado para retornar de forma simples
        um dicionario python com os dados da prova.
        """
        return {
            'titulo': self.titulo,
            'responsavel': self.responsavel,
            'exercicios': self.exercicios,
            'id': str(self.id),
        }

    @classmethod
    def criar_novo(
        cls, titulo: str, responsavel: str, exercicios: Set[Exercicio]
    ) -> 'Prova':
        """
        Método de criação.

        Méto implementado para poder criar
        um novo objeto espelhado na classe.
        """
        return cls(
            id=ProvaId(),
            titulo=titulo,
            responsavel=responsavel,
            exercicios=exercicios,
        )
