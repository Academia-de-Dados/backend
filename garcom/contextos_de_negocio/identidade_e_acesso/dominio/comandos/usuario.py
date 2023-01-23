from dataclasses import dataclass
from datetime import datetime

from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome, Senha
from garcom.barramento import Comando
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


@dataclass
class CriarUsuario(Comando):
    nome: Nome
    email: Email
    senha: str
    senha_verifacao: str
    data_de_nascimento: datetime


@dataclass
class BuscarTodosUsuarios(Comando):
    pass


@dataclass
class BuscarUsuarioPorId(Comando):
    usuario_id: UsuarioId