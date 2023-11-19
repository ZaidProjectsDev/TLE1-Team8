import keyboard
import pygame
import speaker
import gamecapture
import localization
root = None
models = None
state_reporter = speaker.SpeakerObject()
lang = localization.Localization()
def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))  # Delay to ensure the sound plays completely
        state_reporter.say(lang.get_translation('tts_scanning'))
    except pygame.error as e:
        print("Error playing sound:", e)
    finally:
        pygame.mixer.quit()


def scanner(game_window, shared_models):
    print("you pressed 'q' .")
    play_sound('ding-36029.wav')
    result = gamecapture.try_to_capture_game_window(20, game_window, shared_models.genericModel)
    state_reporter.say(result)
    print(result)


def keyboardInput(game_window, shared_models):
    if keyboard.is_pressed('q'):
        if game_window != '':
            scanner(game_window, shared_models)
        else:
            state_reporter.say(lang.get_translation('tts_no_window_found'))

