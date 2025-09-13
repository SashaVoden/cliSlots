# Imports
import random
import time
from pynput import keyboard
import os

#Logic
first_number = 0
second_number = 0
third_number = 0
message = ""

RED = "\033[31m"
RESET = "\033[0m"

def strike(text: str) -> str:
    return f"\033[9m{text}\033[0m"

def print_ui():
    os.system("cls" if os.name == "nt" else "clear")
    ui = f"""
                        _____________________
                        |                   |
                        |   _____________   | {RED}(0){RESET}
                        |   |   |   |   |   |  |
                        |   | {RED}{first_number}{RESET} | {RED}{second_number}{RESET} | {RED}{third_number}{RESET} |   |  |
                        |   |___|___|___|   |  |
                        |                   |  |
                        |                   |==0
                        |                   |
                        |___________________|  space = spin, esc = exit
                       /                     \\
                      /                       \\  {message}
                     /                         \\
                    /___________________________\\
    """
    print(ui)
def spin():
    global first_number, second_number, third_number, message
    message = ""
    for i in range(30):
        first_number = random.randint(1, 7)
        print_ui()
        time.sleep(0.05)
    for o in range(30):
        second_number = random.randint(1, 7)
        print_ui()
        time.sleep(0.05)
    for a in range(30):
        third_number = random.randint(1, 7)
        print_ui()
        time.sleep(0.05)
    if first_number == second_number == third_number:
        message = "Jackpot!"
    else:
        message = "Try again!"
    print_ui()

def on_press(key: keyboard.Key | keyboard.KeyCode | None) -> None:
    if key == keyboard.Key.space:
        spin()

    elif key == keyboard.Key.esc:
        listener.stop()

print_ui()
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
