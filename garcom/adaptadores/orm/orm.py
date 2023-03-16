import uuid
from typing import Any
from datetime import datetime

from sqlalchemy import Column, DateTime, Table, func, create_engine
from sqlalchemy.dialects.postgresql import UUID
from garcom.config import get_postgres_uri
from sqlalchemy.orm import registry

mapper = registry()
metadata = mapper.metadata


class DbColumn(Column):
    """
    Classe coluna.

    Herda da Column do sqlalchemy e implementa
    um método estático para id do tipo uuid.
    """

    @staticmethod
    def uuid_primary_key(field_name: str) -> Column:
        """
        Método de chave primária.

        Cria uma coluna de chave primária com
        uuid do tipo hash.
        """
        return Column(
            field_name,
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            unique=True,
            nullable=False,
        )


class DbTable(Table):
    """
    Classe tabela.

    Herda de Table do sqlalchemy e implementa
    colunas padrão de data de criação.
    """

    def _init(
        cls, *args: tuple[Any], herda_do_public: bool = False, **kwargs: dict[Any, Any]
    ) -> None:
        super()._init(
            *args,
            DbColumn("criado_em", DateTime, default=datetime.utcnow, nullable=False),
            DbColumn(
                "ultima_modificacao",
                DateTime,
                server_default=func.now(),
                server_onupdate=func.now(),
                onupdate=datetime.utcnow,
                nullable=False,
            ),
            **kwargs,
        )


def iniciar_mapeamento():
    """
    Adicionar os start mappers aqui.
    """
    from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.orm.orm import (
        start_mappers,
    )
    from garcom.contextos_de_negocio.identidade_e_acesso.repositorio.orm.usuario import (
        start_mappers_usuario
    )
    
    start_mappers()
    start_mappers_usuario()


def init_database() -> None:
    """
    Método para iniciar o banco de dados.

    Utilize esse método para criar as tabelas no banco de dados.
    """
    metadata.bind = create_engine(get_postgres_uri())
    metadata.create_all()