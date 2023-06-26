import random
import time

# Function to generate a random snowflake character
def generate_snowflake():
    snowflakes = ["❅", "❆", "❄"]
    return random.choice(snowflakes)

# Function to generate a random position within the command prompt window
def generate_position(width, height):
    x = random.randint(1, width)
    y = random.randint(1, height)
    return x, y

# Function to clear the command prompt window
def clear_screen():
    print("\033c", end="")

# Get the width and height of the command prompt window
# Note: This may not work on all operating systems or command prompt emulators
# You may need to adjust the values manually.
width = 80
height = 25

# Clear the screen
clear_screen()

# Animation loop
while True:
    # Generate a random snowflake character and position
    snowflake = generate_snowflake()
    x, y = generate_position(width, height)

    # Move the cursor to the random position
    print(f"\033[{y};{x}H{snowflake}", end="")

    # Sleep for a short duration to control the animation speed
    time.sleep(0.1)

    # Clear the current snowflake by printing a space character
    print(f"\033[{y};{x}H ", end="")
