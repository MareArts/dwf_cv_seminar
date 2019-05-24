import cv2

img1 = cv2.imread('secret.jpg')
img2 = cv2.imread('secret2.jpg')
rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

print(img1.shape)
add_img = cv2.add(img1, (100,100,100,0))
mul_img = cv2.multiply(img1, (100,100,100,0))
sub_img = cv2.subtract(img1, (100,100,100,0))
div_img = cv2.divide(img1, (100,100,100,0))

cv2.imshow('add_img',add_img)
cv2.imshow('sub_img',sub_img)
cv2.imshow('mul_img',mul_img)
cv2.imshow('div_img',div_img)

cv2.waitKey(0)
cv2.destroyAllWindows()