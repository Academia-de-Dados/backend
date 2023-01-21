from dataclasses import dataclass
from datetime import datetime
from garcom.barramento import Comando
from garcom.adaptadores.tipos_nao_primitivos.usuario import Nome, Email


@dataclass
class CriarUsuario(Comando):
    nome: Nome
    email: Email
    data_de_nascimento: datetime
    ativo: bool