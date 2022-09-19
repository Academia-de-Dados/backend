from abc import ABC

from sqlalchemy.orm.session import Session


class RepositorioConsulta(ABC):
    """
    Interface do repositorio de consulta.

    Esta classe se comporta como uma interface entre a
    unidade de trabalho e a camada de repositorio.
    """

    def __init__(self, session: Session) -> None:
        self.session = session


class RepositorioDominio(ABC):
    """
    Interface do repositorio de dominio..

    Esta classe se comporta como uma interface entre a
    unidade de trabalho e a camada de repositorio.
    OBS: Exatamente igual o anterior, estou estudando se
    pode ser útil no futuro manter separado.
    """

    def __init__(self, session: Session) -> None:
        self.session = session
