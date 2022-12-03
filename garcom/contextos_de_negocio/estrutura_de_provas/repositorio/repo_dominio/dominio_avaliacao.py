from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioAbstratoDominio

from ...dominio.agregados.avaliacao import Avaliacao
from garcom.adaptadores.tipos_nao_primitivos.tipos import AvaliacaoId

class AvaliacaoAbstratoDominio(RepositorioAbstratoDominio):
    """
    Repositorio abstrato de dominio.

    Implementa os métodos que alteram o banco de dados.
    """

    def adicionar(self, agregado):
        self._adicionar(agregado)
        self.agregados.add(agregado)

    def remover(self, agregado):
        self._remover(agregado)
        self.agregados.add(agregado)

    def buscar_por_id(self, avaliacao_id: AvaliacaoId):
        agregado = self._buscar_por_id(avaliacao_id)
        if agregado:
            self.agregados.add(agregado)
        return agregado

    @abstractmethod
    def _adicionar(self) -> None:
        """Adiciona uma nova avaliacao no banco."""
        raise NotImplementedError

    @abstractmethod
    def _remover(self) -> None:
        """Remove uma avaliacao do banco."""
        raise NotImplementedError

    @abstractmethod
    def _buscar_por_id(self, avaliacao_id: AvaliacaoId) -> None:
        raise NotImplementedError


class AvaliacaoRepoDominio(AvaliacaoAbstratoDominio):
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

    def __buscar_por_id(self, avaliacao_id: AvaliacaoId) -> None:
        pass