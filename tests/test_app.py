import sys
sys.path.insert(0, '../app')

from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'service' in data
    assert 'version' in data

def test_health_endpoint(client):
    response = client.get('/health')
    data = response.get_json()
    assert 'status' in data
    assert 'database' in data

def test_metrics_endpoint(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'total_requests' in data
    assert 'success_rate_percent' in data

def test_ready_endpoint(client):
    response = client.get('/ready')
    data = response.get_json()
    assert 'ready' in data