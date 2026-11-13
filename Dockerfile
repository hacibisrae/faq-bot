# 1. Image de base : un Linux minimal avec Python 3.12 déjà installé
FROM python:3.12-slim

# 2. Dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier d'abord la liste des dépendances, puis les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le reste du code
COPY . .

# 5. Sécurité : ne pas faire tourner l'app en tant qu'administrateur (root)
RUN useradd --create-home appuser
USER appuser

# 6. Documenter le port utilisé par l'app
EXPOSE 5000

# 7. Commande lancée au démarrage du conteneur
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]