import tkinter as tk
import pyttsx3

screen_reader_enabled = False
button1 = None
canvas1 = None
root = None

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def toggle_screen_reader(button, canvas, main_root):
    global screen_reader_enabled
    global button1
    global canvas1
    global root
    button1 = button
    canvas1 = canvas
    root = main_root
    screen_reader_enabled = not screen_reader_enabled

    if screen_reader_enabled:
        button1.config(text="Disable Screen Reader", bg="red")
        enable_message()
        # Include logic here to actually enable the screen reader

    else:
        button1.config(text="Enable Screen Reader", bg="green")
        disable_message()
        # Include logic here to actually disable the screen reader

# You can add other functionality here without displaying a label

# For example, a function that reads out the game area
def read_game_area():
    if screen_reader_enabled:
        # Your code to read and describe the game area
        pass

def enable_message():
    # Enable message
    engine.say("Screen reader enabled. Click on objects to hear descriptions.")
    engine.runAndWait()

def disable_message():
    # Disable message
    engine.say("Screen reader disabled. Goodbye!")
    engine.runAndWait()
