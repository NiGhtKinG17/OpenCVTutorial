import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('media/messi5.jpg', 0)
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelXY = cv2.bitwise_or(sobelX, sobelY)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel XY', 'Canny Edge']
images = [img, lap, sobelX, sobelY, sobelXY, canny]


for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()