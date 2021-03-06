import cv2
import numpy as np

cap = cv2.VideoCapture('media/slow_traffic_small.mp4')

#first frame of video
ret, frame = cap.read()

#setup initial location of window
x,y,w,h = 300,200,100,50
tracking_window = (x,y,w,h)

#set up the roi(region of interest) for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask,[180], [0,180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

#setup the termination criteria, either 10 iterations or move atleast 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 1)
while cap.isOpened():
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
    
    #appply meanshift to get new location
    ret, tracking_window = cv2.meanShift(dst, tracking_window, term_crit)

    #Draw it on image
    x,y,w,h = tracking_window
    final_image = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    cv2.imshow('dst', dst)
    cv2.imshow('final image', final_image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()