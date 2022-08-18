#!/usr/bin/env python3

# Libraries
import os           # For installing pyautogui
import sys          # For timer
import time         # For sleep
import threading    # For thread
import itertools    # For print items in timer

# Trying to import pyautogui. If there is no pyautogui installed, then it will install it
try:
    import pyautogui as pag
except:
    print("pyautogui is not installed! installing pyautogui for you...\n")
    os.system("python3 -m pip install pyautogui")

# Set done variable to "False" for timer
# We will break the timer funcion if we set this variable to "True"
done = False

# Timer function
def timer():
    List = ["5", "4", "3", "2", "1", "Spam Started"]
    for item in itertools.cycle(List):
        if done:
            break
        sys.stdout.write('\rTimer: ' + item) # \r : this will edit previous item
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('')

timer = threading.Thread(target=timer)

print(f"You have 5 seconds from now to choose target! Press ctrl+c to stop!")

timer.start()  # Start timer
time.sleep(5)  # Wait for 5 seconds
done = True    # Stop timer

print("\nSpam Started")

# Read spam file
# This will read whole file, if you want to spam line by line try "readlines()" and use "For text in lines" loop 
# Like this:
#
# with open("SpamText.txt", "r") as text:
#     lines = text.readlines()
#     for text in lines:
#         pag.typewrite(text.strip("\n"))
#         pag.press("enter")
#
#
# this loop will break after last line!

text = open("SpamText.txt", "r").read()

# Infinite loop
while True:
    pag.typewrite(text)
    pag.press("enter")

# Break the loop with "ctrl+c" or "ctrl+z"
# SlavPH