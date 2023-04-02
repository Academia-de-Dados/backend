from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from dataclass_type_validator import dataclass_validate

from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from garcom.contextos_de_negocio.agregado import Agregado
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso
)


@dataclass_validate
@dataclass
class Usuario(Agregado):
    nome: Nome
    email: Email
    tipo_de_acesso: TipoDeAcesso
    senha: str
    data_de_nascimento: datetime
    ativo: bool = True
    id: Optional[UsuarioId] = None

    eventos = []

    def __post_init__(self):
        self.id = UsuarioId()

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def criar_usuario(cls, comando: CriarUsuario) -> 'Usuario':
        """
        Adicionar conversão para hash
        """
        return cls(
            nome=comando.nome,
            email=comando.email,
            data_de_nascimento=comando.data_de_nascimento,
            senha=comando.senha,
            tipo_de_acesso=comando.tipo_de_acesso,
        )