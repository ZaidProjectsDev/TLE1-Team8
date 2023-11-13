import cv2 as cv
import numpy as np


def findClickPositions(needle_img_path,reference_img, threshold = 0.5, debug_mode=None):

    needle_img = cv.imread(needle_img_path)
  
    result = cv.matchTemplate(reference_img, needle_img, cv.TM_CCOEFF_NORMED)
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    locations = np.where(result >= threshold)

    locations = list(zip(*locations[::-1]))
    print(locations)
    #rectangles wants [x,y,w,h] 
    rectangles =[]
    for loc in locations:
        rect =[int(loc[0]),int(loc[1]),needle_w,needle_h]
        rectangles.append(rect)
        rectangles.append(rect)



    rectangles, weights= cv.groupRectangles(rectangles,1,1.5)

    print(rectangles)
    points = []
    if len(rectangles):
        print('Found needle.')

        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = (255,00,00)
        marker_type =cv.MARKER_CROSS
        #loop over the rectangles and draw their rectangle
        for (x,y,w,h) in rectangles:
            '''
         
            '''
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            #save the points 
            points.append((center_x,center_y))
            if debug_mode =='rectangles':
                #determine box positions 
                top_left = (x,y)
                bottom_right = (x+w,y+h)
                #draw box
                cv.rectangle(reference_img,top_left,bottom_right,line_color,line_type)
            elif debug_mode == 'points':
                cv.drawMarker(reference_img,(center_x,center_y),marker_color, marker_type)
        if debug_mode:
            cv.imshow('Matches', reference_img)

    return points

