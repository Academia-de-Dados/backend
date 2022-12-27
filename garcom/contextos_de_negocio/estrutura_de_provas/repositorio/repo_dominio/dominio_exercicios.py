from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioAbstratoDominio

from ...dominio.agregados.exercicio import Exercicio
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId


class ExercicioRepoDominio(RepositorioAbstratoDominio):
    """
    Repositorio concreto de dominio.

    Possui a implementação dos métodos abstratos,
    utilizando a sessão do sqlalchemy.
    """
    
    def _adicionar(self, exercicio: Exercicio) -> None:
        """Adiciona um exercicio ao banco de dados."""
        self.session.add(exercicio)

    def _remover(self) -> None:
        """Remove um exercicio do banco de dados."""
        pass

    def _buscar_por_id(self, exercicio_id: ExercicioId) -> None:
        pass