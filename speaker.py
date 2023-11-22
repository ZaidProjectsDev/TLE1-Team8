

import pyttsx3


class SpeakerObject:
    engine = None
    initalized = False

    def __init__(self):
        self.initalized = True
    def saySelected(self, msg = "selected", state = True):
        addedMsg = ""
        if self.engine is None:
            self.engine = pyttsx3.init()
        if state is True:
            addedMsg = "Current selection is : "
        else:
            addedMsg = ""
        self.engine.stop()
        self.engine.say(addedMsg+msg)
        self.engine.runAndWait()

    def say(self, error="Undefined Error"):
        if self.engine is None:
            self.engine = pyttsx3.init()
        self.engine.stop()
        self.engine.say(error)
        self.engine.runAndWait()
