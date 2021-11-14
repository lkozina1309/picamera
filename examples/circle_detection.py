from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
import random
import numpy as np
import argparse

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

def stream():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray, 5)
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 500, param1=10, param2=80, minRadius=0, maxRadius=0)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            
            for (x,y,r) in circles:
                cv.circle(image, (x,y), r, (0,255,0), 3)
                cv.circle(image, (x,y), 1, (0,255,255), 3)
        cv.imshow("camera", image)
        key = cv.waitKey(1) & 0xFF
        
        rawCapture.truncate(0)

        if key == ord("q"):
            break
			
time.sleep(1)
stream()
cv2.destroyAllWindows()
