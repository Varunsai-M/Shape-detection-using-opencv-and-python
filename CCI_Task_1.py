#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('shapes.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

for contour in contours:
	if i == 0:
		i = 1
		continue
	approx = cv2.approxPolyDP(
		contour, 0.01 * cv2.arcLength(contour, True), True)
	cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)

cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

