import numpy as np
import cv2

img = cv2.imread('opencv-corner-detection-sample.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray) # type conversion

                    img , # of corners, quality, min distance between corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners) # type conversion

for corner in corners:
    x,y = corner.ravel() # algorithm to find corners. Retunr center
    cv2.circle(img,(x,y),3,255,-1) #draw a circle Radius=3 around the corner
    
cv2.imshow('Corner',img)

### Using Video
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = np.float32(gray)
#                     # img , # of corners, quality, min distance between corners
#     corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 100)
#     corners = np.int0(corners)

#     for corner in corners:
#         x,y = corner.ravel() # algorithm to find corners. Retunr center
#         cv2.circle(frame,(x,y),5,255,-1) #draw a circle Radius=3 around the corner   


#     cv2.imshow('original', frame)
    

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cap.release()
#         cv2.destroyAllWindows()
#         break