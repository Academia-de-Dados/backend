from abc import ABC

from sqlalchemy.orm.session import Session


class RepositorioConsulta(ABC):
    def __init__(self, session: Session) -> None:
        self.session = session


class RepositorioDominio(ABC):
    def __init__(self, session: Session) -> None:
        self.session = session
