import time
import keyboard
import random
import _random
import os
import pyautogui
import sys  # For clean program exit

# Maximum value for the roll
max_value = 1000  # Adjust this to a reasonable number (increase to your liking however dont go too high cuz it prob will break lol -HAPPENED TO ME A LOT OF TIMES-)

# Starting roll number
roll_count = 0

# Function to simulate smooth dragging
def smooth_drag(start_x, start_y, end_x, end_y, steps=75):
    # Calculate the distance to move in each step
    delta_x = (end_x - start_x) / steps
    delta_y = (end_y - start_y) / steps

    # Move the cursor in small steps to simulate smooth dragging
    for i in range(steps):
        current_x = start_x + delta_x * i
        current_y = start_y + delta_y * i
        pyautogui.moveTo(current_x, current_y)
        time.sleep(1 / 165)  # Sleep to simulate ~165 FPS (roughly 0.00606s per frame)

# Main function to manage user interaction
def main():
    print("Hello!")
    user_input = input("Type 'hi': ")

    if user_input.lower() == "hi":
        print("Want to roll? (press 'y' to roll or 'n' to exit)")

        while True:
            if keyboard.is_pressed("y"):
                print("Rolling...")
                time.sleep(0.5)  # Delay for suspense because yippee (change if your too lazy to wait HALF A SECOND)

                bias_factor = roll_count / (roll_count + 1)  # bias because why not haha you need to gamble more!!!

                # RNG
                roll_value = random.randint(1, max_value)

                # More rigging cuz funny
                biased_roll = int(roll_value * bias_factor)
                biased_roll = min(biased_roll, max_value)  # Ensure it's within the max_value range

                print(f"You have rolled a {biased_roll}")  # gonna point out this is kinda how a slot machine works (not actually but you get the point they're rigged)
                # Increment roll count after each roll
                roll_count += 1

                print("\nPress 'y' to roll again or 'n' to exit.")
                while keyboard.is_pressed("y"):
                    pass  # Prevents multiple rolls from holding "Y" key
                
                # Smooth drag to a specific position
                start_x, start_y = pyautogui.position()  # Get current mouse position
                smooth_drag(start_x, start_y, 1893, 0)  # Drag smoothly to (1893, 0)
                time.sleep(0.5)  # Delay before allowing the next drag

            elif keyboard.is_pressed("n"):
                print("Exiting...")
                break

            # Optionally add a break condition for exiting cleanly after all actions complete
            if keyboard.is_pressed("esc"):  # Allow exit via 'esc' key
                print("Exiting program...")
                time.sleep(0.2)  # Slight delay to ensure the message prints
                sys.exit()

            time.sleep(0.1)  # Saves your CPU (your welcome :D)

    else:
        print("You didn't say hi to me... GET OUT!!!")
        
        start_x, start_y = pyautogui.position()  # Get current mouse position
        smooth_drag(start_x, start_y, 1893, 0)  # Move cursor smoothly to (1893, 0)
        
        os.startfile("tuco-get-out.mp3")  # Open .mp3 file
        time.sleep(1.2)
        pyautogui.click()

if __name__ == "__main__":
    main()



    #download link if you don't already have the mp3 (link --> https://www.myinstants.com/en/instant/tuco-get-out-30566/?utm_source=copy&utm_medium=share)