from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)
from garcom.adaptadores.dominio import Dominio


def cadastrar_usuario(
    comando: CriarUsuario, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
) -> UsuarioId:

    usuario = Usuario.cadrastar_novo_usuario(comando)
    usuario_id = usuario.id

    with unidade_de_trabalho(Dominio.usuarios) as uow:
        try:
            # usuario.adicionar_evento()
            uow.repo_dominio.adicionar(usuario)
            uow.commit()

        except Exception as e:
            uow.rollback()
            raise e

    return usuario_id
