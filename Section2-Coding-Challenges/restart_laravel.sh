#!/bin/bash

# Monitor CPU usage and restart Laravel service if usage exceeds threshold
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
THRESHOLD=80.0

if (( $(echo "$CPU_USAGE > $THRESHOLD" | bc -l) )); then
    echo "$(date): High CPU usage detected: $CPU_USAGE%. Restarting Laravel service..."
    systemctl restart laravel-backend.service
    echo "$(date): Laravel backend service restarted."
else
    echo "$(date): CPU usage is normal: $CPU_USAGE%."
fi