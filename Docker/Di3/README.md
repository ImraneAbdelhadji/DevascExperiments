# Di3 – Eigen image-experiment 2 (SQL)

## Oefening
In deze oefening experimenteer ik met een **SQL database in Docker**.
Omdat klassieke database servers (MySQL en MariaDB) niet correct starten in de lab-VM
door threading- en timerbeperkingen, gebruik ik **SQLite** als lichtgewicht SQL-oplossing.

## Wat heb ik gedaan?
- Een SQL database gedraaid in een Docker container
- Een SQLite container gebruikt als lichtgewicht SQL-oplossing
- Een database aangemaakt binnen de container
- Een tabel aangemaakt en data toegevoegd
- SQL queries uitgevoerd om data te controleren
- De container correct gestopt

```bash

#SQLite container starten
docker run -it --name di3-sqlite nouchka/sqlite3

#Database openen (in de container)
.open di3.db

#Tabel aanmaken
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
);

#Data toevoegen
INSERT INTO users (name) VALUES ('Alice');
INSERT INTO users (name) VALUES ('Bob');

#Data opvragen
SELECT * FROM users;

#SQLite verlaten
.exit

#Container stoppen
docker stop di3-sqlite