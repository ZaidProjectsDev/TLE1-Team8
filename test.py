import keyboard
import pygame

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
    print("You pressed 'q'.")
    play_sound('TLE1-Team8\ding-36029.wav')
    keyboardOn()

def keyboardOn():
    keyboard.wait("q")
    scanner()

keyboardOn()