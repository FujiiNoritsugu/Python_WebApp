# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY static static
COPY templates templates
COPY app.py app.py
COPY mysql_model.py mysql_model.py
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
