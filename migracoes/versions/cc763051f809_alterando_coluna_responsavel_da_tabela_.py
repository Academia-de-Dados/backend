"""Alterando coluna responsavel da tabela avaliacao para ser um tipo uuid com chave estrangeira

Revision ID: cc763051f809
Revises: e00e769b7f32
Create Date: 2023-04-05 21:22:35.703557

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'cc763051f809'
down_revision = 'e00e769b7f32'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Altera a coluna responsavel da tabela avaliação e cria uma chave estrangeira.
    """
    
    # 1. cria uma coluna temporária para armazenar os ids dos usuários
    op.add_column(
        'avaliacao',
        sa.Column(
            'responsavel_id',
            UUID(as_uuid=True),
            sa.ForeignKey('usuarios.id'),
            index=True
        )
    )
    
    # 2. copia os ids dos usuários para a coluna temporária
    conexao = op.get_bind()

    conexao.execute(
        sa.text(
            'UPDATE avaliacao SET responsavel_id =' 
            ' (SELECT id FROM usuarios WHERE usuarios.nome = avaliacao.responsavel);'
        )
    )
    
    # 3. copia os dados da coluna temporária para a coluna responsavel
    op.execute(
        'Update avaliacao SET responsavel = '
        '(SELECT id FROM usuarios WHERE usuarios.id = avaliacao.responsavel_id)'
    )
    
    # 4. altera a coluna responsavel para ser do tipo uuid com chave estrangeira para tabela usuarios
    op.alter_column(
        'avaliacao', 
        'responsavel', 
        type_=UUID(as_uuid=True), 
        nullable=False, 
        postgresql_using='responsavel::uuid',
    )

    op.create_foreign_key(
        'fk_avaliacao_usuarios',
        'avaliacao',
        'usuarios',
        ['responsavel'],
        ['id']
    )

    # 5. remove a coluna temporária
    op.drop_column('avaliacao', 'responsavel_id')


def downgrade():
    # 1. Crie uma nova coluna para armazenar os nomes dos responsáveis
    op.add_column('avaliacao', sa.Column('responsavel_nome', sa.String(length=255), nullable=True))

    # 2. Execute um UPDATE para preencher a coluna 'responsavel_nome' com os nomes dos responsáveis com base nos IDs na tabela 'avaliacao'.
    conexao = op.get_bind()
    conexao.execute('UPDATE avaliacao SET responsavel_nome = (SELECT nome FROM usuarios WHERE usuarios.id = avaliacao.responsavel)')

    # 3. Remova a chave estrangeira e altere o tipo da coluna 'responsavel' para String
    op.drop_constraint('fk_avaliacao_usuarios', 'avaliacao', type_='foreignkey')
    op.alter_column('avaliacao', 'responsavel', type_=sa.String(length=255), nullable=False)

    # 4. copia os dados da coluna temporária para a coluna responsavel
    conexao.execute(
        'UPDATE avaliacao SET responsavel = '
        '(SELECT responsavel_nome FROM avaliacao WHERE avaliacao.id = id)'
    )

    # 6. Remova a coluna 'responsavel_nome'
    op.drop_column('avaliacao', 'responsavel_nome')

