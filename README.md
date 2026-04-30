# CI/CD Demo App
Welcome
FastAPI application demonstrating complete CI/CD workflows with UV, GitHub Actions, Docker and automated testing.

## Requirements

- Python 3.12+
- UV package manager
- Docker (optional for container deployment)

## Setup Instructions

### 1. Install UV
```bash
# Install UV (if not already installed)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone & Initialize
```bash
git clone https://github.com/hellonihar/cicd_demo_app
cd cicd_demo_app

# Create virtual environment
uv venv
```

### 3. Activate Virtual Environment (Windows)
```cmd
.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
uv sync
```

## Running the Application

### Development Server (with auto-reload)
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 9090 --reload
```

### Production Server
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 9090
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message: `{"message": "Welcome to CI/CD Demo"}` |
| `/greet?name={name}` | GET | Personalized greeting: `{"message": "Hello, {name}! Welcome to CI/CD Demo"}` |
| `/health` | GET | Health check endpoint |
| `/docs` | GET | Interactive Swagger UI documentation |
| `/redoc` | GET | Alternative ReDoc documentation |

## Project Structure

```
cicd_demo_app/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI Pipeline
├── tests/
│   ├── __init__.py
│   └── test_main.py        # Test suite with 7 test cases
├── .venv/                  # Virtual environment
├── main.py                 # FastAPI application
├── pyproject.toml          # Project configuration & dependencies
├── uv.lock                 # Locked dependency versions
├── Dockerfile              # Container build configuration
├── .dockerignore
├── .python-version         # Python version pin
├── .gitignore
├── requirements.txt        # Standard pip requirements
└── README.md               # This file
```

## Available UV Commands

| Command | Description |
|---------|-------------|
| `uv add <package>` | Install and add a new dependency |
| `uv add --dev <package>` | Install and add a development dependency |
| `uv remove <package>` | Remove an existing dependency |
| `uv sync` | Install all dependencies from lock file |
| `uv run <command>` | Run command in virtual environment |
| `uv lock` | Update the lock file |
| `uv upgrade` | Upgrade all dependencies |
| `uv export --output-file requirements.txt` | Export requirements.txt file |

## Docker Deployment

### Build Docker Image
```bash
docker build -t ci-cd-demo-app .
```

### Run Container
```bash
docker run -d -p 8000:8000 --name ci-cd-demo ci-cd-demo-app
```

### Verify Container Status
```bash
docker ps
docker logs ci-cd-demo
```

### Stop & Remove Container
```bash
docker stop ci-cd-demo
docker rm ci-cd-demo
```

## Running Tests

### Execute Test Suite
```bash
uv run pytest tests/ -v
```

### Run with coverage report
```bash
uv run pytest tests/ --cov=main --cov-report=term --cov-report=xml
```

✅ Test suite covers:
- Root endpoint validation
- Greet endpoint with parameter
- Greet endpoint parameter validation
- Health check verification
- 404 error handling
- Documentation endpoints testing
- OpenAPI schema validation

## GitHub Actions CI Pipeline

Automated CI workflow runs on every push and pull request:

✅ Pipeline Stages:
1. Checkout code
2. Setup Python environment
3. Install UV package manager
4. Install dependencies
5. Run full test suite
6. Generate code coverage report
7. Upload coverage artifacts
8. Build Docker image (master branch only)

✅ Tested across Python versions: 3.12, 3.13, 3.14

View pipeline runs: https://github.com/hellonihar/cicd_demo_app/actions

## CI/CD Pipeline Stages

This application implements a complete DevOps workflow:

| Stage | Description |
|-------|-------------|
| **Commit** | Code pushed to GitHub repository |
| **Test** | Automated unit tests run |
| **Build** | Docker container image created |
| **Scan** | Security vulnerability scanning |
| **Deploy** | Application deployed to target environment |

---
> This project is a demonstration of modern software development practices and continuous integration/delivery pipelines.


*************
Note: After pullingt the image from Docker Hub run the command below on Docker console:
docker run -d -p 9090:9090 --name ci-cd-demo hellonihar/cicd_demo_app

********************