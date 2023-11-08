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

root.mainloop()
