from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioDominio
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)


class ExercicioAbstratoDominio(RepositorioDominio):
    """
    Repositorio abstrato de dominio.

    Classe utilizada para implementar os métodos
    que alteram o banco de dados.
    """

    @abstractmethod
    def adicionar(self, exercicio: Exercicio) -> None:
        """Adiciona um novo exercicio ao banco."""
        raise NotImplementedError

    @abstractmethod
    def remover(self) -> None:
        """Remove um exercicio do banco."""
        raise NotImplementedError


class ExercicioRepoDominio(ExercicioAbstratoDominio):
    """
    Repositorio concreto de dominio.

    Possui a implementação dos métodos abstratos,
    utilizando a sessão do sqlalchemy.
    """

    def adicionar(self, exercicio: Exercicio) -> None:
        """Adiciona um exercicio ao banco de dados."""
        return self.session.add(exercicio)

    def remover(self) -> None:
        """Remove um exercicio do banco de dados."""
        pass
