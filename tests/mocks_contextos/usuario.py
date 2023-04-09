from pytest import fixture


@fixture(scope="function")
def mock_usuario_gen(cliente, session):
    def criar_mock(
        nome: str = "Usuario Teste",
        email: str = "usuarioteste@gmail.com",
        senha: str = "SenhaTeste123",
        senha_verificacao: str = "SenhaTeste123",
        data_de_nascimento: str = "1998-03-12T00:00:00.901Z",
        tipo_de_acesso: str = "aluno",
    ):
        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "senha_verificacao": senha_verificacao,
            "data_de_nascimento": data_de_nascimento,
            "tipo_de_acesso": tipo_de_acesso,
        }

        resposta = cliente.post("/usuarios/signup", json=usuario)

        assert resposta.status_code == 200

        return resposta.json()

    yield criar_mock


@fixture(scope="function")
def mock_gerar_token_autenticado(mock_usuario_gen, cliente, session):
    def criar_mock(usuario_id: str = None):
        if not usuario_id:
            usuario_id = mock_usuario_gen()

        dados = {
            "username": "usuarioteste@gmail.com",
            "password": "SenhaTeste123",
            "grant_type": "password",
        }

        resposta = cliente.post(
            "/usuarios/signin",
            data=dados,
            headers={"content-type": "application/x-www-form-urlencoded"},
        )

        assert resposta.status_code == 200

        return usuario_id, resposta.json()["access_token"]

    yield criar_mock
