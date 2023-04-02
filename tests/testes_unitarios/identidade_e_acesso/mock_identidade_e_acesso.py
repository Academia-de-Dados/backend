from sqlalchemy.orm import sessionmaker
from datetime import datetime
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.comandos.usuario import (
    CriarUsuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


def inserir_usuario(session: sessionmaker, comando: CriarUsuario):

    usuario_id = UsuarioId()
    session.execute(
        "INSERT INTO usuarios (id, nome, senha, email, data_de_nascimento, ativo, tipo_de_acesso, criado_em, ultima_modificacao)"
        "VALUES (:id, :nome, :senha, :email, :data_de_nascimento, :ativo, :tipo_de_acesso, :criado_em, :ultima_modificacao)",
        dict(
            id=usuario_id,
            nome=comando.nome,
            senha=comando.senha,
            email=comando.email,
            data_de_nascimento=comando.data_de_nascimento,
            ativo=True,
            tipo_de_acesso=comando.tipo_de_acesso.value,
            criado_em=datetime.now(),
            ultima_modificacao=datetime.now(),
        ),
    )

    return usuario_id
