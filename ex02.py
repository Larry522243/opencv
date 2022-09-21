import cv2

img = cv2.imread("001.jpg", 1)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Before", img)
cv2.imshow("HSV", img1)
cv2.waitKey()
cv2.destroyAllWindows()