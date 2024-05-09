FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY sender.py sender.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "sender.py"]