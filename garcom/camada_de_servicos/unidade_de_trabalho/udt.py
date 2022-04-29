"""
Padrão de projeto Unidade de Trabalho: permite desacoplar
a camada de serviço da camada de dados. Sem o pradão unidade
de trabalho a api se comunica com três camadas: com o banco
de dados para iniciar uma sessão, com a camada repositório para
inicializar o repositorio sqlalchemy e com a camada de serviço
para fazer solicitações.

A ideia é fazer com que a unidade de trabalho gerencie o estado
do banco de dados, deixando a api flask livre dessa responsabilidade.
Com isso, o flask vai ter apenas duas obrigações:
inicializar uma unidade de trabalho e invocar um serviço.
"""


from abc import ABC, abstractmethod
from enum import Enum
from typing import Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from garcom.adaptadores.orm.repositorio import (
    RepositorioConsulta,
    RepositorioDominio,
)
from garcom.config import get_postgres_uri


class UnidadeDeTrabalhoAbstrata(ABC):

    comitado: bool
    repo_consulta: RepositorioConsulta
    repo_dominio: RepositorioDominio
    classe_consulta_repo: Type[RepositorioConsulta]
    classe_dominio_repo: Type[RepositorioDominio]

    def __enter__(self) -> 'UnidadeDeTrabalho':
        self.comitado = False
        return self

    def __exit__(self, *args) -> None:
        self.close()

    def __call__(self, dominio: Enum):
        if not dominio:
            raise ValueError(
                'O dominio deve ser passado para usar a unidade de trabalho'
            )

        self.classe_consulta_repo = dominio.value[0]
        self.classe_dominio_repo = dominio.value[1]

        return self

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(get_postgres_uri(), isolation_level='REPEATABLE READ'),
    expire_on_commit=False,
)


class UnidadeDeTrabalho(UnidadeDeTrabalhoAbstrata):

    repo_consulta: RepositorioConsulta
    repo_dominio: RepositorioDominio

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY) -> None:
        self.session_factory = session_factory

    def __enter__(self):
        self.comitado = False
        self.session = self.session_factory()
        self.repo_consulta: RepositorioConsulta = self.classe_consulta_repo(
            self.session
        )
        self.repo_dominio: RepositorioDominio = self.classe_dominio_repo(
            self.session
        )

        return super().__enter__()

    def close(self) -> None:
        self.session.close()

    def commit(self) -> None:
        self.session.commit()
        self.comitado = True

    def rollback(self) -> None:
        self.session.rollback()


class UnidadeDeTrabalhoFake(UnidadeDeTrabalhoAbstrata):
    pass
