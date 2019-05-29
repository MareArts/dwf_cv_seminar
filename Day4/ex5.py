





import cv2

img1 = cv2.imread('secret.jpg')
img2 = cv2.imread('secret2.jpg')
rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

alpha = 0.8
beta = 1 - alpha
dst = cv2.addWeighted(img1, alpha,rimg2, beta,0)

for i in range(1,100):
    cv2.imshow('dst3',dst)
    print(i)
    cv2.waitKey(100) #mill sec 0.1 sec


cv2.imshow('dst3',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

