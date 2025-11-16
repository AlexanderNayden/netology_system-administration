#!/bin/bash

# Проверка доступности порта 80
if ! nc -z localhost 80; then
    echo "Port 80 is not accessible"
    exit 1
fi

# Проверка существования index.html
if [ ! -f /var/www/html/index.html ]; then
    echo "index.html does not exist"
    exit 1
fi

# Если все проверки пройдены
exit 0

