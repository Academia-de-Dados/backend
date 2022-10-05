from wsgiref import headers
from fastapi.testclient import TestClient


def test_consultar_todos_exercicios_retorna_404_se_nao_existir_exercicios(
    cliente: TestClient
):
    resposta = cliente.get('/exercicios', headers={'accept': 'application/json'})
    breakpoint()
    assert resposta.status_code == 200