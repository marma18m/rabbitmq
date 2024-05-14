FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY receiver/receiver.py receiver.py
COPY messages ./messages
COPY receiver/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "receiver.py"]