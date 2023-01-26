from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
    BuscarUsuarioPorEmail,
)
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)
from garcom.adaptadores.dominio import Dominio
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    gerar_senha_encriptografada,
)
from garcom.adaptadores.tipos_nao_primitivos.usuario import Senha
from garcom.contextos_de_negocio.identidade_e_acesso.excecoes import (
    SenhasDiferentes,
    EmailJaCadastrado,
)
from garcom.contextos_de_negocio.identidade_e_acesso.servicos.visualizadores.usuarios import (
    consultar_usuario_por_email,
)


def cadastrar_usuario(
    comando: CriarUsuario, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
) -> UsuarioId:

    # verificar se usuario já existe
    usuario = consultar_usuario_por_email(BuscarUsuarioPorEmail(comando.email))
    if usuario:
        raise EmailJaCadastrado(
            status_code=400, detail="Email já cadastrado no sistema!"
        )

    # verificar se usuario digitou a mesma senha duas vezes
    senha = Senha(comando.senha)
    senha_verificacao = Senha(comando.senha_verifacao)
    if senha != senha_verificacao:
        raise SenhasDiferentes(
            status_code=400, detail="Senhas diferentes! Favor digite novamente."
        )

    comando.senha = gerar_senha_encriptografada(senha)
    comando.senha_verifacao = gerar_senha_encriptografada(senha_verificacao)

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
