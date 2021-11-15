from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import random

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
face_cascade = cv2.CascadeClassifier('/home/pi/haar_cascades.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/haarcascade_eye_tree_eyeglasses.xml')

def stream():
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 4)
		
		for (x, y , w ,h) in faces:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex, ey ,ew, eh) in eyes:
				cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)
		cv2.imshow("Frame", image)
		key = cv2.waitKey(1) & 0xFF
		
		rawCapture.truncate(0)
		
		if key == ord("q"):
			break
			
time.sleep(1)
stream()
cv2.destroyAllWindows()
