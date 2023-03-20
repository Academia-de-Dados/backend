from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from fastapi.testclient import TestClient
from garcom.config import get_postgres_tests
from garcom.aplicacao.main import app
from garcom.adaptadores.orm.orm import metadata
from tests.mocks import UnidadeDeTrabalhoFake
from tests.testes_unitarios.mocks import RepoFake
from garcom.adaptadores.orm.orm import iniciar_mapeamento


@fixture
def cliente(session_factory) -> TestClient:
    """Cria um cliente de testes."""
    session_factory()
    cliente = TestClient(app)

    yield cliente


@fixture
def mock_uow():
    """
    Mock unidade de trabalho.

    Cria uma unidade de trabalho fake com
    o repositorio fake.
    """
    uow = UnidadeDeTrabalhoFake(RepoFake())
    yield uow


@fixture
def engine():
    """Cria a engine e o banco de testes."""
    engine = create_engine(get_postgres_tests())
    metadata.create_all(engine)
    return engine


@fixture
def session_factory(engine):
    """Cria a sessão e o mapeamento das tabelas."""
    iniciar_mapeamento()
    yield sessionmaker(bind=engine)
    clear_mappers()


@fixture
def session(session_factory):
    """
    Instância a sessão.

    Cria uma sessão consumivel e apaga as tabelas
    depois dela ser consumida.
    """
    session = session_factory()
    yield session

    # Apaga todos os dados do banco depois que executa o teste
    for tabela in reversed(metadata.sorted_tables):
        session.execute(tabela.delete())
    session.commit()


from tests.mocks_contextos.usuario import *
