#!/bin/bash

SOURCE_DIR="$HOME"
BACKUP_DIR="/tmp/backup"
LOG_FILE="/var/log/backup.log"

# Создаем директорию для логов если не существует
sudo mkdir -p /var/log/

# Выполняем резервное копирование
if rsync -avc --delete --exclude='.*/' "$SOURCE_DIR/" "$BACKUP_DIR/" >> "$LOG_FILE" 2>&1; then
    echo "$(date): Резервное копирование УСПЕШНО завершено" >> "$LOG_FILE"
else
    echo "$(date): Резервное копирование ЗАВЕРШИЛОСЬ С ОШИБКОЙ" >> "$LOG_FILE"
    exit 1
fi