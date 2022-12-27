from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.orm.session import Session
from garcom.contextos_de_negocio.agregado import Agregado

class RepositorioAbstrato(ABC):
    """
    Interface do repositorio.

    Esta classe se comporta como uma interface entre a
    unidade de trabalho e a camada de repositorio.
    """

    def __init__(self, session: Session) -> None:
        self.session = session


class RepositorioAbstratoDominio(ABC):
    """
    Repositorio abstrato de dominio.
    Classe utilizada para implementar os métodos
    que alteram o banco de dados.
    
    O atributo 'agregados' é utilizado para adicionar as instancias
    dos agregados iniciados, para poder coletar os eventos emitidos
    por eles. Apenas repositorio de dominio podem emitir eventos, 
    não usar no de consulta.
    """

    def __init__(self, session: Session):
        self.agregados = set()
        self.session = session

    def adicionar(self, agregado):
        self._adicionar(agregado)
        self.agregados.add(agregado)

    def remover(self, agregado):
        self._remover(agregado)
        self.agregados.add(agregado)

    def buscar_por_id(self, agregado_id: UUID):
        agregado = self._buscar_por_id(agregado_id)
        if agregado:
            self.agregados.add(agregado)
        return agregado

    @abstractmethod
    def _adicionar(self, agregado: Agregado) -> None:
        """Adiciona um novo exercicio ao banco."""
        raise NotImplementedError

    @abstractmethod
    def _remover(self) -> None:
        """Remove um exercicio do banco."""
        raise NotImplementedError

    @abstractmethod
    def _buscar_por_id(self, agregado_id: UUID) -> None:
        raise NotImplementedError