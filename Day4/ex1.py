import cv2
import numpy as np

x = np.uint8([100])
y = np.uint8([200])

z1 = cv2.add(x,y)
z2 = cv2.subtract(x,y)
z3 = cv2.multiply(x,y)
z4 = cv2.divide(x,y)

print(z1, z2, z3, z4)