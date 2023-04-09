from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from tests.testes_integracao.test_unidade_de_trabalho import (
    inserir_exercicio,
    inserir_avaliacao,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


def test_cadastrar_avaliacao_retorna_422_caso_esteja_faltando_campo_obrigatorio(
    cliente: TestClient, mock_usuario_gen, mock_gerar_token_autenticado
):
    usuario_id = mock_usuario_gen(tipo_de_acesso='professor')

    _, token_autenticado = mock_gerar_token_autenticado(usuario_id=usuario_id)
    
    json = {
        "titulo": "Prova de matematica",
        "responsavel": usuario_id,
        "tipo_de_avaliacao": "avaliacao_ensino_medio",
    }

    avaliacao_id = cliente.post(
        "/avaliacao",
        json=json,
        headers={"Authorization": f"Bearer {token_autenticado}"},
    )
    
    assert avaliacao_id.status_code == 422


def test_cadastrar_avaliacao_retorna_201_para_usuario_professor(
    cliente: TestClient, 
    session: sessionmaker, 
    mock_usuario_gen,
    mock_gerar_token_autenticado
):  
    usuario_id = mock_usuario_gen(tipo_de_acesso='professor')
    _, token_autenticado = mock_gerar_token_autenticado(usuario_id=usuario_id)

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

    # cadastrar avaliacao
    requisicao = cliente.post(
        "/avaliacao",
        json={
            "titulo": "Prova de matematica",
            "responsavel": usuario_id,
            "tipo_avaliacao": "Avaliação Ensino Médio",
            "exercicios": [str(exercicio_id)],
        },
        headers={"Authorization": f"Bearer {token_autenticado}"},
    )

    assert requisicao.status_code == 201

    # verificar se a avaliacao realmente foi cadastrada
    avaliacao = session.execute("SELECT * FROM avaliacao").scalar()

    assert requisicao.json() == str(avaliacao)


def test_cadastrar_avaliacao_retorna_403_para_usuario_aluno(
    cliente: TestClient, 
    session: sessionmaker, 
    mock_gerar_token_autenticado
):  
    usuario_id, token_autenticado = mock_gerar_token_autenticado()

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

    # cadastrar avaliacao
    requisicao = cliente.post(
        "/avaliacao",
        json={
            "titulo": "Prova de matematica",
            "responsavel": usuario_id,
            "tipo_avaliacao": "Avaliação Ensino Médio",
            "exercicios": [str(exercicio_id)],
        },
        headers={"Authorization": f"Bearer {token_autenticado}"},
    )

    assert requisicao.status_code == 403
    assert requisicao.json() == {'detail': 'Usuário não autorizado a realizar esta ação!'}


def test_consultar_avaliacao_retorna_204_caso_nao_tenha_nada(cliente: TestClient):

    requisicao = cliente.get("/avaliacao")

    assert requisicao.status_code == 204


def test_consultar_avaliacao_retorna_200(
    cliente: TestClient, 
    session: sessionmaker,
    mock_usuario_gen,
    mock_gerar_token_autenticado
):
    usuario_id = mock_usuario_gen(tipo_de_acesso='professor')
    _, token_autenticado = mock_gerar_token_autenticado(usuario_id=usuario_id)

    # cadastrando avaliacao
    exercicio_id = inserir_exercicio(
        session,
        materia="matematica",
        assunto="aritmética",
        dificuldade="facil",
        enunciado="Quanto é dois mais dois?",
        resposta="4",
    )
    session.commit()

    avaliacao_id = cliente.post(
        "/avaliacao",
        json={
            "titulo": "Prova de matematica",
            "responsavel": usuario_id,
            "tipo_avaliacao": "Avaliação Ensino Médio",
            "exercicios": [str(exercicio_id)],
        },
        headers={"Authorization": f"Bearer {token_autenticado}"},
    )

    # testar o get
    requisicao = cliente.get("/avaliacao")

    assert requisicao.status_code == 200
    assert requisicao.json()[0].get("id") == avaliacao_id.json()