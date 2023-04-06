from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from garcom.aplicacao.sentry import loggers
from garcom.barramento import BarramentoDeMensagens
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.contextos_de_negocio.barramento.identidade_e_acesso import (
    MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    BuscarUsuarioPorEmail,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    validar_token_de_acesso,
)
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import (
    TokenDeAcessoExpirado,
    UsuarioNaoAutorizado,
    UsuarioNaoEncontrado,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso,
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='usuarios/signin/', scheme_name='JWT'
)

exececao = UsuarioNaoAutorizado(
    status_code=401,
    detail='Falha ao validar credenciais!',
    headers={'WWW-Authenticate': 'Bearer'},
)


Token = Annotated[str, Depends(oauth2_scheme)]


def pegar_usuario_ativo(token: Token) -> Usuario:

    unidade_de_trabalho = UnidadeDeTrabalho()
    try:
        info_token = validar_token_de_acesso(token)
    except JWTError as exc:
        if str(exc) == 'Signature has expired.':
            raise TokenDeAcessoExpirado(
                status_code=403,
                detail='Token de acesso expirado! Faça login novamente.',
                headers={'WWW-Authenticate': 'Bearer'},
            )
        else:
            raise exececao

    email_do_usuario = info_token.sub
    if email_do_usuario is None:
        raise exececao

    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    )

    comando = BuscarUsuarioPorEmail(email=email_do_usuario)

    usuario = barramento.manipulador(comando)
    if not usuario:
        raise UsuarioNaoEncontrado(
            status_code=404,
            detail='Usuário não encontrado!',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return usuario


def usuario_administrador(usuario: Usuario = Depends(pegar_usuario_ativo)):

    tipo_de_acesso = usuario.tipo_de_acesso
    if tipo_de_acesso != TipoDeAcesso.administrador:
        loggers.error(
            'Usuário não autorizado a realizar esta ação!',
            extra={'usuario': usuario.email},
        )
        raise exececao
    
    return usuario


def usuario_professor(usuario: Usuario = Depends(pegar_usuario_ativo)):

    tipo_de_acesso = usuario.tipo_de_acesso
    if tipo_de_acesso != TipoDeAcesso.professor:
        loggers.error(
            'Usuário não autorizado a realizar esta ação!',
            extra={'usuario': usuario.email},
        )
        raise exececao
    
    return usuario