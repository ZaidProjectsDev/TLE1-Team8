import tkinter as tk
from screen_reader import toggle_screen_reader, read_game_area

root = tk.Tk()
root.title("Screen Reader App")

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
canvas1.create_window(200, 150, window=button1)

# Start the screen reader function
root.after(1000, read_game_area)

root.mainloop()
