from dataclasses import dataclass
from datetime import datetime

from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from garcom.barramento import Comando
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso,
)


@dataclass
class CriarUsuario(Comando):
    nome: Nome
    email: Email
    senha: str
    senha_verificacao: str
    data_de_nascimento: datetime
    tipo_de_acesso: TipoDeAcesso


@dataclass(frozen=True)
class BuscarTodosUsuarios(Comando):
    pass


@dataclass(frozen=True)
class BuscarUsuarioPorId(Comando):
    usuario_id: UsuarioId


@dataclass(frozen=True)
class BuscarUsuarioPorEmail(Comando):
    email: Email


@dataclass(frozen=True)
class LogarUsuario(Comando):
    email: Email
    senha: str
