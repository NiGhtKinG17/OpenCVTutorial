import cv2

face_cascade = cv2.CascadeClassifier('trainers/haarcascade_frontalface_default.xml')

# img = cv2.imread('media/faces.png')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('vid', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.imshow('image', img)
cap.release()
cv2.destroyAllWindows()