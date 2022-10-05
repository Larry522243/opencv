import cv2, numpy as np
from cv2 import threshold

img = cv2.imread("./img/test3.jpg", 1)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
pts1 = np.float32([[64, 174], [510, 60], [529, 178], [108, 327]])
pts2 = np.float32([[0, 0], [520, 0], [520, 180], [0, 180]])
M = cv2.getPerspectiveTransform(pts1, pts2)
res = cv2.warpPerspective(img, M, (520, 180))
ret, thresh = cv2.threshold(res, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
fin = res.copy()
dst = cv2.drawContours(fin, contours, -1, (0, 255, 255), 3)

# cv2.imshow("img", img)
cv2.imshow("res", res)
cv2.imshow("threshold", thresh)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()