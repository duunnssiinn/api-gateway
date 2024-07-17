from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check__endpoint_response_code_is_200():
    response = client.get("/")
    assert response.status_code == 200
 
def test_health_check_endpoint_json_is_correct():
    response = client.get("/")
    assert response.json() == {"status": "Healthy"}

def test_health_check_endpoint_json_status_value_is_Healthy():
    response = client.get("/")
    assert response.json()["status"] == "Healthy"    

def test_health_check_endpoint_returns_only_200_response_code():
    response = client.get("/")
    assert response.status_code == 500

def test_health_check_json_is_incorrect():
    response = client.get("/")
    assert response.json() == {"status": "healthy"}
