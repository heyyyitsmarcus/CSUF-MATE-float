# src/main.py

import time
from src.buoyancy import adjust_depth
from src.data_logger import collect_sensor_data
from test import transmit_data
from src.sensor_reader import read_sensor_data  # Placeholder for real sensors
import os

# File to store sensor data
DATA_FILE = "logs/sensor_data.csv"

# Simulated depth (starts at surface)
depth = 0  # 0 = surface, positive values = deeper

# --------------------------
# Main Logic Loop
# --------------------------
def simulate_mission():
    print("Starting float simulation...")

    # Simulate mission: Collect data while submerged, then transmit on surfacing
    # Sink to 3m depth
    adjust_depth(3)
    
    # Collect sensor data every 5 seconds for 30 seconds
    for _ in range(6):  # Simulate 30 seconds of data collection
        collect_sensor_data(depth, DATA_FILE)  # Collect and log data
        time.sleep(5)  # Wait 5 seconds before next reading

    # Surface to depth 0 (simulating surfacing)
    adjust_depth(0)

    # After surfacing, transmit collected data over Bluetooth
    if depth == 0:  # Check if the float has reached the surface
        transmit_data(DATA_FILE)

    print("Mission complete.")

if __name__ == "__main__":
    simulate_mission()

