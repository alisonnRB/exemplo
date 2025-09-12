FROM python:3.11-slim

WORKDIR /main

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]