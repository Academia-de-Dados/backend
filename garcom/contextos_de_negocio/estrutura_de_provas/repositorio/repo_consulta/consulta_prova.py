from abc import abstractmethod
from uuid import UUID

from garcom.adaptadores.orm.repositorio import RepositorioConsulta


class ProvaAbstratoConsulta(RepositorioConsulta):
    """
    Repositorio abstrato de consulta.

    Possui os método que o repositorio concreto
    deve implementar.
    """

    @abstractmethod
    def consultar_todos(self) -> None:
        """Retorna todas as provas."""
        raise NotImplementedError

    @abstractmethod
    def consultar_por_id(self, id: UUID) -> None:
        """Retorna uma prova pelo seu id."""
        raise NotImplementedError


class ProvaRepoConsulta(ProvaAbstratoConsulta):
    """Repositorio concreto de consulta."""

    pass
