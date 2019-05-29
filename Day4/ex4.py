import cv2

img1 = cv2.imread('secret.jpg')
img2 = cv2.imread('secret2.jpg')
rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

abs_img = cv2.absdiff(img1, rimg2)  #abs(A-B)  absolute(100-200) = -100 -> +100
cv2.imshow('abs_img',abs_img)

cv2.waitKey(0)
cv2.destroyAllWindows()