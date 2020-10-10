import cv2
import numpy as np

m1 = cv2.imread("h2.png", 1)
m2 = np.full(m1.shape, (0, 0, 255), np.uint8)
m3 = cv2.subtract(m1, m2)
m4 = cv2.cvtColor(m3, cv2.COLOR_BGR2GRAY)
m4_1 = cv2.cvtColor(m4, cv2.COLOR_GRAY2BGR)

m5 = np.full(m1.shape, 255, np.uint8)
m6 = cv2.multiply(m4_1, m5)


cv2.imshow("Image 1", m1)
cv2.imshow("Image 2", m5)
cv2.imshow("Image 3", m6)



cv2.waitKey(0)
cv2.destroyAllWindows()