# Pf2 – Explore the Evolution of Password Methods (Flask & Security)

## Oefening
In deze oefening onderzoek ik hoe wachtwoorden doorheen de tijd zijn opgeslagen in webapplicaties.
Ik bouw een Flask web API waarin ik eerst wachtwoorden **in plaintext** opsla en daarna **gehashte
wachtwoorden** gebruik. Zo toon ik aan waarom hashing noodzakelijk is voor security.

---

## Wat heb ik gedaan?
- Een Flask webapplicatie opgezet in Python
- Een SQLite database (`test.db`) gebruikt voor opslag
- Gebruikers aangemaakt met plaintext wachtwoorden (onveilig)
- Loginfunctionaliteit getest met plaintext opslag
- Password hashing geïmplementeerd met SHA-256
- Gebruikers aangemaakt met gehashte wachtwoorden
- Login getest met gehashte passwords
- De database geïnspecteerd met DB Browser for SQLite
- Geanalyseerd waarom hashing zonder salt nog steeds zwak is

---

## Belangrijke commando’s

```bash

#Applicatie starten op de achtergrond
nohup python3 password-evolution.py &

#Applicatie stoppen
pkill -f password-evolution.py

#Server testen
curl -k https://0.0.0.0:5000/

#Plaintext gebruiker aanmaken
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' https://0.0.0.0:5000/signup/v1

#Plaintext login
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' https://0.0.0.0:5000/login/v1

#Gehashte gebruiker aanmaken
curl -k -X POST -F 'username=rick' -F 'password=samepassword' https://0.0.0.0:5000/signup/v2

curl -k -X POST -F 'username=allan' -F 'password=samepassword' https://0.0.0.0:5000/signup/v2

curl -k -X POST -F 'username=dave' -F 'password=differentpassword' https://0.0.0.0:5000/signup/v2

#Login met gehashte passwords
curl -k -X POST -F 'username=allan' -F 'password=wrongpassword' https://0.0.0.0:5000/login/v2

curl -k -X POST -F 'username=allan' -F 'password=samepassword' https://0.0.0.0:5000/login/v2
