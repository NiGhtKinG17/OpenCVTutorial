import cv2

#read image. 0 for grayscale, 1 for colored, -1 for load an image including alpha channel
img = cv2.imread('media/lena.jpg', -1)

#create window for displaying image
cv2.imshow('image', img)
#image display time in ms. 0 for infinite time until we close the window
cv2.waitKey(0)
#destroy all windows created
cv2.destroyAllWindows()

#create copy of image
cv2.imwrite('media/lena_duplicate.png', img)