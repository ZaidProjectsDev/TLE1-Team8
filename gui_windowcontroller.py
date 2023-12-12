import tkinter as tk
from windowfinder import get_all_windows, create_window_list
import narrator
from windowdefinition import get_updated_window_status, update_active_window, get_active_window


class GuiWindowController:
    automatic_tut_message_delay = 180 #MODIFY THIS NUMBER IF YOU FIND THE AUTO NARRATION TO BE ANNOYING (used to be 30, now 180)
    current_automatic_tut_message_delay = 0
    automatic_tut_message_alt = 'You can press Q to scan and get a narration of your active game window.'
    automatic_tut_message= 'Use TAB and Spacebar to navigate the program. You can press ENTER to automatically start narration of your highlighted game window.'
    def __init__(self, root, shared_models, lang, ):
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
        self.label_instructions = tk.Label = tk.Label(
            text=self.automatic_tut_message,
            font=("Arial", 14),
            padx=20,
            pady=10,
        )
        self.label_instructions.pack()
        self.bind_button_to_narrator(self.label_instructions)

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




    def interrupt_tut_message_timer(self):
        self.current_automatic_tut_message_delay = 0
    def run_automatic_tut_message(self):
        if self.current_automatic_tut_message_delay >= self.automatic_tut_message_delay:
            if self.shared_models.screenReaderEnabled:
                narrator.speak(self.automatic_tut_message_alt, True, False, True)
            else:
                narrator.speak(self.automatic_tut_message, True, False, True)
            self.current_automatic_tut_message_delay = 0
        else:
            if narrator.check_busy() is True:
                self.current_automatic_tut_message_delay = 0
            self.current_automatic_tut_message_delay += 0 #disabled change to 0, change to 1 to work
            #print(self.current_automatic_tut_message_delay)
        self.root.after(250, self.run_automatic_tut_message)
    def close_program(self):
        self.root.destroy()  # Destroy the main (root) window

    def on_leave(self, e):
        print(e.widget)

    def bind_button_to_narrator(self, button):
        button.bind("<Enter>", self.on_enter)
        button.bind("<FocusIn>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        button.bind("<FocusOut>", self.on_leave)

    def on_enter(self, e):

        # narrator.saySelected(e.widget['text'],True)
        if narrator.is_speaking() and narrator.current_text_wait_to_finish is False:
            narrator.stop()
            self.interrupt_tut_message_timer()
          #  self.interrupt_tut_message_timer()

        if not narrator.is_speaking() and narrator.current_text_wait_to_finish is False:
            t = e.widget['text']
            self.interrupt_tut_message_timer()
        #    self.interrupt_tut_message_timer()
            self.run_pyttsx3(t)
            print(e.widget)

    def run_pyttsx3(self, text):
        narrator.speak(text, False)

    def update_active_game_window(self):
        if get_active_window().getTitle() == '' or get_active_window().getTitle() == '':
            self.label_active_game.configure(text=self.lang.get_translation('bark_no_game_window'))
            self.btn_screen_reader_window.configure(state=tk.DISABLED)
        else:
            self.label_active_game.configure(
                text=self.lang.get_translation('bark_current_game_window') + str(get_active_window().getTitle()))
            self.btn_screen_reader_window.configure(state=tk.NORMAL)
            self.update_screen_reader_button()
            self.shared_models.activeUIWindow = get_active_window()
        self.root.after(100, self.update_active_game_window)

    def update_screen_reader_button(self):
        if self.shared_models.screenReaderEnabled:
            self.btn_screen_reader_window.configure(text=self.lang.get_translation('disable_screen_reader_window'))
            self.label_instructions.configure(text=self.automatic_tut_message_alt)
            self.btn_screen_reader_window.configure(command=self.shared_models.uninitalizeVision)
        else:
            self.btn_screen_reader_window.configure(text=self.lang.get_translation('enable_screen_reader_window'))
            self.label_instructions.configure(text=self.automatic_tut_message)
            self.btn_screen_reader_window.configure(command=self.shared_models.initalizeVision)

    def game_window_finder(self):
        tk.Canvas(self.root, width=400, height=300, bg="white")  # Set canvas background color
        get_all_windows()
        window_finder_root = tk.Tk()

        canvas2 = tk.Canvas(self.root, width=720, height=600, bg="white")  # Set canvas background color
        canvas2.pack()
        window_finder_root.focus_force()
        create_window_list(window_finder_root, canvas2, )

        print("Looking for game windows.")

    def update(self):
        if not self.root.winfo_exists():
            self.root.destroy()
            return

        self.update_active_game_window()
        self.run_automatic_tut_message()
        self.root.mainloop()
