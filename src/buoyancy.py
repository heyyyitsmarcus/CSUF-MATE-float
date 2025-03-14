# src/buoyancy.py

import time

# Simulated depth (starts at surface)
depth = 0  # 0 = surface, positive values = deeper

def adjust_depth(target_depth):
    """Simulate changing depth using a buoyancy system (syringe mechanism)."""
    global depth
    print(f"Adjusting depth from {depth}m to {target_depth}m...")

    while depth != target_depth:
        if depth < target_depth:
            depth += 1  # Simulate sinking
        else:
            depth -= 1  # Simulate rising

        print(f"Current depth: {depth}m")
        time.sleep(1)  # Simulate delay for each depth change

    print("Target depth reached.")

