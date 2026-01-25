# Dc1 – Run containers-experiment

## Oefening
In deze oefening leer ik werken met het **runnen en beheren van Docker containers**.
Ik gebruik een bestaande Docker image en voer basisacties uit zoals starten, testen,
bekijken, stoppen en verwijderen van containers.

Alle stappen zijn uitgevoerd via de Docker CLI.

---

## Wat heb ik gedaan?
- Een Docker container gestart met `docker run`
- Poortmapping gebruikt om de container bereikbaar te maken
- Gecontroleerd welke containers draaien
- De container getest met curl
- Logs van de container bekeken
- De container gestopt en verwijderd

---

## Belangrijke commando’s

```bash

#Container starten (nginx)
docker run -d -p 8083:80 --name dc1-nginx nginx

#Draaiende containers bekijken
docker ps

#Container testen
curl http://localhost:8083

#Alle containers bekijken (ook gestopt)
docker ps -a

#Logs van de container bekijken
docker logs dc1-nginx

#Container stoppen
docker stop dc1-nginx

#Container verwijderen
docker rm dc1-nginx


