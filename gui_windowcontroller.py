import tkinter as tk
from windowfinder import get_all_windows, create_window_list
import narrator
from windowdefinition import get_updated_window_status, update_active_window, get_active_window

class GuiWindowController:
    def __init__(self, root, shared_models, lang,):
        self.root = root
        self.root.title("Screen Reader App")
        self.root.geometry("640x480")
        self.root.configure(bg="white")
        self.shared_models = shared_models
        self.lang = lang


        self.label_active_game = tk.Label(
            text=lang.get_translation('bark_current_game_window'),
            font=("Arial", 14),
            padx=20,
            pady=10,
        )
        self.label_active_game.pack()
        self.bind_button_to_narrator(self.label_active_game)

        self.btn_find_game_window = tk.Button(
            text=lang.get_translation('find_game_windows'),
            command=self.game_window_finder,
            bg="green",
            fg="white",
            font=("Arial", 14),
            padx=20,
            pady=10,
        )
        self.btn_find_game_window.pack()
        self.bind_button_to_narrator(self.btn_find_game_window)

        self.btn_screen_reader_window = tk.Button(
            text=lang.get_translation('enable_screen_reader_window'),
            bg="green",
            fg="white",
            command=self.shared_models.initalizeVision,
            font=("Arial", 14),
            padx=20,
            pady=10,
            state=tk.DISABLED,
        )
        self.btn_screen_reader_window.pack()
        self.bind_button_to_narrator(self.btn_screen_reader_window)


    def close_program(self):
        self.root.destroy()  # Destroy the main (root) window
    def on_leave(self, e):
            print(e.widget)

    def bind_button_to_narrator(self, button):
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        button.bind("<Leave>", self.on_leave)
        button.bind("<FocusOut>", self.on_leave)

    def on_enter(self, e):

        # narrator.saySelected(e.widget['text'],True)
        if narrator.is_speaking() and narrator.current_text_wait_to_finish is False:
            narrator.stop()

        if not narrator.is_speaking() and narrator.current_text_wait_to_finish is False:
            t = e.widget['text']
            self.run_pyttsx3(t)
            print(e.widget)

    def run_pyttsx3(self, text):
        narrator.speak(text,False)

    def update_active_game_window(self):
        if get_active_window().getTitle() == '' or get_active_window().getTitle() == '':
            self.label_active_game.configure(text=self.lang.get_translation('bark_no_game_window'))
            self.btn_screen_reader_window.configure(state=tk.DISABLED)
        else:
            self.label_active_game.configure(
                text=self.lang.get_translation('bark_current_game_window') + str(get_active_window().getTitle()))
            self.btn_screen_reader_window.configure(state=tk.NORMAL)
            self.shared_models.activeUIWindow = get_active_window()
        self.root.after(100, self.update_active_game_window)

    def game_window_finder(self):
        tk.Canvas(self.root, width=400, height=300, bg="white")  # Set canvas background color
        get_all_windows()
        window_finder_root = tk.Tk()

        canvas2 = tk.Canvas(self.root, width=720, height=600, bg="white")  # Set canvas background color
        canvas2.pack()
        window_finder_root.focus_force()
        create_window_list(window_finder_root, canvas2,)

        print("Looking for game windows.")

    def update(self):
        if not self.root.winfo_exists():
            self.root.destroy()
            return
        self.update_active_game_window()
        self.root.mainloop()
