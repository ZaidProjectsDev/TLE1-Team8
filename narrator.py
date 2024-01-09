import threading
import time
from tkinter import *
import pyttsx3
import pygame
import localization as lang

pygame.mixer.init()
engine = pyttsx3.init()
root = Tk()

current_text = ""
current_text_wait_to_finish = False


# Check if the narrator is speaking. This can help with interruptions.
def is_speaking():
    global current_text_wait_to_finish, current_text


    init_or_die()
    if pygame.mixer.music.get_busy():
        print('Busy talking ' + str(current_text) + 'should wait to finish : ' + str(current_text_wait_to_finish))
        return True
    else:
        current_text_wait_to_finish = False
        current_text = ""
        return False

def check_busy():
    # skip
    # return False
    return pygame.mixer.music.get_busy()
def init_or_die():
    if not pygame.mixer.get_init():
        pygame.mixer.init()


def speak(text, wait_to_finish=False, use_naviagtional_starter=False, block_main_thread=False):
    #skip
    # return
    global current_text, current_text_wait_to_finish
    if current_text == text:
        return
    if is_speaking() and wait_to_finish is False and block_main_thread is False:
        return

    if current_text != "":
        if current_text_wait_to_finish is True and is_speaking() and wait_to_finish is False and block_main_thread is False:
            return
        else:
            stop()

    current_text = text
    current_text_wait_to_finish = wait_to_finish

    if use_naviagtional_starter is True:
        new_text = "Selected " + str(text)
        text = new_text
        current_text = text
    init_or_die()

    def speak_thread():
        outfile = "temp.wav"
        engine.save_to_file(text, outfile)
        engine.runAndWait()
        init_or_die()
        pygame.mixer.music.load(outfile)
        pygame.mixer.music.play()

    if block_main_thread is False:
        # Create a new thread and start it
        speak_thread = threading.Thread(target=speak_thread)
        speak_thread.start()
    else:
        init_or_die()
        pygame.mixer.music.unload()
        outfile = "temp_b.wav"

        engine.save_to_file(text, outfile)
        engine.runAndWait()

        a = pygame.mixer.Sound("temp_b.wav")
        print("length", a.get_length())
        pygame.mixer.music.load(outfile)
        pygame.mixer.music.play()
        time.sleep(a.get_length()+0.1)


def reset_speaking_vars():
    global current_text, current_text_wait_to_finish
    current_text = ''
    current_text_wait_to_finish = False
    stop()


def stop():
    init_or_die()
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()


def pause():
    init_or_die()
    pygame.mixer.music.pause()


def unpause():
    init_or_die()
    pygame.mixer.music.unpause()
