import cv2 as cv
import numpy as np
import os 
from gamecapture import scan_game_window
from inputchecker import keyboardInput
os.chdir(os.path.dirname(os.path.abspath(__file__)))
canvas_img_path_real = 'img-test/ref/tew2/tew2_ref_2.png'
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.png'
game_window_name = 'The Evil Within 2' #Replace this with what is relevant to your use case.
while (True):
    keyboardInput
    if(cv.waitKey(1)==ord('q')):
        cv.destroyAllWindows()
        break

#points = findClickPositions(needle_img_path_real,canvas_img_path_real,0.8,debug_mode='rectangles');
#print(points)

