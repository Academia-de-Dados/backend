from garcom.contextos_de_negocio.identidade_e_acesso.servicos.visualizadores.usuarios import (
    consultar_usuarios, consultar_usuario_por_id
)
from garcom.contextos_de_negocio.identidade_e_acesso.servicos.executores.usuarios import (
    cadastrar_usuario
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario, BuscarTodosUsuarios, BuscarUsuarioPorId
)


MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS = {}

MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS = {
    BuscarTodosUsuarios: consultar_usuarios,
    BuscarUsuarioPorId: consultar_usuario_por_id,
    CriarUsuario: cadastrar_usuario
}

