FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY model_inference/model_inference.py model_inference.py
COPY messages ./messages
COPY model_inference/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "model_inference.py"]