# Dm1 – Docker management-experiment

## Oefening
In deze oefening beheer ik mijn Docker omgeving.
Ik bekijk containers en images, verwijder ongebruikte resources
en controleer de algemene status van Docker.

Alle stappen zijn uitgevoerd via de Docker CLI.

---

## Wat heb ik gedaan?
- Alle Docker containers bekeken
- Alle Docker images bekeken
- Gestopte containers verwijderd
- Ongebruikte images opgeruimd
- De algemene Docker status gecontroleerd
- De Docker omgeving opgeschoond

---

## Belangrijke commando’s

```bash
#Alle draaiende containers bekijken
docker ps

#Alle containers bekijken (ook gestopt)
docker ps -a

#Alle Docker images bekijken
docker images

#Een container stoppen
docker stop <container_naam>

#Een container verwijderen
docker rm <container_naam>

#Een Docker image verwijderen
docker rmi <image_naam>

#Ongebruikte Docker resources opruimen
docker system prune -f

#Docker status en info bekijken
docker info