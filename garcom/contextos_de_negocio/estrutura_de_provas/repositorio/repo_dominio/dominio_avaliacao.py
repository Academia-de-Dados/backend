from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioAbstratoDominio
from garcom.adaptadores.tipos_nao_primitivos.tipos import AvaliacaoId

from ...dominio.agregados.avaliacao import Avaliacao


class AvaliacaoRepoDominio(RepositorioAbstratoDominio):
    """
    Repositorio concreto de dominio.

    Utiliza a sessão do sqlalchemy para implemetar os
    métodos abstratos.
    """

    def _adicionar(self, avaliacao: Avaliacao) -> None:
        """Adiciona uma avaliacao ao banco de dados."""
        self.session.add(avaliacao)

    def _remover(self) -> None:
        pass

    def _buscar_por_id(self, avaliacao_id: AvaliacaoId) -> None:
        pass
