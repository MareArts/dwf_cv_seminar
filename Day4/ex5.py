





import cv2

img1 = cv2.imread('secret.jpg')
img2 = cv2.imread('secret2.jpg')
rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dst = cv2.addWeighted(img1,0.7,rimg2,0.3,0)

cv2.imshow('dst3',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

