import contextlib
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from garcom.config import get_postgres_tests
from garcom.adaptadores.orm.orm import metadata
from tests.mocks import UnidadeDeTrabalhoFake
from tests.testes_unitarios.exercicios.mocks import RepoExercicioFake
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.orm.orm import start_mappers


@fixture
def mock_uow_exercicio():
    """
    Mock unidade de trabalho.
    
    Cria uma unidade de trabalho fake com
    o repositorio de exercicios fake.
    """
    uow = UnidadeDeTrabalhoFake(RepoExercicioFake())
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
    start_mappers()
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