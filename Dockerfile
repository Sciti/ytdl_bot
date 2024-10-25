# Use the official Python 3.11 slim image
FROM python:3.11-alpine

# Install dependencies
RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
        gcc \
        musl-dev \
        postgresql-dev \
        libffi-dev \
        openssl-dev \
        git \
        ffmpeg

# Copy your bot's source code into the container
WORKDIR /app
COPY . /app

# Install Python dependencies (update with your bot requirements)
RUN pip install --no-cache-dir -r requirements.txt

# Expose any port if necessary (e.g., for webhook)
# EXPOSE 5000

# Default command to run the bot
CMD ["python3", "-m", "ytdl_bot"]
