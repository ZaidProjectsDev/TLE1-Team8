import keyboard
import pygame
import pyttsx3
import gamecapture

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
    result = gamecapture.try_to_capture_game_window(20,game_window)
    engine = pyttsx3.init()
    engine.say(result)
    engine.runAndWait()
    print(result)

def keyboardInput(game_window):
    keyboard.wait("q")
    scanner(game_window)

