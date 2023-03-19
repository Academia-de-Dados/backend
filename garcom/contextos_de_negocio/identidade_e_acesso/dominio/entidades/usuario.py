from dataclasses import dataclass
from datetime import datetime
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(frozen=True)
class UsuarioLeitura:
    nome: Nome
    email: Email
    ativo: bool
    data_de_nascimento: datetime


@dataclass_validate
@dataclass(frozen=True)
class UsuarioLogado:
    usuario: UsuarioLeitura
    access_token: str
    token_type: str = "Bearer"
