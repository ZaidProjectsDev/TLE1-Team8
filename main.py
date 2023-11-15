import cv2 as cv
import numpy as np
import os 
from gamecapture import scan_game_window
from inputchecker import keyboardInput
os.chdir(os.path.dirname(os.path.abspath(__file__)))
canvas_img_path_real = 'img-test/ref/tew2/tew2_ref_2.png'
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.png'
game_window_name = 'Ratchet & Clank: Rift Apart v1.922.0.0' #Replace this with what is relevant to your use case.


#points = findClickPositions(needle_img_path_real,canvas_img_path_real,0.8,debug_mode='rectangles');
#print(points)

import tkinter as tk
import pyttsx3
from screen_reader import toggle_screen_reader, read_game_area

root = tk.Tk()
root.title("Screen Reader App")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

canvas1 = tk.Canvas(root, width=500, height=500)
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

<<<<<<< main
def keyboard_update():
    keyboardInput(game_window_name)
    root.after(10,keyboard_update)

canvas1.create_window(200, 150, window=button1)

# while (True):
#     keyboardInput(game_window_name)
#     if(cv.waitKey(1)==ord('p')):
#         cv.destroyAllWindows()
#         break
keyboard_update()

# Bind events for hover in main.py
def on_hover(event):
    engine.say("Enable Screen Reader")
    engine.runAndWait()

def on_leave(event):
    engine.stop()  # Stop the ongoing speech

# Bind events to functions
button1.bind("<Enter>", on_hover)
button1.bind("<Leave>", on_leave)

canvas1.create_window(200, 150, window=button1)

# Start the screen reader function
root.after(1000, read_game_area)

root.mainloop()
