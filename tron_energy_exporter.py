import time
import os
from prometheus_client import start_http_server, Gauge
import requests
from tronpy import Tron

# Инициализация метрик Prometheus
TRON_ENERGY = Gauge('tron_energy', 'Current TRON energy balance', ['wallet_address'])

# Конфигурация
TRON_WALLET_ADDRESS = os.getenv('TRON_WALLET_ADDRESS')
UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', '60'))  # По умолчанию 60 секунд
METRICS_PORT = int(os.getenv('METRICS_PORT', '8000'))

client = Tron()

def get_account_resource(address):
    try:
        # Получаем информацию о ресурсах аккаунта
        account = client.get_account_resource(address)
        
        # Получаем значение энергии
        energy_limit = account.get('energy_limit', 0)
        energy_used = account.get('energy_used', 0)
        
        return energy_limit - energy_used
    except Exception as e:
        print(f"Error fetching account resource: {e}")
        return 0

def update_metrics():
    while True:
        try:
            energy = get_account_resource(TRON_WALLET_ADDRESS)
            TRON_ENERGY.labels(wallet_address=TRON_WALLET_ADDRESS).set(energy)
        except Exception as e:
            print(f"Error updating metrics: {e}")
        
        time.sleep(UPDATE_INTERVAL)

if __name__ == '__main__':
    if not TRON_WALLET_ADDRESS:
        raise ValueError("TRON_WALLET_ADDRESS environment variable is required")
    
    # Запускаем сервер метрик
    start_http_server(METRICS_PORT)
    print(f"Metrics server started on port {METRICS_PORT}")
    
    # Запускаем сбор метрик
    update_metrics()