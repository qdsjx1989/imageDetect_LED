#!/usr/bin/env python
import cv2
import time
import sys
import numpy
from SimpleCV import *

x=180
y=180

def getPic():
	camera=Camera()
	time.sleep(2)
	img=camera.getImage()
	del camera
	img.save("haha.jpg")
	

getPic()
srcImg=cv2.imread("haha.jpg")

target = srcImg[y,x]
print target

if target[1]>80 and target[2] >80:
        print("led power on")
else:
        print("led power off")


