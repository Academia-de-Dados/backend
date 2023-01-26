from dataclasses import dataclass
from datetime import datetime

from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from garcom.barramento import Comando
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


@dataclass
class CriarUsuario(Comando):
    nome: Nome
    email: Email
    senha: str
    senha_verifacao: str
    data_de_nascimento: datetime


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
