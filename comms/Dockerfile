FROM python:3.10.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY comms/ .
COPY schemas ./schemas
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

CMD ["python3", "comms.py"]