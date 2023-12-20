import threading
import os

import pygame

import gamecapture
import speaker
import windowdefinition
from inputchecker import keyboardInput
import gui_windowcontroller
import shared_model as current_vars
import localization
import tkinter as tk
import narrator
import windowcapturehotkeytest

pygame.init()
shared_models = current_vars.SharedModels()
current_vars.setCurrentSharedModel(shared_models)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lang = localization.Localization()

root = tk.Tk()
# hide the main window
root.withdraw()

gui = gui_windowcontroller.GuiWindowController(root, shared_models, lang)
# buttons
narrator.speak(lang.get_translation('tts_app_started'), True, False, True)


def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            print('music end event')
            narrator.reset_speaking_vars()

    root.after(100, check_event)


MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)


def update_program():
    keyboard_update()
    gamecapture.shared_models = shared_models
    windowdefinition.get_updated_window_status()
    gui.update()
    root.after(100, update_program)


def keyboard_update():
    # if windowdefinition.activeWindow is not None and windowdefinition.activeWindow.title is not '':
    windowcapturehotkeytest.check_for_game_window(shared_models)
    keyboardInput(windowdefinition.active_window.title, shared_models)
    check_event()
    root.after(50, keyboard_update)



update_program()
root.mainloop()