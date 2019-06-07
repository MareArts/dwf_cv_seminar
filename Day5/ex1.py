import cv2
import numpy as np


image1 = np.zeros((400,400,3), np.uint8)
image2 = np.zeros((400,400,3), np.uint8)



cv2.circle(image1, (100, 200), 150, (255,255,255), -1)  
cv2.circle(image2, (300, 200), 150, (255,255,255), -1)  


image_and = cv2.bitwise_and(image1,image2)
image_or = cv2.bitwise_or(image1,image2)
image_xor = cv2.bitwise_xor(image1,image2)
image_not = cv2.bitwise_not(image1)


cv2.namedWindow('img1',0)
cv2.namedWindow('img2',0)

cv2.imshow('img1',image1)
cv2.imshow('img2',image2)

cv2.namedWindow('image_and',0)
cv2.namedWindow('image_or',0)
cv2.namedWindow('image_xor',0)
cv2.namedWindow('image_not',0)

cv2.imshow('image_and',image_and)
cv2.imshow('image_or',image_or)
cv2.imshow('image_xor',image_xor)
cv2.imshow('image_not',image_not)

cv2.waitKey(0)
cv2.destroyAllWindows()

    

