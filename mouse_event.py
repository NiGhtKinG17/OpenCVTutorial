import numpy as np
import cv2

def click_event(event, X, Y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(X, ', ', Y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(X)+', '+str(Y)
        cv2.putText(img, strXY, (X,Y), font, 1, (0,255,255), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[Y, X, 0]
        g = img[Y, X, 1]
        r = img[Y, X, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strRGB = str(b)+', '+str(g)+', '+str(r)
        cv2.putText(img, strRGB, (X,Y), font, 0.5, (255,255,0), 1)
        cv2.imshow('image', img)


#img = np.full((512,512), 255, np.uint8)
img = cv2.imread('media/messi5.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()