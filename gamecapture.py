from time import time
import cv2 as cv
import numpy as np
import os 
from windowcapture import WindowCapture
import torch
from matplotlib import pyplot as plt
import sentencebuilder

model = torch.hub.load('yolov5', 'yolov5s', source='local')
game_window_to_watch = 'The Evil Within 2' #Replace this with the game window you want to watch
#from vision import findClickPositions
#change the working dir the script is in 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.jpg'



#function copied from mak13 @ StackOverflow (https://stackoverflow.com/questions/71905867/how-to-turn-detections-object-into-string)
def results_parser(results):
  s = ""
  if results.pred[0].shape[0]:
    for c in results.pred[0][:, -1].unique():
      n = (results.pred[0][:, -1] == c).sum()  # detections per class
      s += f"{n} {results.names[int(c)]}{'s' * (n > 1)}, "  # add to string
  return s

def scan_game_window(game_window):
    wincap = WindowCapture(game_window)
    fps = time()
    #screenshot = wincap.get_screenshot()
    #Use this function if the game window is black (Slower at the moment. New hwnd search every frame. Need to optimize)
    screenshot = wincap.capture_win_alt(game_window)

    img = screenshot
    detections = []
 
    results = model(img)
    detections.append(results)
    #cv.imshow(game_window + ' scan', np.squeeze(results.render()))
    #cv.imshow(game_window + ' scan', np.squeeze(results.render()))

    results.print()
    print('FPS {}'.format( 1/(time()-fps)))
    fps = time()
    sentencebuilder.sentencebuilder(results_parser(results))
    return results_parser(results)