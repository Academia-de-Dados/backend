from sqlalchemy import Boolean, DateTime, Enum, String

from garcom.adaptadores.orm.orm import DbColumn, DbTable, mapper, metadata
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso,
)

usuarios = DbTable(
    'usuarios',
    metadata,
    DbColumn.uuid_primary_key('id'),
    DbColumn('nome', String(length=255), nullable=False),
    DbColumn('senha', String(length=255), nullable=False),
    DbColumn('email', String(length=255), nullable=False, index=True),
    DbColumn('data_de_nascimento', DateTime, nullable=False),
    DbColumn('ativo', Boolean, nullable=False),
    DbColumn('tipo_de_acesso', Enum(TipoDeAcesso), nullable=False),
)


def start_mappers_usuario() -> None:
    mapper.map_imperatively(Usuario, usuarios)
