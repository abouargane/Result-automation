from sqlalchemy import Column, Integer, String
from backend.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, unique=True, index=True)  # Numéro du dossard
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    equipe = Column(String, index=True)
    sexe = Column(String, index=True)  # "M" ou "F"
    qr_code = Column(String, unique=True, index=True)  # Chemin du QR Code
