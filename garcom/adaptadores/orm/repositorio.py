from abc import ABC

from sqlalchemy.orm.session import Session


class RepositorioAbstrato(ABC):
    """
    Interface do repositorio de consulta.

    Esta classe se comporta como uma interface entre a
    unidade de trabalho e a camada de repositorio.
    """

    def __init__(self, session: Session) -> None:
        self.session = session
