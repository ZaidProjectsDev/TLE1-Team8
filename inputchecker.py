import keyboard
import pygame
from gamecapture import scan_game_window

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))  # Delay to ensure the sound plays completely
    except pygame.error as e:
        print("Error playing sound:", e)
    finally:
        pygame.mixer.quit()


def scanner():
    play_sound('TLE1-Team8\ding-36029.wav')
    print(scan_game_window('Netflix - Google Chrome'))
    keyboardInput()

def keyboardInput():
    keyboard.wait("q")
    scanner()

keyboardInput()