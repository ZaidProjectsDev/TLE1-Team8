from time import time
import cv2 as cv
import numpy as np
import os
from windowcapture import WindowCapture
import torch
from matplotlib import pyplot as plt
import sentencebuilder
import variables


# function copied from mak13 @ StackOverflow (https://stackoverflow.com/questions/71905867/how-to-turn-detections-object-into-string)
def results_parser(results):
    s = ""
    if results.pred[0].shape[0]:
        for c in results.pred[0][:, -1].unique():
            n = (results.pred[0][:, -1] == c).sum()  # detections per class
            s += f"{n} {results.names[int(c)]}{'s' * (n > 1)}, "  # add to string
    return s


def try_to_capture_game_window(retries=5, game_window=None, model=None):
    current_retry_count = 0
    result = None
    while (result == None):
        try_result = scan_game_window(game_window, model)
        if (try_result != "Couldn't come up with a narration"):  # error message
            result = try_result
        else:
            if (current_retry_count < retries):
                current_retry_count += 1
            else:
                result = try_result

    return result


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
    cv.imshow(game_window + ' scan', np.squeeze(results.render()))
    # cv.imshow(game_window + ' scan', np.squeeze(results.render()))

    results.print()
    print('FPS {}'.format(1 / (time() - fps)))
    fps = time()

    return sentencebuilder.sentencebuilder(results_parser(results))
