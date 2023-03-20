from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from datetime import datetime
from garcom.adaptadores.tipos_nao_primitivos.usuario import NomeInvalido, EmailInvalido
from pytest import raises


def test_criar_agregado_usuario():

    comando = CriarUsuario(
        nome=Nome("Teste Identidade e Acesso"),
        email=Email("teste_identidade@gmail.com"),
        data_de_nascimento=datetime(1998, 3, 12),
        senha="Teste",
        senha_verificacao="Teste",
    )

    agregado = Usuario.criar_usuario(comando)

    assert agregado.nome == "Teste Identidade e Acesso"
    assert agregado.email == "teste_identidade@gmail.com"
    assert isinstance(agregado, Usuario)
    assert isinstance(agregado.id, UsuarioId)


def test_criar_agregado_usuario_retorna_erro_caso_nome_seja_invalido():

    with raises(NomeInvalido) as exec_info:
        comando = CriarUsuario(
            nome=Nome("Teste"),
            email=Email("teste_identidade@gmail.com"),
            data_de_nascimento=datetime(1998, 3, 12),
            senha="Teste",
            senha_verificacao="Teste",
        )

        Usuario.criar_usuario(comando)

    assert str(exec_info.value) == "Nome muito curto, por favor insira mais caracters!"


def test_criar_agregado_usuario_retorna_erro_caso_email_seja_invalido():

    with raises(EmailInvalido) as exc_info:
        comando = CriarUsuario(
            nome=Nome("Teste Identidade e Acesso"),
            email=Email("teste_identidade"),
            data_de_nascimento=datetime(1998, 3, 12),
            senha="Teste",
            senha_verificacao="Teste",
        )
        Usuario.criar_usuario(comando)

    assert str(exc_info.value) == "Formatado de email inválido!"
