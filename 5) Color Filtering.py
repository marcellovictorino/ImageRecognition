import cv2
import numpy as np

# Comment: CV2 is based on static image analysis.
#   But videos are just a collection of frames / several static images. So it works pretty similar with video or image

# Using grayscale takes away different colors (3, being RGB) and +1 being Alpha (opacity)
#   it requires less processing using just grayscale

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

    # out.write(frame) # saving the video

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

