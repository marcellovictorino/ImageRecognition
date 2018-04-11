import cv2
import numpy as np


# img = cv2.imread('wristwatch.jpeg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('wristwatch.jpeg', cv2.IMREAD_COLOR)

threshold_cut = 25 # set threshold level, any pixel higher than this will be set to maximum value. Values below will be black
threshold_maxValue = 255

retval, threshold = cv2.threshold(img, threshold_cut, threshold_maxValue, cv2.THRESH_BINARY) 

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, threshold_cut, threshold_maxValue, cv2.THRESH_BINARY) 

# Advanced: able to retrieve information from low light, different levels images!
gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
### Plotting with OpenCV
cv2.imshow('original', img)
cv2.imshow('modified', threshold)
cv2.imshow('Gray Scale', threshold2)
cv2.imshow('Gaussian Adaptive', gauss)

cv2.waitKey(0) # any key closes the window
cv2.destroyAllWindows()

# cv2.imwrite('filename.png', img) # Saves the image