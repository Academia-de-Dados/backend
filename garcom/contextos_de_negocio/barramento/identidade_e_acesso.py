from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    BuscarTodosUsuarios,
    BuscarUsuarioPorEmail,
    BuscarUsuarioPorId,
    CriarUsuario,
    LogarUsuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.servicos.executores.usuarios import (
    cadastrar_usuario,
)
from garcom.contextos_de_negocio.identidade_e_acesso.servicos.visualizadores.usuarios import (
    consultar_usuario_por_email,
    consultar_usuario_por_id,
    consultar_usuarios,
    login_de_usuario,
)

MANIPULADORES_IDENTIDADE_E_ACESSO_EVENTOS = {}

MANIPULADORES_IDENTIDADE_E_ACESSO_COMANDOS = {
    BuscarTodosUsuarios: consultar_usuarios,
    BuscarUsuarioPorId: consultar_usuario_por_id,
    BuscarUsuarioPorEmail: consultar_usuario_por_email,
    CriarUsuario: cadastrar_usuario,
    LogarUsuario: login_de_usuario,
}
