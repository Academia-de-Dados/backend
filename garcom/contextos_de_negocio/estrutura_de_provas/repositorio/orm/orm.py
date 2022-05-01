from sqlalchemy import ARRAY, Boolean, DateTime, String, Text, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper

from garcom.adaptadores.orm.orm import DbColumn, DbTable, metadata
from garcom.adaptadores.tipos.tipos import SET
from garcom.config import get_postgres_uri
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.entidades.prova import (  # noqa
    Prova,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)

exercicios = DbTable(
    'exercicio',
    metadata,
    DbColumn.uuid_primary_key('id'),
    DbColumn('materia', String(length=255), nullable=False, index=True),
    DbColumn('assunto', String(length=255), nullable=False, index=True),
    DbColumn('enunciado', Text, nullable=False),
    DbColumn('multipla_escolha', Boolean, nullable=False),
    DbColumn('alternativas', ARRAY(String), nullable=True),
    DbColumn('dificuldade', String(length=255), nullable=False),
    DbColumn('origem', String(length=255), nullable=True),
    DbColumn('data_lancamento', DateTime, nullable=True),
)

prova = DbTable(
    'prova',
    metadata,
    DbColumn.uuid_primary_key('id'),
    DbColumn('titulo', String(length=255), nullable=False, index=True),
    DbColumn('responsavel', String(length=255), nullable=False, index=True),
    DbColumn('id_dos_exercicios', SET(UUID()), nullable=False),
)


def init_database() -> None:
    """
    Método para iniciar o banco de dados.

    Utilize esse método para criar as tabelas no banco de dados.
    """
    metadata.bind = create_engine(get_postgres_uri())
    metadata.create_all()


def start_mappers() -> None:
    """
    Método para começar o mapeamento.

    Este método deveria iniciar o mapeamento do banco de dados,
    atualmente ele não faz isso e eu ainda não descobri o porque.
    """
    prova_mapper = mapper(Prova, prova)   # noqa
    exericios_mapper = mapper(Exercicio, exercicios)   # noqa
