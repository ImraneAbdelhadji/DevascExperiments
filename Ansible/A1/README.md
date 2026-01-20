# A1 – Ansible Playbooks (Lab 7.4.8)

## Oefening
In deze oefening werk ik met Ansible playbooks om taken te automatiseren
op een Linux webserver.  
Ik gebruik Ansible om verbinding te maken met een remote server en
daar automatisch commando’s en installaties uit te voeren.

---

## Uitgevoerde stappen

### 1. Ansible configureren
Ik configureer Ansible met:
- een inventory bestand (`hosts`) waarin de webserver staat
- een configuratiebestand (`ansible.cfg`)
- SSH login met gebruiker en wachtwoord

Hiermee weet Ansible welke servers beheerd worden.

---

### 2. Verbinding testen met Ansible
Ik test eerst of Ansible correct kan verbinden met de webserver.

Ik gebruik:
- de `ping` module om te testen of de server bereikbaar is
- de `command` module om een eenvoudig commando uit te voeren

Het playbook met het echo-commando toont dat Ansible correct werkt.

---

### 3. Apache installeren met Ansible
Daarna maak ik een playbook dat:
- Apache automatisch installeert
- de Apache service herstart wanneer nodig
- modules activeert met handlers

Zo wordt de webserver volledig automatisch opgezet.

---

### 4. Apache configureren
Ik pas de Apache configuratie aan met Ansible:
- de luisterpoort wordt gewijzigd naar poort 8081
- configuratiebestanden worden aangepast met `lineinfile`
- Apache wordt automatisch herstart

---

### 5. Resultaat testen
Ik test het resultaat:
- via systemctl controleer ik of Apache draait
- via de browser controleer ik of de webpagina bereikbaar is
- Apache is bereikbaar op poort 8081
