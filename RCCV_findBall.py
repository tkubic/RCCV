# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO
#GPIO.setwarnings(False) #turn warnings off in shell

### setup
##GPIO.setmode(GPIO.BCM)
##pinA1A = 19 
##pinA1B = 26
##pinB1A = 6
##pinB1B = 13
### set pins as outputs
##GPIO.setup(pinA1A, GPIO.OUT)
##GPIO.setup(pinA1B, GPIO.OUT)
##GPIO.setup(pinB1A, GPIO.OUT)
##GPIO.setup(pinB1B, GPIO.OUT)
### create pwm instances
##freq = 50 #frequency in Hertz
##pwmA1A =  GPIO.PWM(pinA1A, freq)
##pwmA1B =  GPIO.PWM(pinA1B, freq)
##pwmB1A =  GPIO.PWM(pinB1A, freq)
##pwmB1B =  GPIO.PWM(pinB1B, freq)
### start pwm instances
##pwmA1A.start(0)
##pwmA1B.start(0)
##pwmB1A.start(0)
##pwmB1B.start(0)

class RCCV:

    def __init__(self):
        # setup
        GPIO.setmode(GPIO.BCM)
        pinA1A = 19 
        pinA1B = 26
        pinB1A = 6
        pinB1B = 13
        # set pins as outputs
        GPIO.setup(pinA1A, GPIO.OUT)
        GPIO.setup(pinA1B, GPIO.OUT)
        GPIO.setup(pinB1A, GPIO.OUT)
        GPIO.setup(pinB1B, GPIO.OUT)
        # create pwm instances
        freq = 50 #frequency in Hertz
        self.pwmA1A =  GPIO.PWM(pinA1A, freq)
        self.pwmA1B =  GPIO.PWM(pinA1B, freq)
        self.pwmB1A =  GPIO.PWM(pinB1A, freq)
        self.pwmB1B =  GPIO.PWM(pinB1B, freq)
        # start pwm instances
        self.pwmA1A.start(0)
        self.pwmA1B.start(0)
        self.pwmB1A.start(0)
        self.pwmB1B.start(0)
        # initialize the camera and grab a reference to the raw camera capture
        #self.camera = PiCamera()
        #self.camera.resolution = (640,480)
        global camera
        camera = PiCamera()
        self.rawCapture = PiRGBArray(camera)
        # allow the camera to warmup
        time.sleep(0.1)
    
    def forward(self, dc=100):
        # Go forward
        self.pwmA1A.ChangeDutyCycle(dc)
        self.pwmA1B.ChangeDutyCycle(0)
        self.pwmB1A.ChangeDutyCycle(dc)
        self.pwmB1B.ChangeDutyCycle(0)

    def forwardTurn(self, dc1=100,dc2=0):
        # Go forward while turning
        self.pwmA1A.ChangeDutyCycle(dc1)
        self.pwmA1B.ChangeDutyCycle(0)
        self.pwmB1A.ChangeDutyCycle(dc2)
        self.pwmB1B.ChangeDutyCycle(0)


    def stop(self):
        # Stop
        self.pwmA1A.ChangeDutyCycle(0)
        self.pwmA1B.ChangeDutyCycle(0)
        self.pwmB1A.ChangeDutyCycle(0)
        self.pwmB1B.ChangeDutyCycle(0)

    def backward(self, dc=100):
        # Go Backwards
        self.pwmA1A.ChangeDutyCycle(0)
        self.pwmA1B.ChangeDutyCycle(dc)
        self.pwmB1A.ChangeDutyCycle(0)
        self.pwmB1B.ChangeDutyCycle(dc)

    def spinCW(self, dc=100):
        self.pwmA1A.ChangeDutyCycle(dc)
        self.pwmA1B.ChangeDutyCycle(0)
        self.pwmB1A.ChangeDutyCycle(0)
        self.pwmB1B.ChangeDutyCycle(dc)


    def spinCCW(self, dc=100):
        self.pwmA1A.ChangeDutyCycle(0)
        self.pwmA1B.ChangeDutyCycle(dc)
        self.pwmB1A.ChangeDutyCycle(dc)
        self.pwmB1B.ChangeDutyCycle(0)

    def findContours(self, image):
        # Find the contours
        imgContours, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        return contours

    def findMinCircle(self, image):
        contours = self.findContours(image)
        #print("contours length is:", len(contours))
        if len(contours) >= 1:
            (x, y), radius = cv2.minEnclosingCircle(contours[0])
            center = (int(int(x)*100/640), int(int(y)*100/480))
            radius = int(radius)
            # print(radius)
        else:
            center = (50, 50)
            radius = 0
            #print("no contours found")
        return center, radius

    def driveAuto(self):
        global camera
        self.rawCapture = PiRGBArray(camera)
        # grab an image from the camera
        camera.capture(self.rawCapture, format="bgr")
        self.image = self.rawCapture.array
        # Convert BGR to HSV
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        # Threshold the HSV image to get only blue colors
        lower_range = np.array([150, 100, 0])
        upper_range = np.array([183, 255, 255])
        # Threshold the HSV image to get only blue colors
        maskImg = cv2.inRange(hsv, lower_range, upper_range)
        kernel = np.ones((7,7), np.uint8)
        self.Img = cv2.morphologyEx(maskImg, cv2.MORPH_OPEN, kernel)
        #cv2.imshow("Image", self.Img)
        #cv2.waitKey(1) & 0xFF
        center, radius = self.findMinCircle(image = self.Img)
        #print(center)
        print(radius, center)
        if 60 < center[0] < 100 and 20 <= radius <= 100:
                self.forwardTurn(15,15+center[1]/10)
                print("turning left")
        elif 0 < center[0] <40 and 20 <= radius <= 200:
                self.forwardTurn(15+center[1]/10,15)
                print("turning right")
        elif 40 <= center[0] <=60 and 20 <= radius <= 200:
                self.forward(20)
                print("forward")
        else:
                print("stopping")
                self.stop()


mode = 1
#RCCV().driveAuto

    
    

# display the image on screen and wait for a keypress
#cv2.imshow("Image", closeImg)
#cv2.waitKey(3000) & 0xFF
#cv2.destroyAllWindows()
#RCCV().pwmA1A.stop(0)
#RCCV().pwmA1B.stop(0)
#RCCV().pwmB1A.stop(0)
#pwmB1B.stop(0)
#GPIO.cleanup()
