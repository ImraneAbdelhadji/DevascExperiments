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
- de `ping` module om te testen of de server bereikbaar is: 
    `ansible webservers -m ping`

- de `command` module om een eenvoudig commando uit te voeren:
    `ansible webservers -m command -a "/bin/echo hello world"`

Dit toont aan dat Ansible correct werkt en commando’s kan uitvoeren.

### 3. Apache installeren met Ansible
Daarna maak ik een playbook dat:
- Apache automatisch installeert
- de Apache service herstart wanneer nodig
- modules activeert met handlers

Het playbook voer ik uit met:
    `ansible-playbook install_apache_playbook.yaml`

### 4. Apache configureren
Ik pas de Apache configuratie aan met Ansible:
- de luisterpoort wordt gewijzigd naar poort 8081
- configuratiebestanden worden aangepast met lineinfile
- Apache wordt automatisch herstart

Dit doe ik met:
    `ansible-playbook install_apache_options_playbook.yaml`

### 5. Resultaat testen
Ik test het resultaat:
- ik controleer of Apache draait:
    `sudo systemctl status apache2`

ik controleer via de browser of de webserver bereikbaar is op poort 8081