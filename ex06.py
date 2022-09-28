import cv2
import numpy as np

img = cv2.imread("./img/001.jpg")
img = cv2.resize(img, [700, 300])

kernal =np.ones((3, 3), np.uint8)
erode = cv2.erode(img, kernal)

ret, thresh = cv2.threshold(erode, 127, 255, cv2.THRESH_BINARY)
canny1 = cv2.Canny(thresh, 150, 200)
canny2 = cv2.Canny(thresh, 50, 200)
canny3 = cv2.Canny(thresh, 50, 100)

cv2.imshow("img", img)
cv2.imshow("canny1", canny1)
cv2.imshow("canny2", canny2)
cv2.imshow("canny3", canny3)
cv2.waitKey()
cv2.destroyAllWindows()