# Utiliser une image légère de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans l'image Docker
COPY requirements.txt ./
COPY app.py ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080 (Render et Cloud Run utilisent ce port)
EXPOSE 8080

# Définir la commande de démarrage de l'application
CMD ["python", "app.py"]
