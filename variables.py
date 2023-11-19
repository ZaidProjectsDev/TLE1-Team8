import os
import torch
import os

import torch

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
        model = torch.hub.load('yolov5', modelVersion, source='local')
        return model

    def initalizeVision(self):
        self.genericModel = self.initalizeImageDetectionModel('yolov5x', self.genericModelConf, 0.7)
        print(self)




