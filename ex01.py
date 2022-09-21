import cv2

img = cv2.imread("001.jpg", 0)

cv2.imshow("opencv", img)
cv2.waitKey()
cv2.destroyAllWindows()