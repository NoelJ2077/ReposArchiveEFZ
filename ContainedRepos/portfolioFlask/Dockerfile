# Basis-Image
FROM python:3.12.7-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die Abhängigkeiten und den Code
COPY requirements.txt ./
COPY . /app

# Installiere Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Exponiere den Port für die Anwendung
EXPOSE 5000

# Setze den Standard-Modus auf Entwicklung
ENV FLASK_ENV=development

# Produktions-Setup mit Gunicorn
ARG MODE=development

# Installiere Gunicorn nur im Produktionsmodus
RUN if [ "$MODE" = "production" ]; then \
    pip install gunicorn==23.0.0; \
fi

# Erstellen Sie eine Gunicorn-Konfigurationsdatei
COPY gunicorn.conf.py /app/gunicorn.conf.py

# Startbefehl basierend auf dem Modus
ENTRYPOINT ["sh", "-c", "if [ \"$MODE\" = \"production\" ]; then echo 'Starting Gunicorn...'; gunicorn -c /app/gunicorn.conf.py app:app; else echo 'Starting Flask...'; python app.py; fi"]


# Erklärung des obigen Befehls
# -c /app/gunicorn.conf.py: Verwenden Sie die Gunicorn-Konfigurationsdatei
# app:app: Starte die Anwendung in der Datei app.py

# Docker-Build-Befehle
# docker build -t dapp_portfolio:dev . # development
# docker build --build-arg MODE=production --no-cache -t dapp_portfolio:prod . # production

# Docker-Run-Befehle
# docker run -p 5000:5000 -e FLASK_SECRET="wsGL.ApplicationInterface123!!VBT" -e EMAILJS_PUB_KEY="DAcNuMugICb9NY-xO" -e TEST_KEY="Test Key working" dapp_portfolio:dev
# docker run -p 5000:5000 -e FLASK_SECRET="wsGL.ApplicationInterface123!!VBT" -e EMAILJS_PUB_KEY="DAcNuMugICb9NY-xO" -e TEST_KEY="Test Key working" dapp_portfolio:prod
