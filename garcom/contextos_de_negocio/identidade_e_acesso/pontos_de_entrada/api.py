from fastapi import APIRouter, Depends
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.modelos_pydantic.representacoes import (
    UsuarioConsulta,
    UsuarioDominio,
    UsuarioLogarApi,
    UsuarioLogado,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.barramento import BarramentoDeMensagens
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
    BuscarTodosUsuarios,
    BuscarUsuarioPorId,
    LogarUsuario,
)
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email, Nome
from garcom.contextos_de_negocio.barramento.identidade_e_acesso import (
    MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
)
from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.autenticacao import (
    pegar_usuario_ativo
)


router_usuarios = APIRouter(prefix="/usuarios", tags=["Identidade e Acesso"])


@router_usuarios.post("/signup", response_model=UsuarioId, status_code=200)
def cadastrar_usuario(usuario: UsuarioDominio):
    unidade_de_trabalho = UnidadeDeTrabalho()

    comando = CriarUsuario(
        nome=Nome(usuario.nome),
        email=Email(usuario.email),
        senha=usuario.senha,
        senha_verifacao=usuario.senha_verifacao,
        data_de_nascimento=usuario.data_de_nascimento,
    )
    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    )

    return barramento.manipulador(mensagem=comando)


@router_usuarios.post("/signin", response_model=UsuarioLogado)
def logar_usuario(usuario: UsuarioLogarApi):
    unidade_de_trabalho = UnidadeDeTrabalho()

    comando = LogarUsuario(
        email=usuario.email,
        senha=usuario.senha,
    )

    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    )

    return barramento.manipulador(mensagem=comando)


@router_usuarios.get("/", response_model=list[UsuarioConsulta], status_code=200)
def consultar_usuarios(usuario_atual: Usuario = Depends(pegar_usuario_ativo)):
    unidade_de_trabalho = UnidadeDeTrabalho()

    comando = BuscarTodosUsuarios()
    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    )

    return barramento.manipulador(mensagem=comando)


@router_usuarios.get("/{id}", response_model=UsuarioConsulta)
def consultar_usuario_por_id(id: UsuarioId, usuario_atual: Usuario = Depends(pegar_usuario_ativo)):
    unidade_de_trabalho = UnidadeDeTrabalho()

    comando = BuscarUsuarioPorId(usuario_id=id)
    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS,
    )

    return barramento.manipulador(mensagem=comando)