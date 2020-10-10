import cv2
import numpy as np

# 繪製輪廓

# m1 = cv2.imread("31.jpg", 1)
# m2 = cv2.inRange(m1, (240, 240, 240), (255, 255, 255))
# m2 = cv2.dilate(m2, np.ones((15, 30)))
# m3 = m1.copy()
# m3[:, :, :] = 255
# a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# for i in range(0, len(a)):
#     # cv2.drawContours(m3, a, i, (0, 0, 255), 2)
#     x, y, w, h = cv2.boundingRect(a[i])
#     cv2.rectangle(m1, (x, y), (x+w, y+h), (0, 0, 255), 2)
#     cv2.imshow("Image 3", m1)
#     cv2.waitKey(150)

# cv2.imshow("Image 1", m1)
# cv2.imshow("Image 2", m2)

# m1 = cv2.imread("5c3b43dbf699690021a1363e.png", 1)
# m2 = cv2.inRange(m1, (86, 18, 13), (106, 38, 33))
# m3 = cv2.bitwise_not((m2))
# m3 = cv2.add(m1, cv2.cvtColor(m3, cv2.COLOR_GRAY2BGR))
# m3 = cv2.blur(m3, (5, 5))

# m2 = cv2.morphologyEx(m2, cv2.MORPH_CLOSE, np.ones((22, 22)))
# m2 = cv2.morphologyEx(m2, cv2.MORPH_CLOSE, np.ones((1, 25)))
#
# a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# for i in range(0, len(a)):
#     x, y, w, h = cv2.boundingRect(a[i])
#     cv2.imshow("Image 3" + str(i), m1[y: y+h, x: x+w])
#     cv2.waitKey(150)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import pytesseract as pt

# 文字辨識
# 辨識結果=pt.image_to_string(圖片變數, 語言包名稱, 設定值)

# m1 = cv2.imread("D:/tesseract-Win64_3.05/tessdata/123.png")
# # -c tessedit_char_whitelist=特定要辨識的字元
# result = pt.image_to_string(m1, "my", "")
#
# print("辨識到的文字:", result)
#
# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# m1 = cv2.imread("31.jpg", 1)
# m2 = cv2.inRange(m1, (240, 240, 240), (255, 255, 255))
# m2 = cv2.dilate(m2, np.ones((15, 30)))
# a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# for i in range(0, len(a)):
#     x, y, w, h = cv2.boundingRect(a[i])
#     m3 = m1[y:y+h, x:x+w]
#     m3 =cv2.morphologyEx(m3, cv2.MORPH_OPEN, np.ones((5, 5)))
#     result = pt.image_to_string(m3, "eng", "")
#     print("辨識到的文字:", result)
#     cv2.imshow("Image 3" + str(i), m3)
#     cv2.waitKey(0)

# cv2.imshow("Image 1", m1)
# cv2.imshow("Image 2", m2)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 條碼辨識

# from pyzbar import pyzbar
#
# c1 = cv2.VideoCapture(0)
# while c1.isOpened() == True:
#     ret, m1 = c1.read()
#     if ret == True:
#         ret = pyzbar.decode(m1)
#         for d in ret:
#             print("條碼類型:", d.type)
#             try:
#                 print("內容文字:", d.data.decode("utf-8").encode("sjis").decode("utf-8"))
#             except:
#                 print("內容文字:", d.data.decode("utf-8"))
#             x, y, w, h = d.rect
#             cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)
#             print("================================")
#
#         cv2.imshow("Image 1", m1)
#         if cv2.waitKey(33)!= -1:
#             break
# cv2.destroyAllWindows()

# 辨識

cc1 = cv2.CascadeClassifier("C:/Users/pc/PycharmProjects/cascade/haarcascade_frontalface_default.xml")
c1 = cv2.VideoCapture(0)
while c1.isOpened() == True:
    ret, m1 = c1.read()
    if ret == True:
        ret = cc1.detectMultiScale(m1, minNeighbors=7, minSize=(10, 10))
        for x,y,w,h in ret:
            cv2.rectangle(m1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("Image 1", m1)
        if cv2.waitKey(33)!= -1:
            break
cv2.destroyAllWindows()