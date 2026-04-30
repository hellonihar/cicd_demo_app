# CI/CD Demo App

FastAPI application demonstrating CI/CD workflows.

## Requirements

- Python 3.12+
- UV package manager

## Setup Instructions

### 1. Install UV
```bash
# Install UV (if not already installed)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone & Initialize
```bash
git clone <repository-url>
cd app_to_demo_CI_CD

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
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Production Server
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message: `{"message": "Welcome to CI/CD Demo"}` |
| `/health` | GET | Health check endpoint |
| `/docs` | GET | Interactive Swagger UI documentation |
| `/redoc` | GET | Alternative ReDoc documentation |

## Project Structure

```
app_to_demo_CI_CD/
├── .venv/              # Virtual environment
├── main.py             # FastAPI application
├── pyproject.toml      # Project configuration & dependencies
├── uv.lock             # Locked dependency versions
├── .python-version     # Python version pin
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Available UV Commands

| Command | Description |
|---------|-------------|
| `uv add <package>` | Install and add a new dependency |
| `uv remove <package>` | Remove an existing dependency |
| `uv sync` | Install all dependencies from lock file |
| `uv run <command>` | Run command in virtual environment |
| `uv lock` | Update the lock file |
| `uv upgrade` | Upgrade all dependencies |

## Docker Deployment

### Build Docker Image
```bash
docker build -t ci-cd-demo-app .
```

### Run Container
```bash
docker run -d -p 9090:9090 --name ci-cd-demo ci-cd-demo-app
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

## CI/CD Pipeline

This application is designed to demonstrate continuous integration and deployment workflows. Typical pipeline steps:

1. **Lint**: Code quality checks
2. **Test**: Unit and integration tests
3. **Build**: Create container image
4. **Scan**: Security vulnerability scanning
5. **Deploy**: Deploy to target environment
