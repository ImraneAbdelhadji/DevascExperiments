FROM python:3.9-slim
RUN pip install --no-cache-dir --quiet flask==3.0.0
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/
EXPOSE 5050
CMD ["python3", "/home/myapp/sample_app.py"]
