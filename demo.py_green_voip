#!/usr/bin/env python
import cv2
import time
import numpy

from SimpleCV import *

def getPic():
	camera=Camera()
	time.sleep(2)
	img=camera.getImage()
	del camera
	img.save("haha.jpg")
	

getPic()
srcImg=cv2.imread("haha.jpg")

blueChannel,greChannel,redChanne=cv2.split(srcImg)
blueChannel=cv2.blur(blueChannel, (20,20))
midImg1=blueChannel
rows=blueChannel.shape[0]
cols=blueChannel.shape[1]
for i in range(rows):
	for j in range(cols):
		blue=blueChannel[i][j]
		red=redChanne[i][j]
		gre=greChannel[i][j]
		if blue > 100 and blue < 130 and red > 150 and red < 200 and gre > 180 and gre < 220:
			midImg1[i][j] = 1
		else:
			midImg1[i][j] = 0
midImg2=midImg1
element=cv2.getStructuringElement(cv2.MORPH_RECT,(20,20));
midImg2=cv2.morphologyEx(midImg1,cv2.MORPH_CLOSE,element)
contours,hierarchy = cv2.findContours(midImg2,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
midImg3=cv2.drawContours(midImg2,contours,-1,(255,255,255),8)
cv2.imshow("c", midImg2)
cv2.waitKey(0)

#find the max rect contours
maxRect = cv2.minAreaRect(contours[0])
for i in range(len(contours)):
	tmpRect = cv2.minAreaRect(contours[i])
	if tmpRect[1][0] > maxRect [1][0] and tmpRect[1][1] > maxRect [1][1]:
		maxRect = tmpRect
#need check if contours get 
#rect = cv2.minAreaRect(contours[0])
print maxRect[0]
print maxRect[1]

x=maxRect[0][0]
x=int(x)
y=maxRect[0][1]
y=int(y)
target = srcImg[y,x]

print x,y
print target
if target[1]>160 and target[2] >160:
        print("led power on")
else:
        print("led power off")


