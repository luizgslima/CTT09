from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_somar():
    response = client.get("/somar/10/20")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}

def test_multiplicar():
    response = client.get("/multiplicar/2/2")
    assert response.status_code == 200
    # ERRO INTENCIONAL: Esperando 5 em vez de 4
    assert response.json() == {"resultado": 4}