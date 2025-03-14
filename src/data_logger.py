# src/data_logger.py

import time
import random

def collect_sensor_data(depth, file_path):
    """Simulate collecting sensor data and store it in a CSV file."""
    fake_temperature = round(random.uniform(10, 30), 2)  # Fake temperature
    fake_pressure = round(1000 + depth * 10, 2)  # Simulated pressure based on depth
    fake_data = f"{time.time()},{fake_temperature},{fake_pressure}\n"

    # Log the data to a file
    with open(file_path, "a") as file:
        file.write(fake_data)
    
    print(f"Collected Data: {fake_data.strip()}")

