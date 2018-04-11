import cv2
import numpy as np
import matplotlib.pyplot as plt

# Comment: CV2 is based on static image analysis.
#   But videos are just a collection of several static images. So it works pretty similar with video or image

# Using grayscale takes away different colors (3, being RGB) and +1 being Alpha (opacity)
#   it requires less processing using just grayscale

img = cv2.imread('wristwatch.jpeg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0

### Plotting with MatPlotLib - allows to add other layers of information
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5) # adding a line, color 'c' = Cyan
# plt.show()

### Plotting with OpenCV
# cv2.imshow('image', img)
# cv2.waitKey(0) # any key closes the window
# cv2.destroyAllWindows()

# cv2.imwrite('filename.png', img) # Saves the image

