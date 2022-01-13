import cv2
import numpy as np

img = cv2.imread('media/lena.jpg', 1)
#for blank screen
#img = np.zeros([510, 510, 3], np.uint8)

#line on img params(image, start pt, end pt, ***color is in bgr format not rgb***(b, g, r), thickness)
img = cv2.line(img, (0,0), (255,255), (0, 255, 0), 2)
img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 2)

#points for left top and right bottom. if  thicknes is set to -1 the rectangle is filled with given color
img = cv2.rectangle(img, (255, 255), (510,510), (0,0,255), 2)

img = cv2.circle(img, (255,255), 100, (0,255,255), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (0,300), font, 3, (255,255,255),2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
