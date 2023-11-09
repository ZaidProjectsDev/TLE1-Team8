import cv2 as cv
import numpy as np

reference_img = cv.imread('tew2_ref_2.png', cv.IMREAD_REDUCED_COLOR_2)
needle_img = cv.imread('gui_2.png', cv.IMREAD_REDUCED_COLOR_2)

result = cv.matchTemplate(reference_img,needle_img,cv.TM_CCOEFF_NORMED)
threshold = 0.8
#get the best match position 
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)

print ('Best match top left position: %s'% str(max_loc))
print ('Best match confidence: %s' % max_val)

if max_val >= threshold:
    print('Found needle.')

        #get dimesions of needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0]+needle_w, top_left[1]+needle_h)
    cv.rectangle(reference_img,top_left,bottom_right,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
    cv.imshow('Result',reference_img)
    cv.imwrite('result.png',reference_img);
    cv.waitKey()
else:
    print ('Needle not found.')