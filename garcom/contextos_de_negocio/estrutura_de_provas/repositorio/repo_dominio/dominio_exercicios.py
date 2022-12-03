from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioAbstratoDominio

from ...dominio.agregados.exercicio import Exercicio
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId


class ExercicioAbstratoDominio(RepositorioAbstratoDominio):
    """
    Repositorio abstrato de dominio.

    Classe utilizada para implementar os métodos
    que alteram o banco de dados.
    
    O atributo 'agregados' é utilizado para adicionar as instancias
    dos agregados iniciados, para poder coletar os eventos emitidos
    por eles. Apenas repositorio de dominio emitir eventos, não usar
    no de consulta.
    """

    def adicionar(self, agregado):
        self._adicionar(agregado)
        self.agregados.add(agregado)

    def remover(self, agregado):
        self._remover(agregado)
        self.agregados.add(agregado)

    def buscar_por_id(self, exercicio_id: ExercicioId):
        agregado = self._buscar_por_id(exercicio_id)
        if agregado:
            self.agregados.add(agregado)
        return agregado

    @abstractmethod
    def _adicionar(self, exercicio: Exercicio) -> None:
        """Adiciona um novo exercicio ao banco."""
        raise NotImplementedError

    @abstractmethod
    def _remover(self) -> None:
        """Remove um exercicio do banco."""
        raise NotImplementedError

    @abstractmethod
    def _buscar_por_id(self, exercicio_id: ExercicioId) -> None:
        raise NotImplementedError


class ExercicioRepoDominio(ExercicioAbstratoDominio):
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