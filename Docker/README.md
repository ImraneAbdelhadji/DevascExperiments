# Di1 – Build a Sample Web App in a Docker Container

## Oefening
In deze oefening bouw ik een eenvoudige Flask webapplicatie en draai ik deze
in een Docker container.  
Het doel is om te leren hoe een Python webapplicatie wordt verpakt in Docker
en hoe poorten en bestanden correct worden gebruikt binnen een container.

---

## Wat heb ik gedaan?
- Een eenvoudige Flask webapplicatie gemaakt in Python
- HTML en CSS toegevoegd via templates en static mappen
- De webapp lokaal getest met curl
- Een bash script geschreven om een Docker image te bouwen
- Een Docker container gestart met port mapping
- Problemen met pip en threading opgelost in een beperkte lab-VM
- De container getest via localhost
- De container beheerd met Docker commando’s

---

```bash
#Flask applicatie lokaal testen
python3 sample_app.py


#Testen:
curl http://0.0.0.0:8080

#Docker build & run script uitvoeren
chmod a+x sample-app.sh
bash sample-app.sh

#Controleren of de container draait
docker ps

#Webapp testen in Docker
curl http://localhost:8080

#Logs van de container bekijken
docker logs samplerunning

#Container stoppen en verwijderen
docker stop samplerunning
docker rm samplerunning

#Docker image verwijderen
docker rmi sampleapp

#Containers en images opruimen (optioneel)
docker system prune -f

