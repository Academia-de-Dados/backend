from garcom.representacoes import MyBaseModel
from datetime import datetime
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email


class UsuarioConsulta(MyBaseModel):
    nome: str
    email: str
    data_de_nascimento: datetime
    ativo: bool


class UsuarioDominio(MyBaseModel):
    nome: str
    email: str
    senha: str
    senha_verifacao: str
    data_de_nascimento: datetime


class UsuarioLogarApi(MyBaseModel):
    email: Email
    senha: str


class UsuarioLogado(MyBaseModel):
    usuario: UsuarioConsulta
    token_de_acesso: str
