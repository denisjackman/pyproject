'''
    face redognition routine
'''
# Install libraries
# pip install opencv-python
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/04/28 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import os
import cv2

cascpath = os.path.dirname(cv2.__file__) + \
           "/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascpath)
video_capture = cv2.VideoCapture(0)
print(cascpath)
while True:
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, W, H) in faces:
        cv2.rectangle(frames, (x, y), (x+W, y+H), (0, 255, 0), 2)
    cv2.imshow('Video', frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
