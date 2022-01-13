import cv2

#for accessing camera. 0 or -1 for default camera, 1 and later for any external camera
cap = cv2.VideoCapture(0)
#fourcc is 4 bite code or FourCharacterCode used to uniquely identify data formats www.fourcc.org/codecs.php
fourcc = cv2.VideoWriter_fourcc(*'XVID') #or cv2.VideoWriter_fourcc('X','V','I','D')
#video parameters(file name with which video is saved, fourcc code, frames,(resolution))
out = cv2.VideoWriter('myvideo.avi', fourcc, 20.0, (640,480))

#code for capturing through camera until pressed 'q'
while (True):
    ret, frame = cap.read()
    if ret == True:
        #write the video and saving the captured frames
        out.write(frame)

        #converting our video from rgb to grayscale. by default capture is in rgb
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('cap', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
           break

#important step to release the resources used by above code
cap.release()
out.release()
cv2.destroyAllWindows()
