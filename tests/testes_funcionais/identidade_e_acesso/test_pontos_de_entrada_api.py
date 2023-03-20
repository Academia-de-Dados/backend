from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    validar_token_de_acesso,
)


def test_cadastrar_usuario(cliente: TestClient, session: sessionmaker):

    resposta = cliente.post(
        "/usuarios/signup",
        json={
            "nome": "Cairon Henrique",
            "email": "cairon@gmail.com",
            "senha": "Cairon123",
            "senha_verificacao": "Cairon123",
            "data_de_nascimento": "1998-03-12T00:00:00.901Z",
        },
    )

    usuario_id = session.execute("SELECT * FROM usuarios").scalar()

    assert resposta.status_code == 200
    assert resposta.json() == str(usuario_id)


def test_logar_usuario(cliente: TestClient, session: sessionmaker):

    cadastro = cliente.post(
        "/usuarios/signup",
        json={
            "nome": "Cairon Henrique",
            "email": "cairon@gmail.com",
            "senha": "Cairon123",
            "senha_verificacao": "Cairon123",
            "data_de_nascimento": "1998-03-12T00:00:00.901Z",
        },
    )

    assert cadastro.status_code == 200

    logar = cliente.post(
        "/usuarios/signin",
        data={
            "username": "cairon@gmail.com",
            "password": "Cairon123",
            "grant_type": "password",
        },
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    assert logar.status_code == 200
    assert logar.json()["usuario"]["nome"] == "Cairon Henrique"
    assert logar.json()["usuario"]["email"] == "cairon@gmail.com"
    assert logar.json()["usuario"]["ativo"] == True

    token = logar.json()["access_token"]
    validar_token = validar_token_de_acesso(token)

    assert validar_token.sub == "cairon@gmail.com"


def test_consultar_usuarios(
    cliente: TestClient,
    session: sessionmaker,
    mock_gerar_token_autenticado,
):
    _, token = mock_gerar_token_autenticado()

    usuarios = cliente.get("/usuarios/", headers={"Authorization": "Bearer " + token})

    assert usuarios.status_code == 200
    assert isinstance(usuarios.json(), list)
    assert len(usuarios.json()) == 1
    assert usuarios.json()[0]["nome"] == "Usuario Teste"
    assert usuarios.json()[0]["email"] == "usuarioteste@gmail.com"


def test_consultar_usuario_por_id(
    cliente: TestClient,
    session: sessionmaker,
    mock_gerar_token_autenticado,
):
    id_usuario, token = mock_gerar_token_autenticado()

    usuarios = cliente.get(
        f"/usuarios/{id_usuario}", headers={"Authorization": "Bearer " + token}
    )

    assert usuarios.status_code == 200
    assert usuarios.json()["nome"] == "Usuario Teste"
    assert usuarios.json()["email"] == "usuarioteste@gmail.com"
