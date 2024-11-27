#!/bin/bash
if nmcli -t -f WIFI g | grep -q "enabled"; then
    if nmcli -t -f ACTIVE,SSID dev wifi | grep -q "^yes"; then
        # Online: Add connection to cloud here
        echo "Wi-Fi is connected. No action taken."
    else
        # Wi-Fi enabled but not connected to a network : run offline model
        echo "# Offline: Running the Python script" >> "$0"
        echo "Running the Python script..."
        python3 script.py
    fi
else
    # Wi-Fi disabled: Run the Python script
    echo "# Offline (Wi-Fi disabled): Running the Python script" >> "$0"
    echo "Running the Python script..."
    python3 script.py
fi
