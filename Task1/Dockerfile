FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV YOUR_NAME=Fatima

EXPOSE 5500

CMD ["python", "app.py"]
