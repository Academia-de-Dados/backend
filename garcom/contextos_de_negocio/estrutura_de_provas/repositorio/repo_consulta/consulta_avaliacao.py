from abc import abstractmethod
from uuid import UUID

from sqlalchemy.future import select

from garcom.adaptadores.orm.repositorio import RepositorioAbstrato
from garcom.adaptadores.tipos_nao_primitivos.tipos import AvaliacaoId

from ...dominio.agregados.avaliacao import Avaliacao


class AvaliacaoAbstratoConsulta(RepositorioAbstrato):
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


class AvaliacaoRepoConsulta(AvaliacaoAbstratoConsulta):
    """Repositorio concreto de consulta."""

    def consultar_todos(self) -> list[Avaliacao]:
        """Implementa uma query por todas as avaliacoes"""
        avaliacoes = self.session.execute(select(Avaliacao))
        return avaliacoes.scalars().all()

    def consultar_por_id(self, id: AvaliacaoId) -> Avaliacao:
        """Implementa uma query de avaliacao por id."""
        return self.session.query(Avaliacao).filter_by(id=id).first()
