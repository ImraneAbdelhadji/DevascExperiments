#!/bin/bash
# 1. Map voorbereiden
rm -rf tempdir
mkdir -p tempdir/templates
mkdir -p tempdir/static

# 2. Zoek en kopieer bestanden (ongeacht waar ze precies staan in deze repo)
find . -name "sample_app.py" -exec cp {} tempdir/ \;
find . -name "index.html" -exec cp {} tempdir/templates/ \;
# Kopieer de rest van de templates en static als ze bestaan
cp -r templates/* tempdir/templates/ 2>/dev/null
cp -r static/* tempdir/static/ 2>/dev/null

# 3. Controle of het gelukt is
if [ ! -f tempdir/sample_app.py ]; then
    echo "FOUT: sample_app.py is niet gevonden in $(pwd) of submappen!"
    exit 1
fi

# 4. Dockerfile maken
echo "FROM python:3.9-slim" > tempdir/Dockerfile
echo "RUN pip install --no-cache-dir --quiet flask==3.0.0" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD [\"python3\", \"/home/myapp/sample_app.py\"]" >> tempdir/Dockerfile

cd tempdir
docker stop samplerunning 2>/dev/null
docker rm samplerunning 2>/dev/null

# 5. Bouwen en runnen
docker build -t sampleapp .
docker run -t -d -p 5050:5050 --name samplerunning sampleapp
docker ps -a
