from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Type, TypeVar

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from garcom.adaptadores.orm.repositorio import RepositorioAbstrato
from garcom.config import get_postgres_uri

TypeUnidadeAbstrata = TypeVar(
    'TypeUnidadeAbstrata', bound='UnidadeDeTrabalhoAbstrata'  # noqa: F821
)
TypeUnidade = TypeVar('TypeUnidade', bound='UnidadeDeTrabalho')   # noqa: F821


class UnidadeDeTrabalhoAbstrata(ABC):
    """
    Interface da Unidade de Trabalho.

    Utilizada para definir os métodos que
    a classe concreta deve implementar.
    """

    comitado: bool
    repo_consulta: RepositorioAbstrato
    repo_dominio: RepositorioAbstrato
    classe_consulta_repo: Type[RepositorioAbstrato]
    classe_dominio_repo: Type[RepositorioAbstrato]

    def __enter__(self: TypeUnidadeAbstrata) -> TypeUnidadeAbstrata:
        """
        Método mágico dunder enter.

        Utilizado para entrar em um
        gerenciador de contexto.
        """
        self.comitado = False
        return self

    def __exit__(self, *args: tuple[Any]) -> None:
        """
        Método mágico dunder exit.

        Utilizado para sair de um
        gerenciador de contexto.
        """
        self.close()

    def __call__(
        self: TypeUnidadeAbstrata, dominio: Enum
    ) -> TypeUnidadeAbstrata:
        """
        Método mágico dunder call.

        Utilizado para implementar o operador
        de chamada de função. Atribui aos atributos
        de consulta e dominio o tipo de repositório
        correspondente.
        """
        if not dominio:
            raise ValueError(
                'O dominio deve ser passado para usar a unidade de trabalho'
            )

        self.classe_consulta_repo = dominio.value[0]
        self.classe_dominio_repo = dominio.value[1]

        return self

    @abstractmethod
    def commit(self) -> None:
        """
        Método para salvar no banco de dados.

        Encerra a transação salvando
        todas as alterações realizadas durante a
        transação no banco de dados.
        """
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        """
        Método para cancelar uma operação.

        Encerra a transação descartando
        todas as alterações realizados durante
        a transação.
        """
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """
        Método utilizado sair da conexão.

        Fecha a conexão com o banco de dados.
        """
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(get_postgres_uri(), isolation_level='REPEATABLE READ'),
    expire_on_commit=False,
)


class UnidadeDeTrabalho(UnidadeDeTrabalhoAbstrata):
    """
    Unidade de trabalho concreta.

    Implementa principalmente a sessão com
    o banco de dados.
    """

    repo_consulta: RepositorioAbstrato
    repo_dominio: RepositorioAbstrato

    def __init__(
        self, session_factory: sessionmaker = DEFAULT_SESSION_FACTORY
    ) -> None:
        """
        Método dunder init.

        Define uma sessão padrão para se conectar
        com o banco de dados (no caso, postgres).
        """
        self.session_factory = session_factory

    def __enter__(self: TypeUnidade) -> TypeUnidade:
        """
        Método dunder enter.

        Inicia a sessão do banco de dados e
        instância os repositório de consulta
        e dominio para utilizar a sessão.
        """
        self.comitado = False
        self.session = self.session_factory()
        self.repo_consulta: RepositorioAbstrato = self.classe_consulta_repo(
            self.session
        )
        self.repo_dominio: RepositorioAbstrato = self.classe_dominio_repo(
            self.session
        )

        return super().__enter__()

    def close(self) -> None:
        """
        Método para fechar a conexão.

        Utiliza o método close da sesssão
        para fechar a conexão com o banco
        de dados.
        """
        # if not self.comitado:
        #    self.rollback()

        self.session.close()

    def commit(self) -> None:
        """
        Método para salvar no banco.

        Utiliza o commit da sessão para
        encerrar a transação e salvar
        as modificações no banco de dados.
        """
        self.session.commit()
        self.comitado = True

    def rollback(self) -> None:
        """
        Método para cancelar uma transação.

        Utiliza o método rollback da sessão
        encerrar a transação e descartar as
        alterações iniciado durante a transação.
        """
        self.session.rollback()
