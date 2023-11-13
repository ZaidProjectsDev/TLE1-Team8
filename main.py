import cv2 as cv
import numpy as np
import os 
from gamecapture import scan_game_window
from inputchecker import keyboardInput
os.chdir(os.path.dirname(os.path.abspath(__file__)))
canvas_img_path_real = 'img-test/ref/tew2/tew2_ref_2.png'
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.png'
game_window_name = 'The Evil Within 2' #Replace this with what is relevant to your use case.


#points = findClickPositions(needle_img_path_real,canvas_img_path_real,0.8,debug_mode='rectangles');
#print(points)

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
canvas1.create_window(200, 150, window=button1)
while (True):
    keyboardInput(game_window_name)
    if(cv.waitKey(1)==ord('p')):
        cv.destroyAllWindows()
        break
root.mainloop()
