import cv2
import numpy as np

x = np.uint8([100])
y = np.uint8([200])

#1byte = 0~255 
#z1 = cv2.add(x,y) #100 + 200 = 255
z2 = cv2.subtract(x,y) #100 - 200 = -100 -> 0
zz2 = cv2.absdiff(x,y) #100 - 200 = -100 -> +100
#z3 = cv2.multiply(x,y) # 100 * 200 = 255
#z4 = cv2.divide(x,y) #100 / 200 = 0



#print(z1, z2, z3, z4)
print(z2, zz2)


