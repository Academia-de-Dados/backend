import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, Table, func
from sqlalchemy.dialects.postgresql import UUID
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
        cls,
        *args: tuple[Any],
        herda_do_public: bool = False,
        **kwargs: dict[Any, Any]
    ) -> None:
        super()._init(
            *args,
            DbColumn(
                'criado_em', DateTime, default=datetime.utcnow, nullable=False
            ),
            DbColumn(
                'ultima_modificacao',
                DateTime,
                server_default=func.now(),
                server_onupdate=func.now(),
                onupdate=datetime.utcnow,
                nullable=False,
            ),
            **kwargs,
        )
