import numpy as np

detections_str = ""


def summary_string(results_array, confidence_threshold=70):
    summary_def = ""
    summary_low = ""

    for results_list in results_array:
        for result in results_list:
            try:
                class_name = result['class_name']
                count = result['count']
                average_confidence = sum(result['confidences']) / len(result['confidences'])

                if average_confidence >= confidence_threshold:
                    summary_def += f"{count} {class_name}s, "
                else:
                    summary_low += f"{count} {class_name}s, "
            except Exception as e:
                print(e)

    summary = ""
    if summary_def:
        summary += f"There are {summary_def}"

    if summary_low:
        if summary_def:
            summary += " and "
        summary += f"possibly {summary_low}"

    return summary.rstrip(', ')



def sentencebuilder(detections):
    if (detections == '' or detections == 'none'):
        return "Couldn't come up with a narration"

    # detections_str = np.array_str(detections)
    return summary_string(detections, 0.75)

    return f'''The current scene contains {detections}'''
