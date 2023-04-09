from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from tests.testes_integracao.test_unidade_de_trabalho import (
    inserir_exercicio,
)


def test_cadastrar_novo_exercicio_retorna_200(
    cliente: TestClient, session: sessionmaker
):
    resposta = cliente.post(
        "/exercicios",
        json={
            "assunto": "aritmética",
            "resposta": "4",
            "enunciado": "Quanto é dois mais dois?",
            "materia": "Matemática",
            "dificuldade": "Fácil",
        },
    )
    assert resposta.status_code == 201

    id_do_exercicio = resposta.json()

    # buscar os exercicios cadastrados
    exercicio = session.execute("SELECT * FROM exercicio").scalar()
    assert str(exercicio) == id_do_exercicio


def test_cadastrar_novo_exercicio_retorna_422_caso_esteja_faltando_campo_obrigatorio(
    cliente: TestClient,
):
    resposta = cliente.post(
        "/exercicios",
        json={
            "resposta": "4",
            "enunciado": "Quanto é dois mais dois?",
            "materia": "Matemática",
            "dificuldade": "Fácil",
        },
    )
    assert resposta.status_code == 422


def test_consultar_todos_exercicios_retorna_204_se_nao_existir_exercicios(
    cliente: TestClient,
):
    resposta = cliente.get("/exercicios")

    assert resposta.status_code == 204


def test_consultar_todos_exercicios_retorna_200(
    cliente: TestClient, session: sessionmaker
):
    # cadastrar exercicio
    exercicio_id = inserir_exercicio(
        session,
        materia="matematica",
        assunto="aritmética",
        dificuldade="facil",
        enunciado="Quanto é dois mais dois?",
        resposta="4",
    )
    session.commit()

    # buscar exercicio
    resposta = cliente.get("/exercicios")

    assert resposta.status_code == 200
    assert str(exercicio_id) == resposta.json()[0].get("id")