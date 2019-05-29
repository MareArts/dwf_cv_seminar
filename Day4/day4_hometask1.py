




import cv2

img1 = cv2.imread('secret.jpg')
img2 = cv2.imread('secret2.jpg')
rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
cv2.namedWindow('dst3',0)
cv2.waitKey(0)

for i in range(0,100,1):
    f = i/100.0
    a = f
    b = 1-f
    dst = cv2.addWeighted(img1,a,rimg2,b,0)
        
    cv2.imshow('dst3',dst)
    cv2.waitKey(20)

cv2.waitKey(0)
cv2.destroyAllWindows()
