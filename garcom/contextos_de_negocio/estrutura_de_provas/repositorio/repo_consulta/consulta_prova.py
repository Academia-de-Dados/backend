from abc import abstractmethod
from uuid import UUID

from garcom.adaptadores.orm.repositorio import RepositorioConsulta


class ProvaAbstratoConsulta(RepositorioConsulta):
    @abstractmethod
    def consultar_todos(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def consultar_por_id(self, id: UUID) -> None:
        raise NotImplementedError


class ProvaRepoConsulta(ProvaAbstratoConsulta):
    # implementar as querys aqui
    pass
