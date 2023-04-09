from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.permissoes import (
    usuario_administrador, usuario_professor, ExcessaoSemPermissao
)
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import (
    UsuarioSemPermissaoNecessaria,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from datetime import datetime
from freezegun import freeze_time
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso,
)
from pytest import raises, mark


@mark.parametrize(
    'tipo_de_acesso, funcao',
    [
        (TipoDeAcesso.administrador, usuario_administrador), 
        (TipoDeAcesso.professor, usuario_professor)
    ]
)
@freeze_time('2023-04-09')
def test_permissoes_retorna_usuario(tipo_de_acesso, funcao):

    comando = CriarUsuario(
        nome=Nome('Usuario Teste'),
        email=Email('teste@gmail.com'),
        senha='Senhateste123',
        senha_verificacao='Senhateste123',
        data_de_nascimento=datetime.now(),
        tipo_de_acesso=tipo_de_acesso,
    )

    usuario = Usuario.criar_usuario(comando)

    usuario_adm = funcao(usuario)
    
    assert usuario_adm == usuario


@mark.parametrize(
    'tipo_de_acesso, funcao',
    [
        (TipoDeAcesso.aluno, usuario_administrador), 
        (TipoDeAcesso.aluno, usuario_professor)
    ]
)
@freeze_time('2023-04-09')
def test_permissoes_levanta_excecao(
    tipo_de_acesso, funcao
):

    comando = CriarUsuario(
        nome=Nome('Usuario Teste'),
        email=Email('teste@gmail.com'),
        senha='Senhateste123',
        senha_verificacao='Senhateste123',
        data_de_nascimento=datetime.now(),
        tipo_de_acesso=tipo_de_acesso,
    )

    usuario = Usuario.criar_usuario(comando)
    
    with raises(Exception) as exinfo:
        funcao(usuario)

    assert exinfo.type == UsuarioSemPermissaoNecessaria
    assert exinfo.value == ExcessaoSemPermissao