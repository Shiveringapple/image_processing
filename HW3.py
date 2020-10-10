import cv2
import numpy as np

c1 = cv2.VideoCapture("h3.mp4")
while c1.isOpened() == True:
    ret, m1 = c1.read()
    if ret == True:
        m2 = cv2.inRange(m1, (100, 50, 20), (225, 100, 100))
        m2 = cv2.morphologyEx(m2, cv2.MORPH_CLOSE, np.ones((60, 60)))
        cv2.imshow("Image 4", m2)

        a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for i in range(0, len(a)):
            # cv2.drawContours(m3, a, i, (255, 0, 0), 2)
            x, y, w, h = cv2.boundingRect(a[i])
            cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("Image 3", m1)
        if cv2.waitKey(33) != -1:
            break
    else:
        break
cv2.destroyAllWindows()


