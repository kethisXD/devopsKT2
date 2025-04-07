FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -e .

# Устанавливаем точку входа
ENTRYPOINT ["calcctl"]

# Информация о проекте
LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="$(cat version.txt)"
LABEL description="Command-line calculator utility"