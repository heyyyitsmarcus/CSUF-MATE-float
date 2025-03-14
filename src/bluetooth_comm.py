# src/bluetooth_comm.py

import bluetooth
import os

def transmit_data(file_path):
    """Send stored data via Bluetooth when surfaced."""
    if not os.path.exists(file_path):
        print("No data to send.")
        return

    try:
        BT_SERVER_MAC = "XX:XX:XX:XX:XX:XX"  # Replace with actual Bluetooth MAC address
        BT_PORT = 1

        print("Attempting Bluetooth connection...")
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((BT_SERVER_MAC, BT_PORT))
        print("Connected. Sending data...")

        with open(file_path, "r") as file:
            data = file.read()
            sock.send(data)

        print("Data transmission complete.")
        sock.close()

        # Clear the data after transmission
        os.remove(file_path)
    except Exception as e:
        print(f"Bluetooth transmission failed: {e}")

