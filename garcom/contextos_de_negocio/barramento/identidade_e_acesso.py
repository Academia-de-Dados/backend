from garcom.contextos_de_negocio.identidade_e_acesso.servicos.visualizadores.usuarios import (
    consultar_usuarios,
    consultar_usuario_por_id,
    login_de_usuario,
    consultar_usuario_por_email,
)
from garcom.contextos_de_negocio.identidade_e_acesso.servicos.executores.usuarios import (
    cadastrar_usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
    BuscarTodosUsuarios,
    BuscarUsuarioPorId,
    LogarUsuario,
    BuscarUsuarioPorEmail,
)


MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS = {}

MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS = {
    BuscarTodosUsuarios: consultar_usuarios,
    BuscarUsuarioPorId: consultar_usuario_por_id,
    BuscarUsuarioPorEmail: consultar_usuario_por_email,
    CriarUsuario: cadastrar_usuario,
    LogarUsuario: login_de_usuario,
}
