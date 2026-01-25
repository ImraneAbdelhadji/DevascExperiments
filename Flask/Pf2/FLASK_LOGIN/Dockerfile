FROM python:3.8-slim

# Werkmap in de container
WORKDIR /app

# Optioneel: pip-voortgang uitzetten (handiger in beperkte omgeving)
ENV PIP_PROGRESS_BAR=off

# Python dependencies installeren
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir -r requirements.txt

# App-bestanden kopiëren
COPY . /app

# Zeg tegen flask_app_login.py dat we in Docker zitten
ENV IN_DOCKER=1

# Poort 5555 in de container
EXPOSE 5555

# Start je Flask-app
CMD ["python", "flask_app_login.py"]