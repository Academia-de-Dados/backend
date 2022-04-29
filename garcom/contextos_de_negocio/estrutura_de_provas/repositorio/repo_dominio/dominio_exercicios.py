from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioDominio
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)


class ExercicioAbstratoDominio(RepositorioDominio):
    @abstractmethod
    def adicionar(self):
        raise NotImplementedError

    @abstractmethod
    def remover(self):
        raise NotImplementedError


class ExercicioRepoDominio(ExercicioAbstratoDominio):

    # implementar os add, update, delete, etc, aqui.
    def adicionar(self, exercicio: Exercicio) -> None:
        return self.session.add(exercicio)

    def remover(self):
        pass
