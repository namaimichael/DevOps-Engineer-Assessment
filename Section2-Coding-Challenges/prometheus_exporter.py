import os
import requests
from prometheus_client import start_http_server, Gauge
import time

# Environment variables
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')

# Prometheus metrics
QUEUE_MESSAGES = Gauge(
    'rabbitmq_individual_queue_messages',
    'Total messages in RabbitMQ queues',
    ['host', 'vhost', 'queue']
)
QUEUE_READY = Gauge(
    'rabbitmq_individual_queue_messages_ready',
    'Ready messages in RabbitMQ queues',
    ['host', 'vhost', 'queue']
)
QUEUE_UNACK = Gauge(
    'rabbitmq_individual_queue_messages_unacknowledged',
    'Unacknowledged messages in RabbitMQ queues',
    ['host', 'vhost', 'queue']
)

def fetch_rabbitmq_metrics():
    url = f"http://{RABBITMQ_HOST}:15672/api/queues"
    try:
        response = requests.get(url, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
        response.raise_for_status()
        queues = response.json()
        for queue in queues:
            vhost = queue['vhost']
            name = queue['name']
            QUEUE_MESSAGES.labels(host=RABBITMQ_HOST, vhost=vhost, queue=name).set(queue['messages'])
            QUEUE_READY.labels(host=RABBITMQ_HOST, vhost=vhost, queue=name).set(queue['messages_ready'])
            QUEUE_UNACK.labels(host=RABBITMQ_HOST, vhost=vhost, queue=name).set(queue['messages_unacknowledged'])
    except Exception as e:
        print(f"Error fetching RabbitMQ metrics: {e}")

if __name__ == '__main__':
    # Start the Prometheus exporter server
    start_http_server(8000)
    print("Prometheus exporter started on port 8000")
    while True:
        fetch_rabbitmq_metrics()
        time.sleep(10)