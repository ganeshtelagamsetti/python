import cv2
import numpy as np
Img=cv2.imread('lion.png');
cv2.imshow('Original Image', Img);
gray=cv2.cvtColor (Img, cv2.COLOR_BGR2GRAY);
cv2.imshow('Gray image',gray);
cv2.waitKey (0)
cv2.destroyAllWindows()
