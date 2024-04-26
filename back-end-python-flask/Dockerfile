FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

CMD ["python3", "app.py"]