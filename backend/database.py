from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Récupération de l'URL de la base de données depuis les variables d'environnement
DATABASE_URL = os.getenv("postgresql://result_automation_user:LrwTETINmsLvvXGHPEGLxTHWx5XFLU0K@dpg-cup6qfl6l47c73cjd290-a.oregon-postgres.render.com/result_automation", "sqlite:///./participants.db")

# Création de l'engine SQLAlchemy (ajout de gestion pour PostgreSQL)
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

# Création d'une session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()
metadata = MetaData()
