FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY sender/sender.py sender.py
COPY messages ./messages
COPY sender/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "sender.py"]