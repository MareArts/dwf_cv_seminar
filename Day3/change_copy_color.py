###########################################
import cv2
import numpy as np
img = cv2.imread('./Day3/messi.jpg')

##################################################
#ROI(Region Of Interest)
#row, col
#img[73:107, 184:213] = [0, 0, 255]
#cv2.rectangle(img, (184,73), (213,107), (255,255,255),10)
##################################################


##################################################
face = img[73:107, 184:213]
# img[73+100:107+100, 184+100:213+100] = face
##################################################


##################################################
for i in range(1,10):
    skip=i*10
    img[73+skip:107+skip, 184+skip:213+skip] = face
##################################################


cv2.namedWindow('window',0)
cv2.imshow('window', img)
cv2.waitKey(0)
###########################################


