import cv2

img = cv2.imread('media/lena.jpg')
lowres1 = cv2.pyrDown(img)
lowres2 = cv2.pyrDown(lowres1)
highres1 = cv2.pyrUp(lowres2)
lap = cv2.subtract(highres1, lowres1)

cv2.imshow('Original', img)
cv2.imshow('PyrDown1', lowres1)
cv2.imshow('PyrDown2', lowres2)
cv2.imshow('PyrUp', highres1)
cv2.imshow('Laplace', lap)
cv2.waitKey(0)
cv2.destroyAllWindows()