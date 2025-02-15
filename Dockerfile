# Utiliser une image légère de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY app.py ./
COPY credentials.json ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080 (Cloud Run utilise ce port)
EXPOSE 8080

# Exécuter l'application Flask
CMD ["python", "app.py"]
' > Dockerfile
