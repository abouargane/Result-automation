import os
from fastapi import FastAPI
from backend.database import engine, Base
from backend.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API fonctionne"}

# Forcer l'usage du bon port
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
