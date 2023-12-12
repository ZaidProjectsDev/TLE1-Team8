import os
import torch
import os
import torch
import narrator
import time

current = None
# The point of system.py is to facilitate shared variables for consistent usage
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class SharedModels():
    genericModel = None
    hudModel = None
    doorModel = None
    fireModel = None
    environmentModel = None
    gameElementModel = None
    activeUIWindow = None
    initialized = False
    screenReaderEnabled = False
    #THIS INITIALIZES THE DEFAULT YOLOV5 DETECTION MODEL

    def initalizeImageDetectionModel(self, modelVersion='yolov5x', desiredMinimumConfidence=0.7):
        narrator.speak('Progress : 25%', True, False, True)
        model = torch.hub.load('yolov5', modelVersion, source='local')
        model.conf = desiredMinimumConfidence
        narrator.speak('Progress : 50%', True, False, True)
        self.initialized = True
        return model
    #THIS INITIALIZES THE CUSTOM YOLOV% DETECTION MODEL YOU MADE, EX: Doors, HUD, Fires, etc
    def initalizeCustomImageDetectionModel(self, modelVersion='yolov5x', desiredMinimumConfidence=0.7):
        model = torch.hub.load('yolov5', 'custom', path=modelVersion, source='local', force_reload=True)
        model.conf = desiredMinimumConfidence
        print(model(torch.randn(1, 3, 640, 640)))
        return model

    #THIS RUNS THE DETECTION INITIALIZATION FOR ALL MODELS.
    def initalizeVision(self):
        if self.initialized is False:
            try:

                self.screenReaderEnabled = True

                narrator.speak('Starting Image Detection Software', True, False, True)
                self.genericModel = self.initalizeImageDetectionModel('yolov5x', 0.6)
                self.doorModel = self.initalizeCustomImageDetectionModel('doors.pt', 0.2)
                self.hudModel = self.initalizeCustomImageDetectionModel('hud.pt',0.2)

                narrator.speak('Progress :100%', True, False, True)
                narrator.speak('Image Detection Software Ready. Please press Q to Scan the Game Window.', True, False,
                               True)
            except Exception as e:
                self.screenReaderEnabled = False
                self.genericModel = None
                # other models here
                narrator.speak('There was an error starting the software. Contact the developer')
                time.sleep(4)
                print(str(e))
                narrator.speak(str(e), True, False)
                self.initialized = False
        print(self)

    def uninitalizeVision(self):
        if self.initialized is True:
            narrator.speak('Disabling Screen Reader', True, False)
            self.genericModel = None
            self.initialized = False
            self.screenReaderEnabled = False
            # put other models here that need to be disabled.
            time.sleep(4)
            narrator.speak('Screen Reader disabled.')


def setCurrentSharedModel(current_shared_model):
    current = current_shared_model


def getCurrentSharedModel():
    return current
