from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioAbstrato

from ...dominio.agregados.exercicio import Exercicio


class ExercicioAbstratoDominio(RepositorioAbstrato):
    """
    Repositorio abstrato de dominio.

    Classe utilizada para implementar os métodos
    que alteram o banco de dados.
    
    O atributo 'agregados' é utilizado para adicionar as instancias
    dos agregados iniciados, para poder coletar os eventos emitidos
    por eles. Apenas repositorio de dominio emitir eventos, não usar
    no de consulta.
    """
    def __init__(self):
        super().__init__()
        self.agregados = set()

    def adicionar(self, agregado):
        self.add(agregado)
        self.agregados.add(agregado)

    @abstractmethod
    def add(self, exercicio: Exercicio) -> None:
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

    def add(self, exercicio: Exercicio) -> None:
        """Adiciona um exercicio ao banco de dados."""
        return self.session.add(exercicio)

    def remover(self) -> None:
        """Remove um exercicio do banco de dados."""
        pass
