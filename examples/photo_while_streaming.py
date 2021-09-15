from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import random

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

class Video:

    def __init__(self):
        self.i=0

    def stream(self):
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            
            image = frame.array
            
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF

            rawCapture.truncate(0)
            
            
            if key == ord("s"):
                self.i = self.i + 1
                self.slika()
            if key == ord("q"):
                break

    def slika(self):
        while True:
            camera.start_preview()
            time.sleep(2)
            camera.capture('image%s.jpg' % self.i)
            time.sleep(2)
            break



time.sleep(1)
v=Video()
v.stream()
cv2.destroyAllWindows()
