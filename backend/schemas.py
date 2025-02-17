from pydantic import BaseModel, Field

class ParticipantBase(BaseModel):
    numero: int = Field(..., title="Numéro unique du participant")
    nom: str
    prenom: str
    equipe: str
    sexe: str  # "M" ou "F"

class ParticipantCreate(ParticipantBase):
    pass

class ParticipantResponse(ParticipantBase):
    id: int
    qr_code: str

    class Config:
        from_attributes = True
