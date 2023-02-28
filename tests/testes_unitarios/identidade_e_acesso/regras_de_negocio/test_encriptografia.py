from garcom.contextos_de_negocio.identidade_e_acesso.dominio.regras_de_negocio.encriptografia import (
    verificar_senha,
    gerar_senha_encriptografada,
    criar_token_de_acesso,
    validar_token_de_acesso,
)


def test_encriptografar_senha():

    senha = "macacodepilado"

    senha_hash = gerar_senha_encriptografada(senha)

    assert senha_hash != senha
    assert verificar_senha(senha, senha_hash)


def test_gerar_token_jwt():

    dado_de_acesso = {"sub": "othon@gmail.com"}
    token = criar_token_de_acesso(dado_de_acesso)

    assert token
    assert validar_token_de_acesso(token).sub == "othon@gmail.com"
