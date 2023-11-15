import numpy as np

detections_str = ""
def sentencebuilder(detections):
   if(detections == ''):
      return "Couldn't come up with a narration"
   #detections_str = np.array_str(detections)
   return f'''The current scene contains {detections}'''