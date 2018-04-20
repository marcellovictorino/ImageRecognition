import cv2
import numpy as np

# Blurring and Smoothing -> remove noise from the image


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

    # Blurring: take the average of pixels
    pixelSize = 3
    kernel = np.ones((pixelSize, pixelSize), np.float)/pixelSize**2
    
    smoothed = cv2.filter2D(result, -1, kernel)
    blur = cv2.GaussianBlur(result, (pixelSize,pixelSize), 0)
    median = cv2.medianBlur(result, pixelSize, 0)
    
    # out.write(frame) # saving the video 

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

