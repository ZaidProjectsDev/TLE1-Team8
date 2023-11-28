import os
import torch
import os
import torch
import narrator
current = None
# The point of system.py is to facilitate shared variables for consistent usage
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class SharedModels():
    genericModel = None
    genericModelConf = 1
    environmentModel = None
    environmentModelConf = 1
    gameElementModel = None
    gameElementModelConf = 1
    activeUIWindow = None

    def initalizeImageDetectionModel(self,modelVersion='yolov5x', confidenceVariable=genericModelConf,
                                     desiredMinimumConfidence=0.7):
        narrator.speak('Progress : 25%',True)
        model = torch.hub.load('yolov5', modelVersion, source='local')
        narrator.speak('Progress : 50%',True)
        return model

    def initalizeVision(self):
        narrator.speak('Starting Image Detection Software')
        self.genericModel = self.initalizeImageDetectionModel('yolov5x', self.genericModelConf, 0.7)
        narrator.speak('Progress :100%',True)
        narrator.speak('Image Detection Software Ready. Please press Q to Scan the Game Window.',True)
        print(self)





def setCurrentSharedModel(current_shared_model):
    current = current_shared_model

def getCurrentSharedModel():
    return current