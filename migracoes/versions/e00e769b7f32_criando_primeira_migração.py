"""Criando primeira migração

Revision ID: e00e769b7f32
Revises: 
Create Date: 2023-04-02 09:04:47.639223

"""
from alembic import op
import sqlalchemy as sa
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.objeto_de_valor.tipo_de_acesso import (
    TipoDeAcesso
)

# revision identifiers, used by Alembic.
revision = 'e00e769b7f32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Função que aplica a migração.
    """
    # cria o enum TipoDeAcesso no banco de dados antes de executar a migrations
    op.execute("CREATE TYPE tipodeacesso AS ENUM ('professor', 'aluno', 'administrador')")
    
    # cria a coluna tipo_de_acesso na tabela usuarios
    op.add_column(
        'usuarios',
        sa.Column(
            'tipo_de_acesso', 
            sa.Enum('professor', 'aluno', 'administrador', name='tipodeacesso'), 
            nullable=False,
            server_default='aluno'
        )
    )


def downgrade() -> None:
    """
    Função que desaplica a migração.
    """
    # remove a coluna tipo_de_acesso da tabela usuarios
    op.drop_column('usuarios', 'tipo_de_acesso')

    # remove o enum TipoDeAcesso do banco de dados
    op.execute("DROP TYPE tipodeacesso")