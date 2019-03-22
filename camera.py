import numpy as np
import os
import cv2
import time
import keyboard
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"images")
cap=cv2.VideoCapture(0)
j=0
while (True):

	ret,frame=cap.read()
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
	cv2.imshow('image',frame)
	
	if(keyboard.is_pressed('t')):
		cv2.imwrite("images/ankit/%d.jpg"%j,frame)
		j+=1
	#cv2.waitKey(0)
	if(cv2.waitKey(20) & 0xFF==ord('q')):
		break

cap.release()
cv2.destroyAllWindows()