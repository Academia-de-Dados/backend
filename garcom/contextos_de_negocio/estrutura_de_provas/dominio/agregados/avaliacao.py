from dataclasses import dataclass
from typing import Optional

from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao
from garcom.adaptadores.tipos_nao_primitivos.tipos import AvaliacaoId

from ....agregado import Agregado
from ..agregados.exercicio import Exercicio
from ..comandos.avaliacao import CriarAvaliacao


@dataclass
class Avaliacao(Agregado):

    titulo: str
    responsavel: str
    tipo_de_avaliacao: TipoDeAvaliacao
    exercicios: set[Exercicio]
    id: Optional[AvaliacaoId] = None

    def __post_init__(self):
        self.id = AvaliacaoId()

    def __eq__(self, other: 'Avaliacao') -> bool:
        """
        Método de igualdade.

        Dunder eq utiliza o operador 'is' para comparar objetos.
        Nesse caso, estamos comparando duas provas pelo seu id.
        Atente-se que, implementar eq faz com que o python defina
        __hash__ igual a None.
        """
        return isinstance(other, self.__class__) and self.id == other.id

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
        return f'<Avaliação {self.titulo}, {self.responsavel}>'

    @classmethod
    def criar_avaliacao(
        cls, comando: CriarAvaliacao, exercicios: set[Exercicio]
    ) -> 'Avaliacao':

        return cls(
            titulo=comando.titulo,
            responsavel=comando.responsavel,
            tipo_de_avaliacao=comando.tipo_de_avaliacao,
            exercicios=exercicios,
        )
