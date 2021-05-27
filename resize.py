import cv2
import numpy as np
img=cv2.imread('lion.png')
res1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
res2=cv2.resize(img,(300,300),interpolation=cv2.INTER_CUBIC)
res3=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_CUBIC)

cv2.imshow('original image',img);
cv2.imshow('r1',res1);
cv2.imshow('r2',res2);
cv2.imshow('r3',res3);
cv2.waitKey(0)
