import time

def log_data(data):
    with open("logs/float_data.csv", "a") as file:
        file.write(f"{time.time()},{data}\n")

# Example usage
if __name__ == "__main__":
    log_data("Simulated pressure: 1013.25 hPa")
