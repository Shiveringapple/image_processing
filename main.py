import cv2
import numpy as np



# 圖片
# m1 = cv2.imread("100.jpg", 1)
#
# # print(m1[0, 0])
#
# print(m1.shape)
# print("高度:", m1.shape[0])
# print("寬度:", m1.shape[1])
#
# m1 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
#
# print(m1.shape)
# print("高度:", m1.shape[0])
# print("寬度:", m1.shape[1])
#
# m1 = cv2.cvtColor(m1, cv2.COLOR_GRAY2BGR)
#
# # cv2.imwrite("./1.jpg", m1)
# cv2.imwrite("./1.jpg", m1, [cv2.IMWRITE_JPEG_QUALITY, 100])
#
# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 影片
#
# c1 = cv2.VideoCapture(0)
# while c1.isOpened() == True:
#     ret, m1 = c1.read()
#     if ret == True:
#         cv2.imshow("Image 1", m1)
#         # 每33毫秒執行
#         # print(cv2.waitKey(33))
#         if cv2.waitKey(33) != -1:
#             break
# cv2.destroyAllWindows()


# c1 = cv2.VideoCapture("kono-dio-da-hd.mp4")
#
# print("寬度:", c1.get(3))
# print("高度:", c1.get(4))
# print("FPS:", c1.get(5))
# print("總影格數:", c1.get(7))
# c1.set(1, 1450)
#
# while c1.isOpened() == True:
#     ret, m1 = c1.read()
#     if ret == True:
#         print("當前影格:", c1.get(1))
#         cv2.imshow("Image 1", m1)
#         # 每33毫秒執行
#         # print(cv2.waitKey(33))
#     if cv2.waitKey(33) != -1:
#         break
# cv2.destroyAllWindows()

# 視訊存檔
# c1 = cv2.VideoCapture(0)
#
# format1 = cv2.VideoWriter_fourcc(*'MP4V')
#
# imageWidth = int(c1.get(3))
# imageHeight = int(c1.get(4))
#
# c2 = cv2.VideoWriter("./2.mp4", format1, 30, (imageWidth, imageHeight))
#
#
# while c1.isOpened() == True:
#     ret, m1 = c1.read()
#     if ret == True:
#         cv2.imshow("Image 1", m1)
#         if cv2.waitKey(33) != -1:
#             break
# c2.release()
# cv2.destroyAllWindows()


# 新建一張圖片
# 圖像變數=np.full((高, 寬, 3), 初始顏色值, np.uint8)
# m1 = np.full((300, 500, 3), (140, 180, 210), np.uint8)
#
# # 畫直線
# cv2.line(m1, (10, 10), (250, 10), (0, 0, 255), 2)
#
# # 畫矩形
# cv2.rectangle(m1, (10, 30), (250, 70), (0, 0, 255), 2)
# cv2.rectangle(m1, (10, 30), (250, 120), (0, 0, 255), -1)
#
# # 畫圓形
# cv2.circle(m1, (400, 250), 50, (0, 0, 255), 2)
# cv2.circle(m1, (400, 50), 50, (0, 0, 255), -1)

# 寫字
from PIL import ImageFont, ImageDraw, Image
m1 = np.full((300, 500, 3), (140, 180, 210), np.uint8)

# PIL圖像變數=Image.fromarray(OpenCV圖像變數)
m1 = Image.fromarray(m1)
# ImageFont.truetype(TTF字型檔位置, 文字大小)
setting = ImageFont.truetype("./kaiu.ttf", 50)
# ImageDraw.Draw(PIL圖像變數).text(文字位置, 要寫的文字, 顏色, 設定)
ImageDraw.Draw(m1).text((50, 50), "測試", (0, 0, 255), setting)
m1 = np.array(m1)





















cv2.imshow("Image 1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()