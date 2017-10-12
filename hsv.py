#!/usr/bin/env python
import cv2
img=cv2.imread("demo4.jpg")
#img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
for i in range(480):
	for j in range(640):
		print img[i,j]
