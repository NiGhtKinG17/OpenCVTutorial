import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = np.zeros((250, 500,3), np.uint8)
img2= cv2.rectangle(img2, (250,0), (500,250), (255,255,255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)

cv2.waitKey(0)
cv2.destroyAllWindows()