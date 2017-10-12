#!/usr/bin/env python
from SimpleCV import *
from sys import argv
import sys
import time

target=argv[1]

filename=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())

def getCentorXy():
{
	srcImg=cv2.imread("haha.jpg")
	xianshi=srcImg
	blueChannel,greChannel,redChanne=cv2.split(xianshi)
	blueChannel=cv2.blur(blueChannel, (20,20))
	midImg1=blueChannel
	rows=blueChannel.shape[0]
	cols=blueChannel.shape[1]
	for i in range(rows):
        	for j in range(cols):
                	blue=blueChannel[i][j]
                	red=redChanne[i][j]
                	gre=greChannel[i][j]
                	if blue > 170 and blue < 220 and red > 200 and gre > 180 and gre < 220:
                        	midImg1[i][j] = 1
                	else:
                        	midImg1[i][j] = 0
	midImg2=midImg1
	element=cv2.getStructuringElement(cv2.MORPH_RECT,(20,20));
	midImg2=cv2.morphologyEx(midImg1,cv2.MORPH_CLOSE,element)
	contours,hierarchy = cv2.findContours(midImg2,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
	midImg3=cv2.drawContours(midImg2,contours,-1,(255,255,255),8)
	rect = cv2.minAreaRect(contours[0])
	return rect[0]
}

camera=Camera()
time.sleep(2)
img1=camera.getImage()
img1.save(filename+"onoff.png")
if target == "voip":
	img2=img1.crop(370,120,50,50)
elif target == "tel1":
	img2=img1.crop(150,130,50,50)
elif target == "tel2":
	img2=img1.crop(242,120,50,50)
else:
	sys.exit(0)

if img2.meanColor()[1]>160 and img2.meanColor()[2] >160:
	print("led power on")
	print(img2.meanColor()[0])
	print(img2.meanColor()[1])
	print(img2.meanColor()[2])
else:
	print("led power off")
	print(img2.meanColor()[0])
	print(img2.meanColor()[1])
	print(img2.meanColor()[2])

del camera
