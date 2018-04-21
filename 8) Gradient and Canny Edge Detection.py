import cv2
import numpy as np

# Gradients and Canny Edge Detections

cap = cv2.VideoCapture(0) # 0 means the first available webcam

# Saving the video output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) # FPS , Resolution

while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    edges = cv2.Canny(frame, 150,200)


    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('edges', edges)
    
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()