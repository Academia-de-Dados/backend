from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioDominio


class ProvaAbstratoDominio(RepositorioDominio):
    """
    Repositorio abstrato de dominio.

    Implementa os métodos que alteram o banco de dados.
    """

    @abstractmethod
    def adicionar(self) -> None:
        """Adiciona uma nova prova no banco."""
        raise NotImplementedError

    @abstractmethod
    def remover(self) -> None:
        """Remove um prova do banco."""
        raise NotImplementedError


class ProvaRepoDominio(ProvaAbstratoDominio):
    """
    Repositorio concreto de dominio.

    Utiliza a sessão do sqlalchemy para implemetar os
    métodos abstratos.
    """

    pass
