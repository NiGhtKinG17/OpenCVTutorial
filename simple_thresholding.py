import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('media/gradient.png', 0)

_,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_,th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)
_,th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

titles = ['image', 'bin', 'bin inv', 'trunc', 'to zero']
images = [img, th1, th2, th3, th4]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# cv.imshow('image', img)
# cv.imshow('bin', th1)
# cv.imshow('bin inv', th2)
# cv.imshow('trunc', th3)
# cv.imshow('to zero', th4)

plt.show()

#cv.waitKey(0)

#cv.destroyAllWindows()