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
    genericModelConf = 0.5
    doorModel= None
    doorModelConf = 0.05\
    environmentModel = None
    environmentModelConf = 1
    gameElementModel = None
    gameElementModelConf = 1
    activeUIWindow = None
    initialized = False
    def initalizeImageDetectionModel(self,modelVersion='yolov5x',
                                     desiredMinimumConfidence=0.7):
        narrator.speak('Progress : 25%',True)
        model = torch.hub.load('yolov5', modelVersion, source='local')
        model.conf = desiredMinimumConfidence
        #model = torch.hub.load('.', 'custom', path='/door_detect_test.pt', source='local')
        #model = torch.hub.load('ultralytics/yolov5', 'custom', 'door_detect_test.pt')
       # model = torch.hub.load('yolov5', 'custom', path='door_detect_test.pt', source='local')
       # model.conf = 0.01
        print(model(torch.randn(1, 3, 640, 640)))
        narrator.speak('Progress : 50%',True)
        self.initialized = True
        return model
    def initalizeCustomImageDetectionModel(self,modelVersion='yolov5x',desiredMinimumConfidence=0.7):
        model = torch.hub.load('yolov5', 'custom', path=modelVersion, source='local')
        model.conf = desiredMinimumConfidence
        print(model(torch.randn(1, 3, 640, 640)))
        narrator.speak('Progress : 50%', True)
        self.initialized = True
        return model

    def initalizeVision(self):
        if self.initialized is False:
            narrator.speak('Starting Image Detection Software')
            self.genericModel = self.initalizeImageDetectionModel('yolov5x', self.genericModelConf)
            self.doorModel = self.initalizeCustomImageDetectionModel('stairs.pt',self.doorModelConf)
            narrator.speak('Progress :100%',True)
            narrator.speak('Image Detection Software Ready. Please press Q to Scan the Game Window.',True)
        print(self)





def setCurrentSharedModel(current_shared_model):
    current = current_shared_model

def getCurrentSharedModel():
    return current