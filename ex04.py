# OpenCV的色彩空間與應用
# Import only if not previously imported
# 過濾白色 實作
import cv2
import numpy as np
hmin = 0
hmax = 180
smin = 0
smax = 30
vmin = 221
vmax = 255

# In VideoCapture object either Pass address of your Video file
# Or If the input is the camera, pass 0 instead of the video file
img = cv2.imread("./img/001.jpg", 1)
cv2.imshow('Before', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lowerb = np.array([hmin, smin, vmin])
upperb = np.array([hmax, smax, vmax])
mask = cv2.inRange(hsv, lowerb, upperb)
img = cv2.bitwise_and(img, img, mask=mask)
# Display the resulting img
cv2.imshow('hsv', hsv)
cv2.imshow('img', img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()