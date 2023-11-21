import cv2 as cv
import numpy as np
import os 
import pyttsx3
import speech_recognition as sr
import pyaudio
from gamecapture import scan_game_window
from inputchecker import keyboardInput

os.chdir(os.path.dirname(os.path.abspath(__file__)))
canvas_img_path_real = 'img-test/ref/tew2/tew2_ref_2.png'
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.png'
game_window_name = 'Ratchet & Clank: Rift Apart v1.922.0.0'  # Replace this with what is relevant to your use case.

import tkinter as tk
from screen_reader import toggle_screen_reader

root = tk.Tk()
root.title("Screen Reader App")

# Styling
root.geometry("400x300")  # Set the window size
root.configure(bg="white")  # Set the background color

canvas1 = tk.Canvas(root, width=400, height=300, bg="white")  # Set canvas background color
canvas1.pack()

button1 = tk.Button(
    text="Enable Screen Reader",
    command=lambda: toggle_screen_reader(button1, canvas1, root),
    bg="green",
    fg="white",
    font=("Arial", 14),
    padx=20,
    pady=10,
)
def keyboard_update():
    keyboardInput(game_window_name)
    root.after(10,keyboard_update)

canvas1.create_window(200, 150, window=button1)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000  # Adjust this value based on your environment

def voice_command():
    # Listen for a voice command
    with sr.Microphone() as source:
        print("Listening for a command...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            
            print(f"Command recognized: {command}")  # Add this line to print the recognized command

            if "enable" in command:
                toggle_screen_reader(button1, canvas1, root)
            elif "disable" in command:
                toggle_screen_reader(button1, canvas1, root)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")

    root.after(10, voice_command)

# Start the voice recognition function
root.after(1000, voice_command)
root.mainloop()
