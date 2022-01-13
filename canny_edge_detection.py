import cv2
import matplotlib.pyplot as plt

img = cv2.imread('media/messi5.jpg', 0)

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('X', 'image', 0, 300, nothing)
cv2.createTrackbar('Y', 'image', 0, 300, nothing)

while True:
   

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    x = cv2.getTrackbarPos('X', 'image')
    y = cv2.getTrackbarPos('Y', 'image')

    result = cv2.Canny(img, x, y)
    cv2.imshow('image', img)
    cv2.imshow('Canny', result)
cv2.destroyAllWindows()