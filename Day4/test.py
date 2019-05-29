import cv2

img1 = cv2.imread('secret.jpg')
img2 = cv2.imread('secret2.jpg')
rimg2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

alfa=0.99
beta=1-alfa




for i in range(0,100):
    dst = cv2.addWeighted(img1,alfa,rimg2,beta,0)
    cv2.imshow('dst', dst)
    print(i)
    cv2.waitKey(50)
    alfa = alfa - 0.01
    beta=1-alfa
    print(alfa)
    print(beta)
    
cv2.destroyAllWindows()

