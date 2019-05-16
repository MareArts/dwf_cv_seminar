###########################################
import cv2
import numpy as np


cv2.namedWindow('window',0)

cap = cv2.VideoCapture(0)
_, frame = cap.read()
row, col, _ = frame.shape
print(row, col)



while True:
    # Get the next frame
    ret , frame = cap.read()

    #get frame
    if ret:
        #processing

        cv2.imshow('window', frame)
        if cv2.waitKey(10) > 0:
            break

    else:
        break






img = cv2.imread('./Day3/messi.jpg')

row, col, _ = img.shape
print(row, col)

row_step = row/4
col_step = col/4


for i in range(4):
    for j in range(4):
        
        if i%2 != j%2:
            continue

        y1 = int(row_step*i)
        y2 = int(row_step*i + row_step)

        x1 = int(col_step*j)
        x2 = int(col_step*j + col_step)

        img[y1:y2, x1:x2] = [255, 255, 255] - img[y1:y2, x1:x2]

        
img[:, :] = [255, 255, 255] - img[:,:]


cv2.namedWindow('window',0)
cv2.imshow('window', img)
cv2.waitKey(0)
###########################################



cv2.namedWindow('window',0)

cap = cv2.VideoCapture(0)
_, frame = cap.read()
row, col, _ = frame.shape
print(row, col)

row_step = row/4
col_step = col/4

while True:
    # Get the next frame
    ret , frame = cap.read()

    #get frame
    if ret:
        for i in range(4):
            for j in range(4):
                if i%2 != j%2:
                    continue

                y1 = int(row_step*i)
                y2 = int(row_step*i + row_step)

                x1 = int(col_step*j)
                x2 = int(col_step*j + col_step)

                frame[y1:y2, x1:x2] = [255, 255, 255] - frame[y1:y2, x1:x2]

        cv2.imshow('window', frame)
        if cv2.waitKey(10) >0:
            break
        





