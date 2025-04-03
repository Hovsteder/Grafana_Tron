# Grafana TRON Energy Monitor

Система мониторинга энергии кошелька TRON с использованием Grafana, Prometheus и Python.

## Требования

- Docker
- Docker Compose
- TRON кошелек

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Hovsteder/Grafana_Tron.git
cd Grafana_Tron
```

2. Создайте файл `.env` с вашими настройками:
```bash
TRON_WALLET_ADDRESS=ваш_адрес_кошелька
UPDATE_INTERVAL=60  # интервал обновления в секундах
```

3. Запустите сервисы:
```bash
docker-compose up -d
```

4. Откройте Grafana в браузере:
```
http://localhost:3000
```

Логин: admin
Пароль: admin

## Настройка дашборда

1. Войдите в Grafana
2. Добавьте Prometheus как источник данных:
   - URL: http://prometheus:9090
3. Импортируйте дашборд или создайте новый
4. Добавьте график с метрикой `tron_energy`

## Метрики

- `tron_energy`: Текущий баланс энергии кошелька TRON

## Поддержка

При возникновении проблем создайте Issue в этом репозитории.