import cv2
import numpy as np
import random

# Load two images
img1 = cv2.imread('empireofthesun.jpg')
#for speed up.
img1 = cv2.resize(img1, (200,200))


h,w,d = img1.shape

hit_count = 0
Max_hit = 10000 #ecsape count
x=0
y=0
r_x = 1
r_y = 1

while 1:
    
    if x<0:
        r_x = random.randint(1,3)
        hit_count = hit_count + 1
    
    if y<0:
        r_y = random.randint(1,3)
        hit_count = hit_count + 1
    
    if x>w:
        r_x = random.randint(-3,-1)
        hit_count = hit_count + 1

    if y>h:
        r_y = random.randint(-3,-1) 
        hit_count = hit_count + 1


    x = x + r_x
    y = y + r_y


    if Max_hit < hit_count: #break display
        break

    img2 = np.zeros(img1.shape, np.uint8)
    cv2.circle(img2, (x, y), 30, (255,255,255), -1)  
    image_and = cv2.bitwise_and(img1,img2)

    cv2.imshow('result',image_and)
    #cv2.imshow('img2',img2)
    if cv2.waitKey(10) > 0:
        break




cv2.destroyAllWindows()


