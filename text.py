import cv2
import numpy as np
img=cv2.imread('lion.png')
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'lion king',(10,500),font,2,(225,0,1),2,cv2.LINE_AA)
cv2.imshow('IMAGE TEXT MARKED',img)
