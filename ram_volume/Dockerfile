FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY ram_volume/ram_volume.py ram_volume.py
COPY messages ./messages
COPY ram_volume/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "ram_volume.py"]