from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from tests.testes_integracao.test_unidade_de_trabalho import (
    inserir_exercicio,
    inserir_avaliacao
)
from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao


def test_cadastrar_novo_exercicio_retorna_200(
    cliente: TestClient, session: sessionmaker
):
    resposta = cliente.post(
        '/exercicios',
        json={
            'assunto':'aritmética', 
            'resposta': '4', 
            'enunciado': 'Quanto é dois mais dois?',
            'materia': 'Matemática',
            'dificuldade': 'Fácil'
        }
    )
    assert resposta.status_code == 201

    id_do_exercicio = resposta.json()

    # buscar os exercicios cadastrados
    exercicio = session.execute("SELECT * FROM exercicio").scalar()
    assert str(exercicio) == id_do_exercicio


def test_cadastrar_novo_exercicio_retorna_422_caso_esteja_faltando_campo_obrigatorio(
    cliente: TestClient
):
    resposta = cliente.post(
        '/exercicios',
        json={
            'resposta': '4', 
            'enunciado': 'Quanto é dois mais dois?',
            'materia': 'Matemática',
            'dificuldade': 'Fácil'
        }
    )
    assert resposta.status_code == 422


def test_consultar_todos_exercicios_retorna_204_se_nao_existir_exercicios(
    cliente: TestClient
):
    resposta = cliente.get('/exercicios')

    assert resposta.status_code == 204


def test_consultar_todos_exercicios_retorna_200(
    cliente: TestClient, session: sessionmaker
):
    # cadastrar exercicio
    exercicio_id = inserir_exercicio(
        session, 
        materia='matematica', 
        assunto='aritmética', 
        dificuldade='facil', 
        enunciado='Quanto é dois mais dois?',
        resposta='4',
    )
    session.commit()
    
    # buscar exercicio
    resposta = cliente.get('/exercicios')
    
    assert resposta.status_code == 200
    assert str(exercicio_id) == resposta.json()[0].get('id')


def test_cadastrar_avaliacao_retorna_422_caso_esteja_faltando_campo_obrigatorio(
    cliente: TestClient
):
    avaliacao_id = cliente.post(
        '/avaliacao',
        json={
            'titulo': 'Prova de matematica',
            'responsavel': 'Othon',
            'tipo_de_avaliacao': 'avaliacao_ensino_medio',
        }
    )
    
    assert avaliacao_id.status_code == 422
    

def test_cadastrar_avaliacao_retorna_201(
    cliente: TestClient, session: sessionmaker
):
    # cadastrar exercicio
    exercicio_id = inserir_exercicio(
        session, 
        materia='matematica', 
        assunto='aritmética', 
        dificuldade='facil', 
        enunciado='Quanto é dois mais dois?',
        resposta='4',
    )
    session.commit()

    # cadastrar avaliacao
    requisicao = cliente.post(
        '/avaliacao',
        json={
            'titulo': 'Prova de matematica',
            'responsavel': 'Othon',
            'tipo_avaliacao': 'Avaliação Ensino Médio',
            'exercicios': [str(exercicio_id)]
        }
    )
    
    assert requisicao.status_code == 201
    
    # verificar se a avaliacao realmente foi cadastrada
    avaliacao = session.execute("SELECT * FROM avaliacao").scalar()
    
    assert requisicao.json() == str(avaliacao)


def test_consultar_avaliacao_retorna_204_caso_nao_tenha_nada(cliente: TestClient):
    
    requisicao = cliente.get('/avaliacao')
    
    assert requisicao.status_code == 204


def test_consultar_avaliacao_retorna_200(
    cliente: TestClient, session: sessionmaker
):
    
    #cadastrando avaliacao
    exercicio_id = inserir_exercicio(
        session, 
        materia='matematica', 
        assunto='aritmética', 
        dificuldade='facil', 
        enunciado='Quanto é dois mais dois?',
        resposta='4',
    )
    session.commit()
    
    avaliacao_id = cliente.post(
        '/avaliacao',
        json={
            'titulo': 'Prova de matematica',
            'responsavel': 'Othon',
            'tipo_avaliacao': 'Avaliação Ensino Médio',
            'exercicios': [str(exercicio_id)]
        }
    )

    # testar o get
    requisicao = cliente.get('/avaliacao')

    assert requisicao.status_code == 200
    assert requisicao.json()[0].get('id') == avaliacao_id.json()
