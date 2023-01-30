from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import JWTError
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    validar_token_de_acesso,
    verificar_senha,
    criar_token_de_acesso,
)
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.contextos_de_negocio.barramento.identidade_e_acesso import (
    MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
)
from garcom.barramento import BarramentoDeMensagens
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    BuscarUsuarioPorEmail,
)
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import (
    UsuarioNaoAutorizado,
    TokenDeAcessoExpirado,
)
from datetime import datetime


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/signin/", scheme_name="JWT")

exececao = UsuarioNaoAutorizado(
    status_code=401,
    detail="Falha ao validar credenciais!",
    headers={"WWW-Authenticate": "Bearer"},
)


def pegar_usuario_ativo(token: str = Depends(oauth2_scheme)):

    unidade_de_trabalho = UnidadeDeTrabalho()
    try:
        info_token = validar_token_de_acesso(token)
        email_do_usuario = info_token.sub
        if email_do_usuario is None:
            raise exececao

        if datetime.fromtimestamp(info_token.tempo_de_expiracao) < datetime.now():
            raise TokenDeAcessoExpirado(
                status_code=403,
                detail="Token de acesso expirado! Faça login novamente.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    except JWTError:
        raise exececao

    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    )

    comando = BuscarUsuarioPorEmail(email=email_do_usuario)

    usuario = barramento.manipulador(comando)
    if not usuario:
        raise exececao

    return usuario
