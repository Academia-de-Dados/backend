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
)


def consultar_usuarios(
    comando: BuscarTodosUsuarios, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
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
