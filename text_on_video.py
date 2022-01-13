import cv2
import datetime

cap = cv2.VideoCapture(0)

cap.set(3, 3000) #3 is numerical value for cv2.CAP_PROP_FRAME_WIDTH
cap.set(4, 3000) #4 is numerical value for cv2.CAP_PROP_FRAME_HEIGHT

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, dt, (10,50), font, 1, (0,0,0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()