import cv2
import numpy as np

x = 0
v = 5

while True:
    m1 = np.full((300, 500, 3), 255, np.uint8)
    cv2.rectangle(m1, (x, 100), (x+100, 200), (255, 0, 0), -1)
    x += v
    if x + 100 >= 500 or x <= 0:
        v = -v
    cv2.imshow("Image 1", m1)
    if cv2.waitKey(33) != -1:
        break

cv2.destroyAllWindows()