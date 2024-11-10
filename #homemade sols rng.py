import time
import keyboard
import random
import pyautogui
import sys  # For clean program exit
import os

# Maximum value for the roll
max_value = 1000

# Global variable for roll count
roll_count = 0

# Function to simulate smooth dragging
def smooth_drag(start_x, start_y, end_x, end_y, steps=100):
    delta_x = (end_x - start_x) / steps
    delta_y = (end_y - start_y) / steps

    for i in range(steps):
        current_x = start_x + delta_x * i
        current_y = start_y + delta_y * i
        pyautogui.moveTo(current_x, current_y)
        time.sleep(1 / 165)

# Main function to manage user interaction
def main():
    global roll_count

    print("Hello!")
    user_input = input("Type 'hi': ")

    if user_input.lower() == "hi":
        print("Want to roll? (press 'y' to roll or 'n' to exit)")

        while True:
            if keyboard.is_pressed("y"):
                print("Rolling...")
                time.sleep(0.5)  # Delay for suspense

                # Implement a more controlled bias factor
                bias_factor = (roll_count + 1) / (roll_count + 2)

                # RNG with bias
                roll_value = random.randint(1, max_value)
                biased_roll = int(roll_value * bias_factor)
                biased_roll = min(biased_roll, max_value)  # Ensure it's within range

                print(f"You have rolled a {biased_roll}")
                roll_count += 1

                print("\nPress 'y' to roll again or 'n' to exit.")
                while keyboard.is_pressed("y"):  # Prevents multiple rolls
                    pass

                time.sleep(0.5)  # Pause before continuing with the next roll

            elif keyboard.is_pressed("n"):
                print("Exiting...")
                break

            # Clean exit check
            if keyboard.is_pressed("esc"):
                print("Exiting program...")
                time.sleep(0.2)
                sys.exit()

            time.sleep(0.1)  # Prevents high CPU usage (your welcome)

    else:
        print("You didn't say hi to me... GET OUT!!!")
        
        start_x, start_y = pyautogui.position()
        smooth_drag(start_x, start_y, 1893, 0)  # Move cursor to (1893, 0) only here
        
        os.startfile("tuco-get-out.mp3")  # Opens the .mp3 file
        time.sleep(1.2)
        pyautogui.click()

if __name__ == "__main__":
    main()
