import cv2, numpy as np
img = cv2.imread("./img/test6.jpg", 1)
img = cv2.resize(img, [378, 504])
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernal =np.ones((5, 5), np.uint8)
erode = cv2.erode(imgGray, kernal)

ret, thresh = cv2.threshold(erode, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
canny = cv2.Canny(thresh, 40, 200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
fin = img.copy()
dst = cv2.drawContours(fin, contours, -1, (0, 255, 255), 2)

cv2.imshow("img", imgGray)
cv2.imshow("threshold", thresh)
cv2.imshow("canny", canny)
cv2.imshow("contours", dst)
cv2.waitKey()
cv2.destroyAllWindows()