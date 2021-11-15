from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import random

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

def stream():
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		frame1 = frame.array
		frame2 = frame.array
		diff = cv2.absdiff(frame1, frame2)
		gray = cv2.cvtColor (diff, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray, (5,5), 0)
		_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
		dilated = cv2.dilate(thresh, None, iterations=3)
		contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		
		for contour in contours:
			(x,y,w,h) = cv2.boundingRect(contour)
			if cv2.contourArea(contour) < 900:
				continue
			cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
			
		cv2.imshow("feed", frame1)
		key = cv2.waitKey(1) & 0xFF
		
		rawCapture.truncate(0)
		
		if key == ord("q"):
			break
			
time.sleep(1)
stream()
cv2.destroyAllWindows()
			
			
