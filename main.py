from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo App", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Welcome to CI/CD Demo"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
