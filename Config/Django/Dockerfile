FROM python:3-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN apt-get update && \
apt-get install -y cron build-essential libpq-dev curl --no-install-recommends && \
pip install --no-cache-dir -r requirements.txt && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app

COPY ./Config/Django/entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]
