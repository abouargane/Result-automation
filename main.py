from fastapi import FastAPI
from backend.database import engine, Base
from backend.routes import router

app = FastAPI()

# Création automatique des tables
Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API fonctionne"}

