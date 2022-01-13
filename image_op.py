import cv2

img = cv2.imread('media/messi5.jpg')

ball = img[280:340, 330:390]

img[223:283, 50:110] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()