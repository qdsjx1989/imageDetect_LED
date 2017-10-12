#!/usr/bin/env python
import cv2
import time
import sys
import numpy

fps=100
cap=cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FPS, fps)
ledon=0
for i in range(fps):
	ret , frame = cap.read()
	if frame[178,156][1] > 30 and frame[178,156][2] > 30:
		ledon=ledon+1
	#cv2.imwrite(str(i)+".png", frame)
print ledon
del cap
