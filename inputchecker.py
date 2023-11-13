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


def scanner(game_window):
    print("you pressed 'q' .")
    play_sound('ding-36029.wav')
    print(scan_game_window(game_window))

def keyboardInput(game_window):
    keyboard.wait("q")
    scanner(game_window)

