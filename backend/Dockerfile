FROM python:3.10-slim

LABEL authors="keshavi"

# Install system packages needed for llama-cpp-python
RUN apt-get update && apt-get install -y \
    build-essential cmake git wget python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy local code into the container
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
