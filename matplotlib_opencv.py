import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('media/lena.jpg', -1)
matimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('image', img)

plt.imshow(matimg)
plt.show()

cv.waitKey(0)

cv.destroyAllWindows()