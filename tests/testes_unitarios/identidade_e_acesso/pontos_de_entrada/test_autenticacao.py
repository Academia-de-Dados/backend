from pytest import raises
from freezegun import freeze_time
from datetime import datetime
from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.autenticacao import (
    pegar_usuario_ativo,
)
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import (
    UsuarioNaoAutorizado,
    TokenDeAcessoExpirado,
    UsuarioNaoEncontrado,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    criar_token_de_acesso,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso
)
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from tests.testes_unitarios.identidade_e_acesso.mock_identidade_e_acesso import (
    inserir_usuario,
)


def test_pegar_usuario_ativo_retorna_excecao_caso_token_seja_invalido():

    token = "sfjasodkjfsalkdfjlaskfjalskdfsadf"

    with raises(UsuarioNaoAutorizado) as exc_info:
        pegar_usuario_ativo(token)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Falha ao validar credenciais!"


def test_pegar_usuario_ativo_retorna_excecao_caso_email_do_usuario_seja_none():

    # criando token
    token = criar_token_de_acesso({"sub": None})

    with raises(UsuarioNaoAutorizado) as exc_info:
        pegar_usuario_ativo(token)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Falha ao validar credenciais!"


def test_pegar_usuario_ativo_retorno_excecao_caso_o_tempo_do_token_tenha_expirado():

    # criando token
    with freeze_time("2023-02-19"):
        token = criar_token_de_acesso({"sub": "othon@gmail.com"})

    with raises(TokenDeAcessoExpirado) as exc_info:
        with freeze_time("2023-02-22"):
            pegar_usuario_ativo(token)

    assert exc_info.value.detail == "Token de acesso expirado! Faça login novamente."
    assert exc_info.value.status_code == 403


def test_pegar_usuario_ativo_retorna_excecao_caso_usuario_nao_exista():

    # criando token
    token = criar_token_de_acesso({"sub": "othon@gmail.com"})

    with raises(UsuarioNaoEncontrado) as exc_info:
        pegar_usuario_ativo(token)

    assert exc_info.value.detail == "Usuário não encontrado!"
    assert exc_info.value.status_code == 404


def test_pegar_usuario_ativo_retorna_usuario_cadastrado(session):

    comando = CriarUsuario(
        nome=Nome("Teste Othon"),
        email=Email("othon@gmail.com"),
        senha="Testeautenticacao123",
        senha_verificacao="Testeautenticacao123",
        data_de_nascimento=datetime(1990, 1, 1),
        tipo_de_acesso=TipoDeAcesso.aluno,
    )

    id_usuario = inserir_usuario(session, comando)

    session.commit()

    # criando token
    token = criar_token_de_acesso({"sub": "othon@gmail.com"})

    usuario = pegar_usuario_ativo(token)

    assert usuario.id == id_usuario
