import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/resultats/{numero}")
def enregistrer_resultat(numero: int, temps: float, db: Session = Depends(get_db)):
    participant = db.query(models.Participant).filter(models.Participant.numero == numero).first()
    if not participant:
        raise HTTPException(status_code=404, detail="Participant non trouvé")

    # Sauvegarder le temps d'arrivée (tu peux ajouter une table pour les résultats)
    participant.temps = temps
    db.commit()
    return {"message": f"Résultat enregistré pour le participant {numero}"}
