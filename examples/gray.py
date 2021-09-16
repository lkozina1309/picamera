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
            
		image = frame.array
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
           
		cv2.imshow("Frame", gray)
		key = cv2.waitKey(1) & 0xFF

		rawCapture.truncate(0)
		
		if key == ord("q"):
			break
            

time.sleep(1)
stream()
cv2.destroyAllWindows()
