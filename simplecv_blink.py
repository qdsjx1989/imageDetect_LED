#!/usr/bin/env python
from SimpleCV import *
from sys import argv
import sys
import time

count=0
MAX=10
img=[];
cropImg=[];
flag=[];

target=argv[1]

camera=Camera()
time.sleep(2)

if target != "tel1" and target != "tel2":
	sys.exit(0)


#print(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
for count in range(MAX):
	img.append(camera.getImage())
	time.sleep(0.1)
#print(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))

for count in range(MAX):
	if target == "tel1":
		tmp2=img[count].crop(150,130,50,55)
	elif target == "tel2":
		tmp2=img[count].crop(242,120,50,55)
	cropImg.append(tmp2)
#	img[count].save(str(count)+".png")

for count in range(MAX):
	if cropImg[count].meanColor()[1]>80 and cropImg[count].meanColor()[2] >80:
		flag.append(True)
#		print(count)
#		print(cropImg[count].meanColor()[0])
#		print(cropImg[count].meanColor()[1])
#		print(cropImg[count].meanColor()[2])
	else:
		flag.append(False)
#		print(count)
#		print(cropImg[count].meanColor()[0])
#		print(cropImg[count].meanColor()[1])
#		print(cropImg[count].meanColor()[2])

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
