FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY SIM/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]