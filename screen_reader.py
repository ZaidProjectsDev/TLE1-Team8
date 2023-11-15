import cv2
import numpy as np
import pyautogui
import pytesseract
import pyttsx3
import threading

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

    def on_hover(event):
        if screen_reader_enabled:
            engine.say("Disable Screen Reader")
        else:
            engine.say("Enable Screen Reader")
        engine.runAndWait()

    def on_leave(event):
        engine.stop()  # Stop the ongoing speech

    screen_reader_enabled = not screen_reader_enabled
    if screen_reader_enabled:
        button1.config(text="Disable Screen Reader", bg="red")
        threading.Thread(target=enable_message).start()
    else:
        button1.config(text="Enable Screen Reader", bg="green")
        threading.Thread(target=disable_message).start()

    # Bind events to functions
    button1.bind("<Enter>", on_hover)
    button1.bind("<Leave>", on_leave)

def enable_message():
    # Enable message
    engine.say("Screen reader enabled. Have Fun!")
    engine.runAndWait()

def disable_message():
    # Disable message
    engine.say("Screen reader disabled. Goodbye!")
    engine.runAndWait()

def read_game_area():
    if screen_reader_enabled:
        # Read and describe the game area using OpenCV
        screenshot = capture_game_area()
        text = perform_ocr(screenshot)
        describe_text(text)

def capture_game_area():
    # OpenCV to capture the game area
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    return screenshot_cv

def perform_ocr(image):
    # Use pytesseract for OCR on the given image
    # You may need to adjust the region based on the game's UI
    region_of_interest = image[100:300, 100:300]  # Example region
    text = pytesseract.image_to_string(region_of_interest)
    return text

def describe_text(text):
    # Use text-to-speech to describe the extracted text
    engine.say(text)
    engine.runAndWait()

# Trigger the initial announcement when the program starts
engine.say("Program has started")
engine.runAndWait()
