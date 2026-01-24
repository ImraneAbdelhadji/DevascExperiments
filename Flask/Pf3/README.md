# Pv2 – Eigen venv-experiment (deployment)

## Doel
In deze oefening heb ik een eigen Python project gemaakt
om te tonen dat ik virtual environments en deployment begrijp.

## Wat doet deze applicatie?
Dit is een Flask webapplicatie die:
- een stad vraagt aan de gebruiker
- weerinformatie ophaalt via de OpenWeather API
- temperatuur en weersbeschrijving toont

## Waarom virtual environment?
Ik gebruik een venv zodat:
- dependencies gescheiden blijven van het systeem
- het project reproduceerbaar is
- deployment eenvoudiger is

Installeer dependencies:
`pip install -r requirements.txt`

Start de applicatie:
`python3 app.py`
