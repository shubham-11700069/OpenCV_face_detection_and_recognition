import cv2
import numpy as np
import os
import pickle
from PIL import Image

face_front_cascade=cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
#face_right_cascade=cv2.CascadeClassifier('data/haarcascade_profileface.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels={}
with open("labels.pickle","rb") as f:
	labels=pickle.load(f)
	labels={v:k for k,v in labels.items()}

cap=cv2.VideoCapture(0)


while(True):
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_front_cascade.detectMultiScale(frame,scaleFactor=1.5, minNeighbors=3)
	#right_sideF=face_right_cascade.detectMultiScale(frame,scaleFactor=2, minNeighbors=3)
	conf_ls=[]
	idx=1
	for(x,y,w,h) in faces:
		#print(x,y,w,h)
		roi_color=frame[y:y+h,x:x+w]
		roi_gray=gray[y:y+h,x:x+w]
		
		id_, conf=recognizer.predict(roi_gray)
		conf_ls.append(conf)
		if(idx>1):
			#print(id_)
			#print(labels[id_])
			font=cv2.FONT_HERSHEY_SIMPLEX
			name=labels[id_]
			color=(255,255,255)
			stroke=2
			if(conf==max(conf_ls) or conf>80):
				cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

		color=(0,0,255) #BGR
		stroke=3
		cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)
		idx+=1

	'''for(x,y,w,h) in right_sideF:
		#print(x,y,w,h)
		roi_color=frame[y:y+h,x:x+w]

		color=(0,255,0) #BGR 
		stroke=5
		cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)'''

	cv2.imshow('frame',frame)

	if(cv2.waitKey(20) & 0xFF==ord('q')):
		break

#cv2.DestroyAllWindows()