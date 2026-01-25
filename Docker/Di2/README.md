# Di2 – Eigen image-experiment (web service)

## Oefening
In deze oefening maak ik mijn **eigen Docker image** voor een eenvoudige webservice.
Ik gebruik een Flask applicatie die draait in een Docker container.

## Wat heb ik gedaan?
- Een eenvoudige Flask webapp gemaakt (`app.py`)
- Een Dockerfile aangemaakt
- Een eigen Docker image gebouwd
- Een Docker container gestart met port mapping
- De webservice getest met curl
- Problemen met poorten en bestaande containers opgelost

```bash

#Docker image bouwen
docker build -t di2-webapp .

#Container starten
docker run -d -p 8082:8080 --name di2-container di2-webapp

#Controleren of de container draait
docker ps

#Webservice testen
curl http://localhost:8082

#Container stoppen en verwijderen
docker stop di2-container
docker rm di2-container