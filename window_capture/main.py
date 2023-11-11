from time import time
import cv2 as cv
import numpy as np
import os 
from windowcapture import WindowCapture
import torch
from matplotlib import pyplot as plt
model = torch.hub.load('yolov5', 'yolov5s', source='local')
game_window_to_watch = 'The Evil Within 2' #Replace this with the game window you want to watch
#from vision import findClickPositions
#change the working dir the script is in 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.jpg'
wincap = WindowCapture(game_window_to_watch)

#function copied from mak13 @ StackOverflow (https://stackoverflow.com/questions/71905867/how-to-turn-detections-object-into-string)
def results_parser(results):
  s = ""
  if results.pred[0].shape[0]:
    for c in results.pred[0][:, -1].unique():
      n = (results.pred[0][:, -1] == c).sum()  # detections per class
      s += f"{n} {results.names[int(c)]}{'s' * (n > 1)}, "  # add to string
  return s

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    #Use this function if the game window is black (Slower at the moment. New hwnd search every frame. Need to optimize)
    #screenshot = wincap.capture_win_alt(game_window_to_watch)

    img = screenshot
    detections = []
 
   # %matplotlib inline 

    corrected_colors= cv.cvtColor(img, cv.COLOR_RGB2BGR)
    results = model(img)
    detections.append(results)
    cv.imshow('YOLO', np.squeeze(results.render()))
    #img = cv.imread(needle_img_path_real)
    #print(img)
    #screenshot =  cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    #cv.imshow('Computer Vision', screenshot)
    #findClickPositions(needle_img_path_real, screenshot, 0.5, 'rectangles')
    #print(results_parser(results))
    results.print()
    print('FPS {}'.format( 1/(time()-loop_time)))
    loop_time = time()
    #press q with the output window focussed to exit
    #wait 1ms every loop to process key presses
    if(cv.waitKey(1)==ord('q')):
        cv.destroyAllWindows()


        break


print('Done.')