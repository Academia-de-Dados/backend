from sqlalchemy import Boolean, DateTime, String

from garcom.adaptadores.orm.orm import DbColumn, DbTable, mapper, metadata
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)

usuarios = DbTable(
    'usuarios',
    metadata,
    DbColumn.uuid_primary_key('id'),
    DbColumn('nome', String(length=255), nullable=False),
    DbColumn('email', String(length=255), nullable=False, index=True),
    DbColumn('data_de_nascimento', DateTime, nullable=False),
    DbColumn('ativo', Boolean, nullable=False),
)


def start_mappers_usuario() -> None:
    mapper.map_imperatively(Usuario, usuarios)
