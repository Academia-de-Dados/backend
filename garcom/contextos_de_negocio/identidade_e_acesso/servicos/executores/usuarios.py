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
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    gerar_senha_encriptografada, 
)

#TODO: fazer query por email para verificar se já existe usuario com esse email

def cadastrar_usuario(
    comando: CriarUsuario, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
) -> UsuarioId:

    comando.senha = gerar_senha_encriptografada(comando.senha)
    comando.senha_verifacao = gerar_senha_encriptografada(comando.senha_verifacao)
    
    usuario = Usuario.criar_usuario(comando)
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
