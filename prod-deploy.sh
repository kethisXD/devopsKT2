#!/bin/bash
# Скрипт для локального деплоя

# Получаем текущую версию
VERSION=$(cat version.txt)
echo "Deploying version $VERSION to production"

# Сборка Docker-образа локально
echo "Building Docker image locally..."
docker build -t kethisxd/calcctl:latest -t kethisxd/calcctl:v$VERSION .

# Запускаем через docker compose
docker compose down || true
docker compose up -d

echo "Waiting for container to start..."
sleep 2

# Тестируем приложение
echo "Testing calculation: 5 + 3 ="
docker exec calcctl-prod calcctl add 5 3 || {
  echo "Error running calcctl in container. Testing with direct docker run..."
  docker run --rm kethisxd/calcctl:latest add 5 3
}

echo "✅ Deployment complete!"