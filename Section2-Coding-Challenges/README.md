# Section 2: Coding Challenges

This directory contains solutions to the coding challenges, including a Dockerfile for containerizing a Laravel application, a Prometheus exporter for RabbitMQ, and a Bash script to restart a Laravel service based on CPU usage.

---

## Files Overview

### 1. `Dockerfile`
- **Description**:
  The `Dockerfile` is used to containerize a Laravel application. It sets up a lightweight and production-ready environment with PHP-FPM, Composer, and required PHP extensions for Laravel.

- **Usage**:
  1. **Build the Docker image**:
     ```bash
     docker build -t laravel-app .
     ```
  2. **Run the container**:
     ```bash
     docker run -d -p 8000:9000 laravel-app
     ```
  3. Access the application at `http://localhost:8000`.

---

### 2. `prometheus_exporter.py`
- **Description**:
  This Python script acts as a Prometheus exporter for RabbitMQ. It connects to the RabbitMQ management API and exports queue metrics like `messages`, `messages_ready`, and `messages_unacknowledged`.

- **Exposed Metrics**:
  - `rabbitmq_individual_queue_messages`
  - `rabbitmq_individual_queue_messages_ready`
  - `rabbitmq_individual_queue_messages_unacknowledged`

- **Usage**:
  1. **Set environment variables**:
     ```bash
     export RABBITMQ_HOST=your_rabbitmq_host
     export RABBITMQ_USER=your_rabbitmq_user
     export RABBITMQ_PASSWORD=your_rabbitmq_password
     ```
  2. **Install dependencies**:
     ```bash
     pip install prometheus-client requests
     ```
  3. **Run the exporter**:
     ```bash
     python prometheus_exporter.py
     ```
  4. Access metrics at `http://localhost:8000/metrics`.

---

### 3. `restart_laravel.sh`
- **Description**:
  This Bash script monitors CPU usage on the server and restarts the Laravel backend service if CPU usage exceeds 80%. It ensures service availability under heavy load.

- **Usage**:
  1. **Make the script executable**:
     ```bash
     chmod +x restart_laravel.sh
     ```
  2. **Run the script manually**:
     ```bash
     ./restart_laravel.sh
     ```
  3. **Automate using Cron (Optional)**:
     Add the script to a cron job for periodic monitoring:
     ```bash
     crontab -e
     ```
     Add the following line to check every minute:
     ```bash
     * * * * * /path/to/restart_laravel.sh >> /var/log/restart_laravel.log 2>&1
     ```

---

## Summary

- The **`Dockerfile`** provides a containerized environment for Laravel applications.
- The **`prometheus_exporter.py`** enables monitoring of RabbitMQ queues via Prometheus.
- The **`restart_laravel.sh`** script ensures Laravel service uptime by monitoring and acting on CPU usage thresholds.

Each file addresses a specific challenge and can be used independently or integrated into larger systems. For further details, feel free to explore the code and adapt it to your environment.