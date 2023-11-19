import pyttsx3


class SpeakerObject:
    engine = None
    initalized = False
    def __init__(self):
        self.initalized = True

    def say(self, error="Undefined Error"):
        if self.engine is None:
            self.engine = pyttsx3.init()
        self.engine.say(error)
        self.engine.runAndWait()
