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


def test_greet_endpoint():
    """Test greet endpoint returns personalized message"""
    name = "Test User"
    response = client.get(f"/greet?name={name}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Hello, {name}! Welcome to CI/CD Demo"


def test_greet_endpoint_missing_parameter():
    """Test greet endpoint requires name parameter"""
    response = client.get("/greet")
    assert response.status_code == 422
    error_detail = response.json()["detail"]
    assert any(error["loc"] == ["query", "name"] for error in error_detail)


def test_square_endpoint_positive_number():
    """Test square endpoint returns correct value for positive number"""
    number = 5
    response = client.get(f"/square?number={number}")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 25


def test_square_endpoint_zero():
    """Test square endpoint returns 0 when input is 0"""
    response = client.get("/square?number=0")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0


def test_square_endpoint_negative_number():
    """Test square endpoint returns correct value for negative number"""
    number = -7
    response = client.get(f"/square?number={number}")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 49


def test_square_endpoint_large_number():
    """Test square endpoint handles large numbers correctly"""
    number = 12345
    response = client.get(f"/square?number={number}")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == number * number


def test_square_endpoint_missing_parameter():
    """Test square endpoint requires number parameter"""
    response = client.get("/square")
    assert response.status_code == 422
    error_detail = response.json()["detail"]
    assert any(error["loc"] == ["query", "number"] for error in error_detail)


def test_square_endpoint_invalid_number_type():
    """Test square endpoint returns validation error for non-integer input"""
    response = client.get("/square?number=not-a-number")
    assert response.status_code == 422
    error_detail = response.json()["detail"]
    assert any(error["loc"] == ["query", "number"] for error in error_detail)
