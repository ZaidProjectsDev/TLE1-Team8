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
    s = ""
    if results.pred[0].shape[0]:
        for c in results.pred[0][:, -1].unique():
            class_idx = int(c)
            class_name = results.names[class_idx]
            class_confidences = results.pred[0][results.pred[0][:, -1] == c, -2]  # confidence values for the class

            n = class_confidences.shape[0]  # number of detections for the class
            s += f"{n} {class_name}{'s' * (n > 1)} with confidences: {', '.join(map(lambda x: f'{x:.2f}', class_confidences))}, "  # add to string

    return s


def try_to_capture_game_window(retries=5, game_window=None, models=None):
    combined_results = []

    for model in models:
        current_retry_count = 0
        result = None

        while result is None and current_retry_count < retries:
            try_result = scan_game_window(game_window, model)

            if try_result != "Couldn't come up with a narration":
                result = try_result
            else:
                current_retry_count += 1

        combined_results.append(result)

    return combined_results


def scan_game_window(game_window, model):
    wincap = WindowCapture(game_window)
    fps = time()
    # screenshot = wincap.get_screenshot()
    # Use this function if the game window is black (Slower at the moment. New hwnd search every frame. Need to optimize)
    screenshot = wincap.capture_win_alt(game_window)

    img = screenshot
    detections = []

    results = model(img)
    detections.append(results)
    cv.namedWindow(game_window + ' scan', cv.WINDOW_KEEPRATIO)
    cv.imshow(game_window + ' scan', np.squeeze(results.render()))
    cv.resizeWindow(game_window + ' scan', 960, 540)

    # cv.imshow(game_window + ' scan', np.squeeze(results.render()))

    results.print()
    print('FPS {}'.format(1 / (time() - fps)))
    fps = time()

    return sentencebuilder.sentencebuilder(results_parser(results))
