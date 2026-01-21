# A2 – Eigen playbook-experiment (webserver)

## Oefening
In deze oefening maak ik een eigen Ansible playbook om een webserver
automatisch te installeren en configureren.  
Dit is een eigen experiment, los van het oorspronkelijke lab.

---

## Wat doet dit playbook?
Het playbook:
- installeert Apache
- start de Apache service
- zorgt dat Apache automatisch start bij het opstarten van de server
- plaatst een aangepaste webpagina

---

## Uitgevoerde stappen

### 1. Inventory configureren
Ik maak een inventory bestand (`hosts`) waarin de webserver staat.
De server zit in de groep `webservers`.

Zo weet Ansible op welke server het playbook moet worden uitgevoerd.

---

### 2. Apache installeren met Ansible
Ik maak een eigen Ansible playbook (`webserver_A2.yaml`) dat Apache
automatisch installeert.

Ik gebruik:
- de `apt` module om Apache te installeren
- de `service` module om Apache te starten en te activeren

Het playbook voer ik uit met:
`ansible-playbook -i hosts webserver_A2.yaml`
