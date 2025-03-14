def change_buoyancy(action):
    if action == "inflate":
        print("Inflating bladder... Float rising.")
    elif action == "deflate":
        print("Deflating bladder... Float sinking.")
    else:
        print("Invalid action")

# Example usage
if __name__ == "__main__":
    change_buoyancy("inflate")
