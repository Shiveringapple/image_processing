import cv2
import numpy as np

m1 = cv2.imread("NIKE.png", 1)
m2 = np.full(m1.shape, 200, np.uint8)
# 數值相加：m1 + 200的灰階色彩空間
m3 = cv2.add(m1, m2)
# 數值相加：m1 - 200的灰階色彩空間
m4 = cv2.subtract(m1, m2)

# 彩色空間的數值相加減，可以用來過濾過花的背景，以達到方便文字辨識的效果
m5 = np.full(m1.shape, (255, 0, 0), np.uint8)
m6 = cv2.add(m1, m5)
# 圖像相減(<0會等於0)
m7 = cv2.subtract(m1, m5)

# 圖像相減(<0會絕對值)
m8 = np.full(m1.shape, 255, np.uint8)
m9 = cv2.absdiff(m1, m8)

# 圖像相除
m10 = np.full(m1.shape, 200, np.uint8)
m11 = cv2.divide(m1, m10)

# 圖像相乘
m12 = np.full(m1.shape, 255, np.uint8)
m13 = cv2.multiply(m1, m12)

# 二進位
m14 = cv2.bitwise_not(m1)

#
m15 = m1 * 100

# h = 300
# w = int((h/m1.shape[0])*m1.shape[1])

w = 300
h = int((w/m1.shape[1])*m1.shape[0])

m99 = cv2.resize(m1, (w, h))









cv2.imshow("Image 1", m99)

cv2.waitKey(0)
cv2.destroyAllWindows()