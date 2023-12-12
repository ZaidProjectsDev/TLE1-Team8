from time import time
import cv2 as cv
import numpy as np
import os

import shared_model
from windowcapture import WindowCapture
import torch
from matplotlib import pyplot as plt
import sentencebuilder

shared_models = shared_model.SharedModels()
import speaker


# function copied from mak13 @ StackOverflow (https://stackoverflow.com/questions/71905867/how-to-turn-detections-object-into-string)
def results_parser(results):
    result_array = []
    if results.pred[0].shape[0]:
        for c in results.pred[0][:, -1].unique():
            class_idx = int(c)
            class_name = results.names[class_idx]
            class_confidences = results.pred[0][results.pred[0][:, -1] == c, -2]  # confidence values for the class

            n = class_confidences.shape[0]  # number of detections for the class
            result_array.append({
                'class_name': class_name,
                'count': n,
                'confidences': class_confidences.tolist()
            })

    if not result_array:
        return "none"
    else:
        return result_array


def try_to_capture_game_window(retries=5, game_window=None, models=None):
    combined_results = []
    cur_scan = 0
    for model in models:
        current_retry_count = 0
        result = None

        while result is None and current_retry_count < retries:
            try_result = scan_game_window(game_window, model, str(cur_scan))

            if try_result != "Couldn't come up with a narration":
                result = try_result
                cur_scan += 1
            else:
                current_retry_count += 1

        combined_results.append(result)

    return combined_results


def scan_game_window(game_window, model, model_name):
    wincap = WindowCapture(game_window)
    fps = time()
    # screenshot = wincap.get_screenshot()
    # Use this function if the game window is black (Slower at the moment. New hwnd search every frame. Need to optimize)
    screenshot = wincap.capture_win_alt(game_window)

    img = screenshot
    detections = []

    results = model(img)
    detections.append(results)
    window_name = game_window + '_' + model_name + ' scan'
    cv.namedWindow(window_name, cv.WINDOW_KEEPRATIO)
    cv.imshow(window_name, np.squeeze(results.render()))
    cv.resizeWindow(window_name, 960, 540)

    # cv.imshow(game_window + ' scan', np.squeeze(results.render()))

    results.print()
    print('FPS {}'.format(1 / (time() - fps)))
    fps = time()

    return sentencebuilder.sentencebuilder(results_parser(results))
