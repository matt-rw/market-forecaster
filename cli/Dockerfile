# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements-cli.txt /app/
RUN pip install --upgrade pip && pip install -r requirements-cli.txt
RUN apt-get update && apt-get install -y vim

COPY . /app/

ENTRYPOINT ["python", "-m", "cli"]

