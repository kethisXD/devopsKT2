#!/bin/bash
# Скрипт для сборки бинарного файла calcctl


mkdir -p dist


cat > dist/calcctl << 'EOF'
#!/usr/bin/env python3

from app_ctl.calctl import main

if __name__ == "__main__":
    main()
EOF


chmod +x dist/calcctl

echo "Бинарный файл создан в dist/calcctl"