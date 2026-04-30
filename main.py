from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo App", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Welcome to CI/CD Demo ***"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# add one end point that takes a name as query parameter and returns a personalized greeting
@app.get("/greet")
async def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to CI/CD Demo"}
