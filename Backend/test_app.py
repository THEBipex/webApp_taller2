import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Prueba que el endpoint raiz funciona"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"API Backend Operativa" in rv.data

def test_suma_correcta(client):
    """Prueba una suma valida"""
    rv = client.post('/sumar', json={'num1': 10, 'num2': 5})
    json_data = rv.get_json()
    assert json_data['resultado'] == 15.0

def test_suma_error(client):
    """Prueba error cuando faltan datos"""
    rv = client.post('/sumar', json={})
    assert rv.status_code == 400