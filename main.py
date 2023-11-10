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
