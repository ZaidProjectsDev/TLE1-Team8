import numpy as np

detections_str = ""


def summary_string(results_array, confidence_threshold=70):
   summary = ""
   for result in results_array:
      class_name = result['class_name']
      count = result['count']
      average_confidence = sum(result['confidences']) / len(result['confidences'])

      if average_confidence >= confidence_threshold:
         summary += f"There are {count} {class_name}s, "
      else:
         summary += f"There are possibly {count} {class_name}s, "

   return summary.rstrip(', ')


def sentencebuilder(detections):
   if(detections == '' or detections =='none'):
      return "Couldn't come up with a narration"

   #detections_str = np.array_str(detections)
   return summary_string(detections, 0.75)

   return f'''The current scene contains {detections}'''