import cv2
import numpy as np

m1 = cv2.imread("h2.png", 1)

# 將B跟G都過濾掉
m1[:, :, 2]= cv2.subtract(m1[:, :, 2], m1[:, :, 1])
m1[:, :, 2]= cv2.subtract(m1[:, :, 2], m1[:, :, 0])
# 將R過濾掉
m2 = cv2.bitwise_not(m1[:, :, 2])
m2 = cv2.multiply(m2, np.full(m2.shape, 255, np.uint8))

cv2.imshow("Image 2", m2)
cv2.waitKey(0)
cv2.destroyAllWindows()