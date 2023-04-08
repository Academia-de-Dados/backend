from typing import Annotated

from fastapi import Depends

from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.autenticacao import (
    pegar_usuario_ativo,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.aplicacao.sentry import loggers
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import (
    UsuarioSemPermissaoNecessaria,
)

UsuarioAtivo = Annotated[Usuario, Depends(pegar_usuario_ativo)]

MENSAGEM = 'Usuário não autorizado a realizar esta ação!'

ExcessaoSemPermissao = UsuarioSemPermissaoNecessaria(
    status_code=403,
    detail=MENSAGEM,
    headers={'WWW-Authenticate': 'Bearer'},
)


def usuario_administrador(usuario: UsuarioAtivo) -> UsuarioAtivo:

    tipo_de_acesso = usuario.tipo_de_acesso
    if tipo_de_acesso != TipoDeAcesso.administrador:
        loggers.error(
            MENSAGEM,
            extra={'usuario': usuario.email},
        )
        raise ExcessaoSemPermissao

    return usuario


def usuario_professor(usuario: UsuarioAtivo) -> UsuarioAtivo:

    tipo_de_acesso = usuario.tipo_de_acesso
    if tipo_de_acesso != TipoDeAcesso.professor:
        loggers.error(
            MENSAGEM,
            extra={'usuario': usuario.email},
        )
        raise ExcessaoSemPermissao

    return usuario