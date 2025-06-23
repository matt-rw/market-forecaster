# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements-cli.txt /app/
RUN pip install --upgrade pip && pip install -r requirements-cli.txt

COPY . /app/

ENTRYPOINT ["python", "-m", "cli"]

