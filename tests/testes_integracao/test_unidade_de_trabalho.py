from datetime import datetime
from sqlite3 import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from garcom.adaptadores.dominio import Dominio
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId
from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (  # noqa
    Exercicio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.eventos.estrutura_de_provas import (
    EnviarEmail,
)


def inserir_exercicio(
    session: sessionmaker,
    materia: str,
    assunto: str,
    dificuldade: str,
    enunciado: str,
    resposta: str,
) -> str:

    exercicio_id = ExercicioId()
    session.execute(
        "INSERT INTO exercicio (id, materia, assunto, enunciado, dificuldade, resposta, multipla_escolha, criado_em, ultima_modificacao)"
        "VALUES (:id, :materia, :assunto, :enunciado, :dificuldade, :resposta, :multipla_escolha, :criado_em, :ultima_modificacao)",
        dict(
            id=exercicio_id,
            materia=materia,
            assunto=assunto,
            dificuldade=dificuldade,
            enunciado=enunciado,
            resposta=resposta,
            multipla_escolha=False,
            criado_em=datetime.now(),
            ultima_modificacao=datetime.now(),
        ),
    )
    return exercicio_id


def inserir_avaliacao(
    session: sessionmaker,
    titulo: str,
    responsavel: str,
    tipo_de_avaliacao: TipoDeAvaliacao,
):
    avaliacao_id = ExercicioId()
    session.execute(
        "INSERT INTO avaliacao (id, titulo, responsavel, tipo_de_avaliacao, criado_em, ultima_modificacao)"
        "VALUES (:id, :titulo, :responsavel, :tipo_de_avaliacao, :criado_em, :ultima_modificacao)",
        dict(
            id=avaliacao_id,
            titulo=titulo,
            responsavel=responsavel,
            tipo_de_avaliacao=tipo_de_avaliacao,
            criado_em=datetime.now(),
            ultima_modificacao=datetime.now(),
        ),
    )

    return avaliacao_id


def buscar_id_do_exercicio(
    session: sessionmaker, materia: str, assunto: str
) -> ExercicioId:

    exercicio = session.execute(
        "SELECT * FROM exercicio WHERE materia=:materia AND assunto=:assunto",
        dict(materia=materia, assunto=assunto),
    )

    return exercicio.scalar()


def buscar_exercicio_e_retornar_objeto(session: sessionmaker):
    return session.execute(select(Exercicio)).first()[0]


def test_inserir_e_buscar_dados_utilizando_query_sql(session: sessionmaker):

    exercicio_id = inserir_exercicio(
        session=session,
        materia="fisica",
        assunto="Mecanica",
        dificuldade="facil",
        enunciado="Qual a primeira Lei de Newton",
        resposta="Lei da inernica",
    )
    session.commit()

    exercicio = buscar_id_do_exercicio(session, "fisica", "Mecanica")

    assert str(exercicio) == str(exercicio_id)


def test_uow_pode_recuperar_um_exercicio_do_banco_de_dados(session, session_factory):
    materia = "fisica"
    assunto = "Quântica"
    dificuldade = "media"
    enunciado = "Qual o primeiro esferico harmonico de um eletron?"
    resposta = "Esfera simples."

    # Inserindo exercicio
    exericio_id = inserir_exercicio(
        session=session,
        materia=materia,
        assunto=assunto,
        dificuldade=dificuldade,
        enunciado=enunciado,
        resposta=resposta,
    )
    session.commit()

    # Testando se a unidade de trabalho busca o exercicio
    unidade = UnidadeDeTrabalho(session_factory)
    with unidade(Dominio.exercicios) as uow:
        exercicio = uow.repo_consulta.consultar_por_id(exericio_id)

    assert exercicio.id == exericio_id
    assert exercicio.materia == "Física"
    assert exercicio.assunto == assunto
    assert exercicio.dificuldade == "Média"
    assert exercicio.enunciado == enunciado


def test_uow_pode_inserir_um_exercicio_no_banco_de_dados(session, session_factory):
    # criando um exercicio
    materia = "Física"
    assunto = "Quântica"
    dificuldade = "Média"
    enunciado = "Qual o primeiro esferico harmonico de um eletron?"
    resposta = "Esferico simples"

    exercicio = Exercicio(
        materia=materia,
        assunto=assunto,
        dificuldade=dificuldade,
        enunciado=enunciado,
        resposta=resposta,
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


def test_uow_pode_coletar_eventos_dos_agregados(session, session_factory):

    # criando um exercicio
    materia = "Física"
    assunto = "Quântica"
    dificuldade = "Média"
    enunciado = "Qual o primeiro esferico harmonico de um eletron?"
    resposta = "Esferico simples"

    exercicio = Exercicio(
        materia=materia,
        assunto=assunto,
        dificuldade=dificuldade,
        enunciado=enunciado,
        resposta=resposta,
    )

    # Usando a unidade de trabalho para inserir no banco de dados
    unidade = UnidadeDeTrabalho(session_factory)

    with unidade(Dominio.exercicios) as uow:
        try:
            evento = EnviarEmail(mensagem="Olá Mundo!")
            exercicio.adicionar_evento(evento)
            uow.repo_dominio.adicionar(exercicio)
            uow.commit()

        except IntegrityError:
            uow.rollback()

    eventos = list(unidade.coletar_novos_eventos())

    assert evento in eventos
