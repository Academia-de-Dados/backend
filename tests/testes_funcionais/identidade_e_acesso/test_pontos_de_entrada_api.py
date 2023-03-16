from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from pytest import mark


def test_cadastrar_usuario(cliente: TestClient, session: sessionmaker):

    resposta = cliente.post(
        "/usuarios/signup",
        json={
            "nome": "Cairon Henrique",
            "email": "cairon@gmail.com",
            "senha": "Cairon123",
            "senha_verifacao": "Cairon123",
            "data_de_nascimento": "1998-03-12T00:00:00.901Z",
        }
    )
    
    assert resposta.status_code == 200