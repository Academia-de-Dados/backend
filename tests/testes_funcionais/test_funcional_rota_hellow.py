from fastapi.testclient import TestClient


def test_rota_hellow(cliente: TestClient):
    
    resposta = cliente.get('/')
    
    assert resposta.status_code == 200
    assert resposta.json() == {'mensagem': 'Olá Pessoas!'}