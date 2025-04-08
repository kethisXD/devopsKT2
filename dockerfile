FROM python:3.12-slim

WORKDIR /app

# Копируем код приложения
COPY app_ctl/ /app/app_ctl/
COPY version.txt /app/

# Создаем скрипт-обертку вместо установки пакета
RUN echo '#!/usr/bin/env python3' > /usr/local/bin/calcctl && \
    echo 'import sys' >> /usr/local/bin/calcctl && \
    echo 'from app_ctl.calctl import main' >> /usr/local/bin/calcctl && \
    echo 'if __name__ == "__main__":' >> /usr/local/bin/calcctl && \
    echo '    sys.exit(main())' >> /usr/local/bin/calcctl && \
    chmod +x /usr/local/bin/calcctl && \
    # Добавляем текущую директорию в PYTHONPATH
    echo 'export PYTHONPATH="/app:$PYTHONPATH"' >> /etc/profile && \
    echo 'export PYTHONPATH="/app:$PYTHONPATH"' >> ~/.bashrc

# Проверяем, что скрипт создан
RUN cat /usr/local/bin/calcctl

# Создаем директорию для данных
RUN mkdir -p /app/data

# Устанавливаем PYTHONPATH для работы импорта
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Тестовый запуск
RUN python -c "import app_ctl; print('Module imported successfully')"
RUN ls -la /usr/local/bin/calcctl

# Устанавливаем точку входа
ENTRYPOINT ["calcctl"]

# Метаданные
LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="Command-line calculator utility"