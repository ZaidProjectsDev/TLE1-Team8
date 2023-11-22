import cv2 as cv
import numpy as np
import os

import gamecapture
import speaker
import windowdefinition
from gamecapture import scan_game_window
from inputchecker import keyboardInput
import gui_windowcontroller
import shared_model as current_vars

shared_models = current_vars.SharedModels()
current_vars.setCurrentSharedModel(shared_models)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import localization

lang = localization.Localization()
import tkinter as tk
from screen_reader import toggle_screen_reader
error_reporter = speaker.SpeakerObject()
message_reporter = speaker.SpeakerObject()

root = tk.Tk()

# buttons
btn_language = tk.Button(
    text=lang.get_translation('language_toggle_button'),
    command=lambda: lang.set_language(lang.language),
    bg="green",
    fg="white",
    font=("Arial", 14),
    padx=20,
    pady=10,
)
btn_language.pack()
message_reporter.say(lang.get_translation('tts_app_started'))

# # Styling
# root.geometry("400x300")  # Set the window size
# root.configure(bg="white")  # Set the background color
#
# canvas1 = tk.Canvas(root, width=400, height=300, bg="white")  # Set canvas background color
# canvas1.pack()
#
# button1 = tk.Button(
#     text="Enable Screen Reader",
#     command=lambda: toggle_screen_reader(button1, canvas1, root),
#     bg="green",
#     fg="white",
#     font=("Arial", 14),
#     padx=20,
#     pady=10,
# )
# def keyboard_update():
#     keyboardInput(game_window_name)
#     root.after(10,keyboard_update)
#
# canvas1.create_window(200, 150, window=button1)

# while (True):
#     keyboardInput(game_window_name)
#     if(cv.waitKey(1)==ord('p')):
#         cv.destroyAllWindows()
#         break

def update_program():
    keyboard_update()
    gui_windowcontroller.shared_models = shared_models
    gamecapture.shared_models = shared_models
    gui_windowcontroller.update()
    root.after(5, update_program)


def keyboard_update():
    # if windowdefinition.activeWindow is not None and windowdefinition.activeWindow.title is not '':
    keyboardInput(windowdefinition.activeWindow.title, shared_models)

    root.after(10, keyboard_update)




update_program()
root.mainloop()
