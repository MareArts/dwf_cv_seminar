

###########################################
import cv2
import numpy as np
img = cv2.imread('./messi.jpg')
cv2.namedWindow('window',0)
cv2.imshow('window', img)
cv2.waitKey(0)
###########################################


###########################################
#image sahpe
print(img.shape)
#image size
print(img.size)

#image type
print(img.dtype)
###########################################


###########################################
#access 1 pixel
pixel = img[100,100]
print(pixel)

pixel = img[100][100]
print(pixel)
###########################################


###########################################
#show RGB cube
###########################################

###########################################
#and show this
pixel_B = img[100][100][0]
pixel_G = img[100][100][1]
pixel_R = img[100][100][2]
###########################################
print(pixel_B, pixel_G, pixel_R)
print(img[100][100])



