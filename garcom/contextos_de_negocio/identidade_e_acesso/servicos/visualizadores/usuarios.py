from garcom.adaptadores.dominio import Dominio
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    BuscarTodosUsuarios,
    BuscarUsuarioPorId,
    BuscarUsuarioPorEmail,
    LogarUsuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    verificar_senha, criar_token_de_acesso
)
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import SenhaIncorreta
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.entidades.usuario import (
    UsuarioLogado, UsuarioLeitura
)
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome


def consultar_usuarios(
    _: BuscarTodosUsuarios, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
) -> list[Usuario]:
    with unidade_de_trabalho(Dominio.usuarios) as uow:
        usuarios = uow.repo_consulta.consultar_todos()

    return usuarios


def consultar_usuario_por_id(
    comando: BuscarUsuarioPorId,
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> Usuario:
    with unidade_de_trabalho(Dominio.usuarios) as uow:
        usuario = uow.repo_consulta.consultar_por_id(comando.usuario_id)

    return usuario


def consultar_usuario_por_email(
    comando: BuscarUsuarioPorEmail,
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> Usuario:
    with unidade_de_trabalho(Dominio.usuarios) as uow:
        usuario = uow.repo_consulta.consultar_por_email(comando.email)
    
    return usuario


def login_de_usuario(
    comando: LogarUsuario,
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
) -> UsuarioLogado:

    email = comando.email
    senha = comando.senha
    
    comando_buscar_por_email = BuscarUsuarioPorEmail(
        email=email
    )
    
    usuario = consultar_usuario_por_email(
        comando_buscar_por_email, unidade_de_trabalho
    )
    
    validar_senha = verificar_senha(
        senha=senha, senha_encriptada=usuario.senha
    )
    
    if not validar_senha:
        raise SenhaIncorreta(
            status_code=400,
            detail='Senha informada está incorreta, por favor digite a senha certa!'
        )
    
    token_de_acesso = criar_token_de_acesso(
        dado_de_acesso={'sub': usuario.email}
    )
    
    usuario = UsuarioLeitura(
        nome=Nome(usuario.nome),
        email=Email(usuario.email),
        ativo=usuario.ativo,
        data_de_nascimento=usuario.data_de_nascimento,
    )
    
    return UsuarioLogado(
        usuario=usuario,
        token_de_acesso=token_de_acesso,
    )