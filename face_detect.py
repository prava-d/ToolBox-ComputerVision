""" Experiment with face detection and image filtering using OpenCV """
""" This worked when I ran it on my home computer, but not here for some reason.
I got permission from a Ninja to push."""

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((30, 30), 'uint8')
cap = cv2.VideoCapture('Image_Processing_Test_Video.webm')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
        for (x, y, w, h) in faces:
            frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))
            # face
            cv2.ellipse(frame, (x+int(w/2), y+int(h/2)), (int(0.9*w/2), int(h/2)), 0, 0, 360, (0, 0, 0), 2)
            # mouth
            cv2.ellipse(frame, (x+int(w/2), y+int(h/2)), (int(w/3), int(h/3)), 0, 45, 135, (0, 0, 0), 2)
            # eyes
            cv2.ellipse(frame, (x+int(2*w/7), y+int(2*h/5)), (int(w/10), int(h/15)), 0, 0, 360, (0, 0, 0), 2)
            cv2.ellipse(frame, (x+int(5*w/7), y+int(2*h/5)), (int(w/10), int(h/15)), 0, 0, 360, (0, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
