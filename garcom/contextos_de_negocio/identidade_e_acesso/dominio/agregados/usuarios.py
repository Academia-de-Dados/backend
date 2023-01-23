from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from dataclass_type_validator import dataclass_validate

from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome, Senha
from garcom.contextos_de_negocio.agregado import Agregado
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)


@dataclass_validate
@dataclass
class Usuario(Agregado):
    nome: Nome
    email: Email
    senha: Senha
    data_de_nascimento: datetime
    ativo: bool = True
    id: Optional[UsuarioId] = None

    eventos = []

    def __post_init__(self):
        self.id = UsuarioId()

    @classmethod
    def cadrastar_novo_usuario(cls, comando: CriarUsuario) -> "Usuario":
        """
        Adicionar conversão para hash
        """
        if comando.senha != comando.senha_verifacao:
            raise cls.SenhasInformadasDevemSerIguais(
                'As duas senhas precisam ser iguais!'
            )
        
        senha = Senha(comando.senha)
        
        return cls(
            nome=comando.nome,
            email=comando.email,
            ativo=comando.ativo,
            data_de_nascimento=comando.data_de_nascimento,
            senha=senha,
        )

    class SenhasInformadasDevemSerIguais(Exception):
        pass