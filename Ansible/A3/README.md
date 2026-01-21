# A3 – Eigen playbook-experiment 2 (Docker)

## Oefening
In deze oefening maak ik een eigen Ansible playbook om een andere service
dan een webserver te installeren.  
Voor A3 kies ik Docker, zodat ik toon dat ik Ansible ook kan gebruiken
voor andere types servers en services.

---

## Wat doet dit playbook?
Het playbook:
- installeert Docker
- start de Docker service
- zorgt dat Docker automatisch start bij het opstarten van de server

---

## Uitgevoerde stappen

### 1. Inventory configureren
Ik maak een inventory bestand (`hosts`) met een aparte hostgroep
voor deze oefening.

De server staat in de groep `dockerservers`.
Zo weet Ansible op welke server het playbook moet worden uitgevoerd.

---

### 2. Docker installeren met Ansible
Ik maak een eigen Ansible playbook (`install_docker.yaml`) dat Docker
automatisch installeert.

Ik gebruik:
- de `apt` module om Docker te installeren
- de `service` module om Docker te starten en te activeren

Het playbook voer ik uit met:
`ansible-playbook -i hosts install_docker.yaml`

---

### 3. Extra test: Docker zichtbaar maken

Docker zelf toont niets in de browser.
Om te testen of Docker echt werkt, start ik een webserver container
met Docker.

Ik start een Nginx container via Ansible:
`ansible dockerservers -m command -a "docker run -d -p 8082:80 nginx"`

Daarna test ik via de browser:

http://192.0.2.3:8082

Als de Nginx webpagina verschijnt, weet ik dat Docker correct werkt.
