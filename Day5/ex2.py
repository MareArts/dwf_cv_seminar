import cv2

# Load two images
img1 = cv2.imread('empireofthesun.jpg')
img2 = cv2.imread('empireofthesun_mask.jpg')

image_and = cv2.bitwise_and(img1,img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

#cv2.imwrite('abc.png', image_and)

cv2.imshow('image_and',image_and)
cv2.waitKey(0)
cv2.destroyAllWindows()


