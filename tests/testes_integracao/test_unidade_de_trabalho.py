from datetime import datetime
from sqlite3 import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from garcom.adaptadores.dominio import Dominio
from garcom.adaptadores.tipos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)

def inserir_exercicio(
    session: sessionmaker, 
    materia: str,
    assunto: str,
    dificuldade:str,
    enunciado: str,
) -> str:

    exercicio_id = ExercicioId()
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


def buscar_id_do_exercicio(
    session: sessionmaker, materia: str, assunto: str
) -> ExercicioId:

    exercicio = session.execute(
        "SELECT * FROM exercicio WHERE materia=:materia AND assunto=:assunto",
        dict(materia=materia, assunto=assunto)
    )

    return exercicio.scalar()


def buscar_exercicio_e_retornar_objeto(session: sessionmaker):
    return session.execute(select(Exercicio)).first()[0]


def test_inserir_e_buscar_dados_utilizando_query_sql(session: sessionmaker):

    exercicio_id = inserir_exercicio(
        session, 'Fisica', 'Mecanica', 'Qual a primeira Lei de Newton', 'Facil'
    )
    session.commit()

    exercicio = buscar_id_do_exercicio(session,'Fisica', 'Mecanica')

    assert exercicio == exercicio_id


def test_uow_pode_recuperar_um_exercicio_do_banco_de_dados(
    session, session_factory
):
    materia = 'Fisica'
    assunto = 'Quântica'
    dificuldade = 'Média'
    enunciado = 'Qual o primeiro esferico harmonico de um eletron?'

    # Inserindo exercicio
    exericio_id = inserir_exercicio(session, materia, assunto, dificuldade, 
        enunciado,
    )
    session.commit()

    # Testando se a unidade de trabalho busca o exercicio
    unidade = UnidadeDeTrabalho(session_factory)
    with unidade(Dominio.exercicios) as uow:
        exercicio = uow.repo_consulta.consultar_por_id(exericio_id)
    
    assert exercicio.id == exericio_id
    assert exercicio.materia == materia
    assert exercicio.assunto == assunto
    assert exercicio.dificuldade == dificuldade
    assert exercicio.enunciado == enunciado


def test_uow_pode_inserir_um_exercicio_no_banco_de_dados(
    session, session_factory
):
    # criando um exercicio
    materia = 'Fisica'
    assunto = 'Quântica'
    dificuldade = 'Média'
    enunciado = 'Qual o primeiro esferico harmonico de um eletron?'

    exercicio = Exercicio(
        materia=materia,
        assunto=assunto,
        dificuldade=dificuldade,
        enunciado=enunciado
    )
    exercicio_id = exercicio.id

    # Usando a unidade de trabalho para inserir no banco de dados
    unidade = UnidadeDeTrabalho(session_factory)

    with unidade(Dominio.exercicios) as uow:
        try:
            uow.repo_dominio.adicionar(exercicio)
            uow.commit()
        
        except IntegrityError:
            uow.rollback()
    
    # Fazendo uma busca pra verificar se foi inserido mesmo
    exercicio_recuperado = buscar_exercicio_e_retornar_objeto(session)
    
    assert exercicio_recuperado.materia == materia
    assert exercicio_recuperado.assunto == assunto
    assert exercicio_recuperado.dificuldade == dificuldade
    assert exercicio_recuperado.enunciado == enunciado
    assert exercicio_recuperado.id == exercicio_id