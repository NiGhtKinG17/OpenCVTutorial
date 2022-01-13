import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('media/lena.jpg',0)

# b, g, r = cv2.split(img)

# cv2.imshow('image', img)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)

# plt.hist(b.ravel() , 256, [0,256])
# plt.hist(g.ravel() , 256, [0,256])
# plt.hist(r.ravel() , 256, [0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()