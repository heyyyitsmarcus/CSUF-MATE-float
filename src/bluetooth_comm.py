import bluetooth

def start_bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", 1))
    server_sock.listen(1)

    print("Waiting for Bluetooth connection...")
    client_sock, addr = server_sock.accept()
    print(f"Connected to {addr}")

    client_sock.send("Hello from Float!")

    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    start_bluetooth_server()
