from datetime import datetime

from garcom.adaptadores.tipos_nao_primitivos.usuario import Email
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso,
)
from garcom.representacoes import MyBaseModel


class UsuarioConsulta(MyBaseModel):
    nome: str
    email: Email
    data_de_nascimento: datetime
    ativo: bool


class UsuarioDominio(MyBaseModel):
    nome: str
    email: Email
    senha: str
    senha_verificacao: str
    data_de_nascimento: datetime
    tipo_de_acesso: TipoDeAcesso


class UsuarioLogarApi(MyBaseModel):
    # email: Email
    # senha: str
    username: str
    password: str


class UsuarioLogado(MyBaseModel):
    usuario: UsuarioConsulta
    access_token: str
    token_type: str
