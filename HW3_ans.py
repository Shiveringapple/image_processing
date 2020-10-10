import cv2
import numpy as np

c1 = cv2.VideoCapture("h3.mp4")
# 建立變數當作背景
mb = np.full((0), 255, np.uint8)

while c1.isOpened() == True:
    ret, m1 = c1.read()
    if ret == True:
        m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2HSV)
        if mb.shape[0] == 0:
            mb = m2.copy()
        m2 = cv2.subtract(m2, mb)
        th, m2 = cv2.threshold(m2[:, :, 1], 127, 255, cv2.THRESH_BINARY)
        m2 = cv2.dilate(m2, np.ones((10, 10)))
        a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for i in range(0, len(a)):
            x, y, w, h = cv2.boundingRect((a[i]))
            cv2.rectangle(m1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("Image 1", m1)
        cv2.imshow("Image 2", m2)
        if cv2.waitKey(33)!=-1:
            break
    else:
        break
cv2.destroyAllWindows()
