import cv2
import numpy as np
import matplotlib.pyplot as plt

# Comment: CV2 is based on static image analysis.
#   But videos are just a collection of frames / several static images. So it works pretty similar with video or image

# Using grayscale takes away different colors (3, being RGB) and +1 being Alpha (opacity)
#   it requires less processing using just grayscale

cap = cv2.VideoCapture(0) # 0 means the first available webcam

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0

### Plotting with OpenCV
# cv2.imshow('image', img)
# cv2.waitKey(0) # any key closes the window
# cv2.destroyAllWindows()

# cv2.imwrite('filename.png', img) # Saves the image