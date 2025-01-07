# DevOps Engineer Assessment

## Overview
This repository contains solutions for the technical assessment, showcasing my skills in DevOps, coding, troubleshooting, and process optimization.

## Repository Structure

-  README.md
    - Section1-General-Knowledge
       - centralized-logging.md
       - self-healing-service.md
    - Section2-Coding-Challenges
        - Dockerfile
        -  README.md
        - prometheus_exporter.py
        - restart_laravel.sh
    - Section3-Monitoring-Troubleshooting
        - high_latency_debug.md
        - react_native_monitoring.md
    - Section4-Behavioral
        - behavioral-responses.md

---

## Section 1: General Knowledge
- **Context**:
  This section addresses high-level DevOps concepts, including designing scalable systems, centralized logging, and secure CI/CD pipelines.
  
- **Solutions**:
  - [`self-healing-service.md`](Section1-General-Knowledge/self-healing-service.md): A detailed explanation of designing a self-healing distributed service using Kubernetes health probes, retries, and circuit breakers.
  - [`centralized-logging.md`](Section1-General-Knowledge/centralized-logging.md): A design for implementing centralized logging with tools like ELK Stack or Loki, suitable for microservices architecture.

---

## Section 2: Coding Challenges
- **Context**:
  This section includes practical coding tasks to demonstrate scripting, Python programming, and containerization skills.
  
- **Solutions**:
  - [`prometheus_exporter.py`](Section2-Coding-Challenges/prometheus_exporter.py): A Python-based Prometheus exporter for RabbitMQ, exposing queue metrics like `messages_ready` and `messages_unacknowledged`.
  - [`restart_laravel.sh`](Section2-Coding-Challenges/restart_laravel.sh): A Bash script that monitors CPU usage and restarts the Laravel backend service when usage exceeds 80%.
  - [`Dockerfile`](Section2-Coding-Challenges/Dockerfile): A Dockerfile for containerizing a Laravel application with PHP, Composer, and essential dependencies.

---

## Section Details

### 1. **Section1-General-Knowledge**
- **Context**:
  This section addresses high-level DevOps concepts and system design, focusing on centralized logging and self-healing distributed services.
- **Files**:
  - [`centralized-logging.md`](Section1-General-Knowledge/centralized-logging.md): Describes the design and implementation of a centralized logging system using tools like ELK Stack or Loki.
  - [`self-healing-service.md`](Section1-General-Knowledge/self-healing-service.md): Explains how to design a self-healing distributed service using Kubernetes health checks, retries, and circuit breakers.

---

### 2. **Section2-Coding-Challenges**
- **Context**:
  This section contains solutions to coding challenges, including containerization, monitoring integration, and service management.
- **Files**:
  - [`Dockerfile`](Section2-Coding-Challenges/Dockerfile): A Dockerfile to containerize a Laravel application with PHP, Composer, and necessary extensions.
  - [`prometheus_exporter.py`](Section2-Coding-Challenges/prometheus_exporter.py): A Python script that acts as a Prometheus exporter, exposing RabbitMQ queue metrics like `messages_ready` and `messages_unacknowledged`.
  - [`restart_laravel.sh`](Section2-Coding-Challenges/restart_laravel.sh): A Bash script to monitor CPU usage and restart the Laravel service when usage exceeds a threshold.
  - [`README.md`](Section2-Coding-Challenges/README.md): Contains detailed explanations and usage instructions for the files in this section.

---

### 3. **Section3-Monitoring-Troubleshooting**
- **Context**:
  This section focuses on monitoring solutions and debugging strategies to address performance and reliability issues in modern applications.
- **Files**:
  - [`high_latency_debug.md`](Section3-Monitoring-Troubleshooting/high_latency_debug.md): A detailed guide on debugging high latency in Node.js microservices, including profiling and optimization techniques.
  - [`react_native_monitoring.md`](Section3-Monitoring-Troubleshooting/react_native_monitoring.md): Steps to monitor React Native API endpoints using Prometheus, Grafana, and synthetic monitoring tools.

---

### 4. **Section4-Behavioral**
- **Context**:
  This section includes responses to behavioral questions, highlighting real-world problem-solving scenarios and task prioritization strategies.
- **Files**:
  - [`behavioral-responses.md`](Section4-Behavioral/behavioral-responses.md): Provides examples of improving system performance and handling multiple urgent tasks with prioritization.

---

## Usage Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/namaimichael/DevOps-Engineer-Assessment.git
   cd DevOps-Engineer-Assessment 
   ```

2.	**Navigate to a Section:**
    - General Knowledge: cd Section1-General-Knowledge
    - Coding Challenges: cd Section2-Coding-Challenges
    - Monitoring and Troubleshooting: cd Section3-Monitoring-Troubleshooting
    - Behavioral Responses: cd Section4-Behavioral

3.	**Run the Code:**
    - For Python or Bash scripts:
    ```bash 
    python Section2-Coding-Challenges/prometheus_exporter.py
    Section2-Coding-Challenges/restart_laravel.sh
    ```

---
## Summary

This repository provides comprehensive solutions to the DevOps Engineer Technical Assessment, demonstrating skills in system design, coding, monitoring, and problem-solving. Explore each section for detailed explanations, implementations, and real-world examples.