from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test that root endpoint returns correct welcome message"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Welcome to CI/CD Demo"


def test_health_check_endpoint():
    """Test health check endpoint returns healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_invalid_endpoint():
    """Test invalid endpoint returns 404 status code"""
    response = client.get("/invalid-path")
    assert response.status_code == 404


def test_docs_endpoint():
    """Test that Swagger UI documentation loads correctly"""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_openapi_json():
    """Test that OpenAPI schema is available"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "CI/CD Demo App"
    assert schema["info"]["version"] == "1.0.0"
