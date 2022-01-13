import cv2

cap = cv2.VideoCapture('media/vtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()

while cap.isOpened():
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('FG Mask frame', fgmask)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()