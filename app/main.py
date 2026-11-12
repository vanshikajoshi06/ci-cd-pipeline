from fastapi import FastAPI

app = FastAPI(title="CI/CD Pipeline Demo")


@app.get("/")
def home():
    return {
        "message": "Welcome to our CI/CD Pipeline!",
        "status": "Application is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/users")
def get_users():
    return {
        "users": ["Vanshika", "Rahul", "Priya"]
    }