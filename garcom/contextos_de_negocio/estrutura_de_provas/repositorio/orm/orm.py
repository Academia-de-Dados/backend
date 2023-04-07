from sqlalchemy import ARRAY, Boolean, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from garcom.adaptadores.orm.orm import DbColumn, DbTable, mapper, metadata
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.avaliacao import (
    Avaliacao,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio,
)

from .....adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao
from .....adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade,
    Materia,
)

exercicios = DbTable(
    'exercicio',
    metadata,
    DbColumn.uuid_primary_key('id'),
    DbColumn('materia', Enum(Materia), nullable=False, index=True),
    DbColumn('assunto', String(length=255), nullable=False, index=True),
    DbColumn('enunciado', Text, nullable=False),
    DbColumn('multipla_escolha', Boolean, nullable=False),
    DbColumn('dificuldade', Enum(Dificuldade), nullable=False),
    DbColumn('resposta', Text, nullable=False),
    DbColumn('alternativas', ARRAY(String), nullable=True),
    DbColumn('origem', String(length=255), nullable=True),
    DbColumn('data_lancamento', DateTime, nullable=True),
    DbColumn('imagem_enunciado', String(length=255), nullable=True),
    DbColumn('imagem_resposta', String(length=255), nullable=True),
)

avaliacao = DbTable(
    'avaliacao',
    metadata,
    DbColumn.uuid_primary_key('id'),
    DbColumn('titulo', String(length=255), nullable=False, index=True),
    DbColumn(
        'responsavel',
        UUID(as_uuid=True),
        ForeignKey('usuarios.id'),
        nullable=False,
        index=True,
    ),
    DbColumn('tipo_de_avaliacao', Enum(TipoDeAvaliacao), nullable=False),
)

exercicios_prova = DbTable(
    'exercicios_prova',
    metadata,
    DbColumn('id_avaliacao', ForeignKey('avaliacao.id'), primary_key=True),
    DbColumn('id_exercicio', ForeignKey('exercicio.id'), primary_key=True),
)


def start_mappers() -> None:
    """
    Método para começar o mapeamento.

    Este método deveria iniciar o mapeamento do banco de dados,
    atualmente ele não faz isso e eu ainda não descobri o porque.
    """
    mapper.map_imperatively(Exercicio, exercicios)
    mapper.map_imperatively(
        Avaliacao,
        avaliacao,
        properties={
            'exercicios': relationship(
                Exercicio,
                secondary=exercicios_prova,
                lazy='subquery',
                collection_class=set,
            ),
        },
    )
