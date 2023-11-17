import windowdefinition
import windowfinder
import tkinter as tk
import variables
from localization import Localization
shared_models =None
from screen_reader import toggle_screen_reader

chosen_game_window = None
lang = Localization()
root = tk.Tk()
root.title("Screen Reader App")

# Styling
root.geometry("640x480")  # Set the window size
root.configure(bg="white")  # Set the background color

label_active_game = tk.Label(text=lang.get_translation('bark_current_game_window'),
                             font=("Arial", 14),
                             padx=20,
                             pady=10,
                             )
label_active_game.pack()
btn_screen_reader_window = tk.Button(
    text=lang.get_translation('enable_screen_reader_window'),
    bg="green",
    fg="white",
    command=lambda: shared_models.initalizeVision(),
    font=("Arial", 14),
    padx=20,
    pady=10,
    state=tk.DISABLED,
)
btn_screen_reader_window.pack()
btn_find_game_window = tk.Button(
    text=lang.get_translation('find_game_windows'),
    command=lambda: game_window_finder(),
    bg="green",
    fg="white",
    font=("Arial", 14),
    padx=20,
    pady=10,
)
btn_find_game_window.pack()


def update_active_game_window():
    if windowdefinition.activeWindow == '':
        label_active_game.configure(text=lang.get_translation('bark_no_game_window'))
        btn_screen_reader_window.configure(state=tk.DISABLED)
    else:
        label_active_game.configure(
            text=lang.get_translation('bark_current_game_window') + windowdefinition.activeWindow.title)
        btn_screen_reader_window.configure(state=tk.NORMAL)
        shared_models.activeUIWindow = windowdefinition.activeWindow
    root.after(100, update_active_game_window)


def game_window_finder():
    tk.Canvas(root, width=400, height=300, bg="white")  # Set canvas background color
    windowfinder.get_all_windows()
    window_finder_root = tk.Tk()

    canvas2 = tk.Canvas(root, width=720, height=600, bg="white")  # Set canvas background color
    canvas2.pack()
    windowfinder.create_window_list(window_finder_root, canvas2)

    print("Looking for game windows.")


def update():
    update_active_game_window()
    root.mainloop()
