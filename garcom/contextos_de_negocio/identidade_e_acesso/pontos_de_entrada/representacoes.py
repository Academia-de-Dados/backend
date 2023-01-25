from garcom.representacoes import MyBaseModel
from datetime import datetime


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
