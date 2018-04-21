import cv2
import numpy as np

# Blurring and Smoothing -> remove noise from the image
# Morphological transformation, better than previous methods


cap = cv2.VideoCapture(0) # 0 means the first available webcam

# Saving the video output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) # FPS , Resolution

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Hue Saturation Value - better then using classic RGB, since color elements are independent
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_blue = np.array([90,0,0]) # Hue, Saturation, Value
    upper_blue = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue) # everything that is within these ranges
    result = cv2.bitwise_and(frame, frame, mask= mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dialation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('result', result)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()