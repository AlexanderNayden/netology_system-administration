terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.5.3"
    }
    null = {
      source  = "hashicorp/null"
      version = "3.2.2"
    }
  }
}

# Создаем docker-compose файл
resource "local_file" "docker_compose" {
  filename = "docker-compose.yml"
  content  = <<-EOT
services:
  web1:
    image: nginx:alpine
    container_name: web-server-1
    hostname: web1
    volumes:
      - ./web1.html:/usr/share/nginx/html/index.html:ro

  web2:
    image: nginx:alpine
    container_name: web-server-2
    hostname: web2
    volumes:
      - ./web2.html:/usr/share/nginx/html/index.html:ro

  loadbalancer:
    image: haproxy:alpine
    container_name: load-balancer
    hostname: loadbalancer
    ports:
      - "8088:80"
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - web1
      - web2
EOT
}

# Создаем HTML файлы
resource "local_file" "web1_html" {
  filename = "web1.html"
  content  = <<-EOT
<!DOCTYPE html>
<html>
<head>
    <title>Web Server 1</title>
</head>
<body style="background: lightblue; text-align: center; padding: 50px;">
    <h1>Hello from Web Server 1!</h1>
    <p>Load Balancer Test</p>
</body>
</html>
EOT
}

resource "local_file" "web2_html" {
  filename = "web2.html"
  content  = <<-EOT
<!DOCTYPE html>
<html>
<head>
    <title>Web Server 2</title>
</head>
<body style="background: lightgreen; text-align: center; padding: 50px;">
    <h1>Hello from Web Server 2!</h1>
    <p>Load Balancer Test</p>
</body>
</html>
EOT
}

# Создаем конфигурацию HAProxy
resource "local_file" "haproxy_cfg" {
  filename = "haproxy.cfg"
  content  = <<-EOT
global
    daemon
    maxconn 256

defaults
    mode http
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web1 web1:80 check
    server web2 web2:80 check
EOT
}

# Запускаем инфраструктуру
resource "null_resource" "start_infrastructure" {
  depends_on = [
    local_file.docker_compose,
    local_file.web1_html,
    local_file.web2_html,
    local_file.haproxy_cfg
  ]

  provisioner "local-exec" {
    command = "docker-compose up -d"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "docker-compose down"
  }
}

output "load_balancer_url" {
  value = "http://localhost:8088"
}

output "instructions" {
  value = <<-EOT

  ✅ ИНФРАСТРУКТУРА УСПЕШНО РАЗВЕРНУТА!

  Балансировщик нагрузки доступен по адресу: http://localhost:8088

  Архитектура:
  - 2 веб-сервера Nginx (web-server-1, web-server-2)
  - 1 балансировщик HAProxy (load-balancer)
  - Round-robin распределение нагрузки

  Для проверки выполните:
  curl http://localhost:8088

  EOT
}
