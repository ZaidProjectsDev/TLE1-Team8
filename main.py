import cv2 as cv
import numpy as np
import os 
from gamecapture import scan_game_window
os.chdir(os.path.dirname(os.path.abspath(__file__)))
canvas_img_path_real = 'img-test/ref/tew2/tew2_ref_2.png'
needle_img_path_real = 'img-test/ref/tew2/goal/gui_2.png'

while (True):
    
    print(scan_game_window('The Evil Within 2'))
    if(cv.waitKey(1)==ord('q')):
        cv.destroyAllWindows()
        break

#points = findClickPositions(needle_img_path_real,canvas_img_path_real,0.8,debug_mode='rectangles');
#print(points)

