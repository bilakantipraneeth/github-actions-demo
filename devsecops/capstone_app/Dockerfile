# Insecure base image
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Insecure: Running as root
CMD [ "python", "app.py" ]
