from datetime import datetime
from sqlalchemy.orm import sessionmaker
from garcom.adaptadores.tipos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho


def inserir_exercicio(
    session: sessionmaker, 
    materia: str,
    assunto: str,
    dificuldade:str,
    enunciado: str,
) -> str:

    exercicio_id = str(ExercicioId())
    session.execute(
        "INSERT INTO exercicio (id, materia, assunto, enunciado, dificuldade, multipla_escolha, criado_em, ultima_modificacao)"
        "VALUES (:id, :materia, :assunto, :enunciado, :dificuldade, :multipla_escolha, :criado_em, :ultima_modificacao)",
        dict(
            id=exercicio_id, materia=materia, assunto=assunto, 
            dificuldade=dificuldade, enunciado=enunciado, multipla_escolha=False,
            criado_em=datetime.now(), ultima_modificacao=datetime.now()
        )
    )
    return exercicio_id


def buscar_exercicio(
    session: sessionmaker, materia: str, assunto: str
) -> ExercicioId:

    exercicio = session.execute(
        "SELECT * FROM exercicio WHERE materia=:materia AND assunto=:assunto",
        dict(materia=materia, assunto=assunto)
    )

    return exercicio.scalar()


def test_inserir_e_buscar_dados_utilizando_query_sql(session: sessionmaker):

    exercicio_id = inserir_exercicio(
        session, 'Fisica', 'Mecanica', 'Qual a primeira Lei de Newton', 'Facil'
    )
    session.commit()

    exercicio = buscar_exercicio(session,'Fisica', 'Mecanica')

    assert str(exercicio) == exercicio_id