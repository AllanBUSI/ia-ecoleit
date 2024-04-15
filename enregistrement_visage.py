import cv2


# import os

# contents = os.listdir('image')


# print(contents)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
capture = cv2.VideoCapture(0)

c=50

input = input("Enter le prenom de la personne : ")

id=0

while True:
    ret, frame = capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(c, c))
    for x, y, w, h in face:
        cv2.imwrite("image/p-{:d}.png".format(id), frame[y:y+h, x:x+w])
        id+=1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('video', frame)
    key=cv2.waitKey(1)&0xFF

capture.release()
cv2.destroyAllWindows()