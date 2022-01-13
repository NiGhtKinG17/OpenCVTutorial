import cv2
import numpy as np

img = cv2.imread('media/pic1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)

corners =  np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('img',  img)
cv2.waitKey(0)
cv2.destroyAllWindows()