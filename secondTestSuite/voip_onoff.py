#!/usr/bin/env python
import cv2
import time
import sys
import numpy
from SimpleCV import *

x=100
y=195

def getPic():
	camera=Camera()
	time.sleep(2)
	img=camera.getImage()
	del camera
	img.save("haha.jpg")
	

getPic()
srcImg=cv2.imread("haha.jpg")

target = srcImg[y,x]

if target[1]>160 and target[2] >160:
        print("led power on")
else:
        print("led power off")


