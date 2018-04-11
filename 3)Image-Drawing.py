import cv2
import numpy as np


# Comment: CV2 is based on static image analysis.
#   But videos are just a collection of several static images. So it works pretty similar with video or image

# Using grayscale takes away different colors (3, being RGB) and +1 being Alpha (opacity)
#   it requires less processing using just grayscale

# img = cv2.imread('wristwatch.jpeg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('wristwatch.jpeg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255), 15) #xy0 , xy1 , color BGR, linewidth
cv2.rectangle(img, (15,25), (200,150), (0,0,0), 10)
cv2.circle(img, (100,63), 55, (0,0,255), 10) # center, radius, color, linewidth = -1 => fill

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorial', (0,130), font, 1, (200,200,130), 2, cv2.LINE_AA)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0

### Plotting with OpenCV
cv2.imshow('image', img)
cv2.waitKey(0) # any key closes the window
cv2.destroyAllWindows()

# cv2.imwrite('filename.png', img) # Saves the image