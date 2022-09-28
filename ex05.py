import cv2
img = cv2.imread("./img/001.jpg", 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
thresh5 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
ret, thresh6 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)


cv2.imshow("img", img)
cv2.imshow("thresh1", thresh1)
cv2.imshow("thresh2", thresh2)
cv2.imshow("thresh3", thresh3)
cv2.imshow("thresh4", thresh4)
cv2.imshow("thresh5", thresh5)
cv2.imshow("thresh6", thresh6)

cv2.waitKey()
cv2.destroyAllWindows()