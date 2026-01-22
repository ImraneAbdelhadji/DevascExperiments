# Pv1 – Python Virtual Environment (venv)

## Oefening
In deze oefening leer ik werken met een Python virtual environment (venv).
Ik gebruik een venv om Python packages gescheiden te houden per project.

## Wat heb ik gedaan?
- Een projectmap aangemaakt
- Een virtual environment gemaakt en geactiveerd
- Flask en requests geïnstalleerd
- Een eenvoudige Flask applicatie gemaakt
- De applicatie getest in de browser
- Gecontroleerd welk proces draait op poort 5050

## Belangrijke commando’s
- venv maken: `python3 -m venv venv`
- venv activeren: `source venv/bin/activate`
- packages installeren: `pip install flask`
- app starten: `python3 app.py`
- Controleren: `sudo lsof -i :5050`
- venv stoppen: `deactivate`

## Resultaat
De Flask applicatie draait correct binnen een virtual environment.
