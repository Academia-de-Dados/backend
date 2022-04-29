from abc import abstractmethod

from garcom.adaptadores.orm.repositorio import RepositorioDominio


class ProvaAbstratoDominio(RepositorioDominio):
    @abstractmethod
    def adicionar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def remover(self) -> None:
        raise NotImplementedError


class ProvaRepoDominio(ProvaAbstratoDominio):

    # implementar os add, update, delete, etc, aqui.
    pass
