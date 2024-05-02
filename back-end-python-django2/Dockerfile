# Dockerfile

FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /usr/src/app/core

CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:8000"]
