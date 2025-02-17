import os
from fastapi import FastAPI
from backend.database import engine, Base
from backend.routes import router

app =  FastAPI(
    title="Result Automation API",
    description="API pour la collecte des résultats via QR Code",
    version="1.0",
    docs_url="/docs",  # Permet d'accéder à Swagger
    redoc_url="/redoc",  # Permet d'accéder à Redoc
)

Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API fonctionne"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Render utilise une variable d'environnement
    uvicorn.run(app, host="0.0.0.0", port=port)
