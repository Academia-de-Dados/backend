from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioAbstrato

from ...dominio.agregados.avaliacao import Avaliacao


class AvaliacaoAbstratoDominio(RepositorioAbstrato):
    """
    Repositorio abstrato de dominio.

    Implementa os métodos que alteram o banco de dados.
    """

    @abstractmethod
    def adicionar(self) -> None:
        """Adiciona uma nova avaliacao no banco."""
        raise NotImplementedError

    @abstractmethod
    def remover(self) -> None:
        """Remove uma avaliacao do banco."""
        raise NotImplementedError


class AvaliacaoRepoDominio(AvaliacaoAbstratoDominio):
    """
    Repositorio concreto de dominio.

    Utiliza a sessão do sqlalchemy para implemetar os
    métodos abstratos.
    """

    def adicionar(self, avaliacao: Avaliacao) -> None:
        """Adiciona uma avaliacao ao banco de dados."""
        return self.session.add(avaliacao)

    def remover(self) -> None:
        pass
