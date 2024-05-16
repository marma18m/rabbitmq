FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY model_inference/ .
COPY schemas ./schemas

RUN pip install -r requirements.txt

CMD ["python3", "model_inference.py"]