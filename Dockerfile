FROM python:alpine3.20

WORKDIR /http-job

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]

EXPOSE 8000
