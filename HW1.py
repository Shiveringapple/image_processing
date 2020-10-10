import cv2
import numpy as np


def forword():
    width = 0
    while width < 400:
        m1 = np.full((300, 500, 3), (140, 180, 210), np.uint8)
        cv2.rectangle(m1, (width, 30), (width + 100, 130), (0, 0, 255), 2)
        width = width + 10
        cv2.imshow("Image 1", m1)
        if cv2.waitKey(33) != -1:
            break

def backword():
    width = 400
    while width > 0:
        m1 = np.full((300, 500, 3), (140, 180, 210), np.uint8)
        cv2.rectangle(m1, (width, 30), (width + 100, 130), (0, 0, 255), 2)
        width = width - 10
        cv2.imshow("Image 1", m1)
        if cv2.waitKey(33) != -1:
            break

while True:
    # print("1")
    forword()
    # print("2")
    backword()


cv2.destroyAllWindows()