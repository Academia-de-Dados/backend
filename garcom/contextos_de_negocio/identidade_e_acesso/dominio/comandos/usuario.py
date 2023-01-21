from dataclasses import dataclass
from datetime import datetime

from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from garcom.barramento import Comando


@dataclass
class CriarUsuario(Comando):
    nome: Nome
    email: Email
    data_de_nascimento: datetime
    ativo: bool
