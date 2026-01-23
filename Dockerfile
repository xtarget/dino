FROM python:3.11-slim

EXPOSE 8080
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

# install deps only, for caching
COPY src/setup.py .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -e .

# install dino itself
COPY src .
RUN pip install --no-cache-dir -e .

USER 1000
CMD uwsgi --http-socket :8080 --master --workers 8 --module dino.wsgi
