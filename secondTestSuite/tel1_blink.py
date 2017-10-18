#!/usr/bin/env python
from SimpleCV import *
import time

count=0
MAX=8
img=[];
cropImg=[];
flag=[];

x=260
y=168

camera=Camera()

time.sleep(2)

for count in range(MAX):
	img.append(camera.getImage())
	time.sleep(0.1)

for count in range(MAX):
	tmp2=img[count][x,y]
	print tmp2
	cropImg.append(tmp2)
	#img[count].save(str(count)+".png")

for count in range(MAX):
	if cropImg[count][1]>80 and cropImg[count][2] >80:
		flag.append(True)
	else:
		flag.append(False)

blink=False
for count in range(MAX):
	if flag[count] != flag[0]:
		blink = True
		break
if blink == True:
	print("blinking")
else:
	print("no blinking")

del camera
