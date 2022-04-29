import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, MetaData, Table, func
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()


class DbColumn(Column):
    def __init__(self, *args, **kwargs) -> None:
        # Sqlalchemy define como padrão nullable = True,
        # ou seja, permite campos nulos
        if 'nullable' not in kwargs:
            kwargs['nullable'] = False

        super().__init__(*args, **kwargs)

    @staticmethod
    def uuid_primary_key(field_name: str) -> Column:
        return Column(
            field_name,
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            unique=True,
            nullable=False,
        )


class DbTable(Table):
    def __init__(
        self, *args, herda_do_public: 'DbTable' = None, **kwargs
    ) -> None:

        self.herda_do_public = herda_do_public
        super().__init__(*args, **kwargs)

    def _init(cls, *args, herda_do_public: bool = False, **kwargs) -> None:
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
