import cv2
import numpy as np

img = cv2.imread('media/messi5.jpg')
imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('media/messi5-face.jpg', 0)

match = cv2.matchTemplate(imgrey, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(match >= 0.95)
print(loc)
w,h = template.shape[::-1]

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h), (0,255,0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()