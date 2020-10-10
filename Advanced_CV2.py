import cv2
import numpy as np
# 影像二值化：整個圖片用兩個顏色表示 --> 簡化顏色 以利後面方便處理
# 難度在於只剩純黑跟純白兩個顏色 還可以看出原本的圖片是甚麼
# m1 = cv2.imread("100.jpg", 1)
# m2 = m1.copy()
# 變數一, 變數二=cv2.threshold(圖像變數, 門檻值, 最大值, 方法)
# th, m2[:, :, 0] = cv2.threshold(m1[:, :, 0], 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:, :, 1] = cv2.threshold(m1[:, :, 1], 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:, :, 2] = cv2.threshold(m1[:, :, 2], 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)

# m2[:, :, 0] = cv2.adaptiveThreshold(m1[:, :, 0], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 0)
# m2[:, :, 1] = cv2.adaptiveThreshold(m1[:, :, 1], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 0)
# m2[:, :, 2] = cv2.adaptiveThreshold(m1[:, :, 2], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 0)


# m2=cv2.adaptiveThreshold(  # 結果圖像=cv2.adaptiveThreshold(
# m1,  # 圖像變數,
# 255,  # 最大值,
# cv2.ADAPTIVE_THRESH_MEAN_C,  # 方法一,
# cv2.THRESH_BINARY,  # 方法二,
# 3,  # 區塊大小,
# 0  # 微調值
# )

# 邊緣偵測
# 結果圖像=cv2.Canny(圖像變數, 門檻值1, 門檻值2)
# m2 = cv2.Canny(m1, 20, 100)

# 模糊化
# 平均值模糊法
# 結果圖像=cv2.blur(圖像變數, 範圍大小)
# m2 = cv2.blur(m1,(50,50))

# 中值模糊法
# 結果圖像=cv2.medianBlur(圖像變數, 處理數量)
# m2 = cv2.medianBlur(m1, 51)

# 銳利化
# 結果圖像=cv2.equalizeHist(圖像變數)
# m1 = cv2.imread("6.jpg", 1)
# m2 = m1.copy()
# m2[:, :, 0] = cv2.equalizeHist(m1[:, :, 0])
# m2[:, :, 1] = cv2.equalizeHist(m1[:, :, 1])
# m2[:, :, 2] = cv2.equalizeHist(m1[:, :, 2])

# 侵蝕(色彩值低的會侵蝕色彩值高的)
# 結果圖像=cv2.erode(圖像變數, 結構陣列)
# m1 = cv2.imread("NIKE.png", 1)
# m2 = cv2.erode(m1, np.ones((10, 10)))

# 膨脹(色彩值高的會侵蝕色彩值低的)
# 結果圖像=cv2.dilate(圖像變數, 結構陣列)
# m1 = cv2.imread("NIKE.png", 1)
# m2 = cv2.dilate(m1, np.ones((20, 1)))

# 去雜訊(藉由侵蝕再膨脹一來一回先去雜訊再把受影響的部分復原)
# cv2.MORPH_OPEN：先執行侵蝕後執行膨脹
# cv2.MORPH_CLOSE：先執行膨脹後執行侵蝕
# cv2.MORPH_GRADIENT：執行膨脹與侵蝕產生的變化差
# 結果圖像=cv2.morphologyEx(圖像變數, 方法, 結構陣列)
# m1 = cv2.imread("4.jpg", 1)
# m2 = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((4, 4)))

# 顏色篩選(判斷圖像裡的各項素是否在指定色彩範圍內)
# 結果圖像=cv2.inRange(圖像變數, 顏色下限, 顏色上限)
# m2 =cv2.inRange(m1, (160, 90, 61), (210, 140, 111))

# 尋找輪廓
# 輪廓點, 輪廓階層資料=cv2.findContours(圖像變數(只支援灰階圖像),類型,方法)
# 圖像要先變成黑白
# m1 = cv2.imread("NIKE.png", 1)
# m2 = cv2.inRange(m1, (0, 0, 0), (225, 225, 225))
#
# a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(b)

# 繪製輪廓
# cv2.drawContours
# m3 = m1.copy()
# m3[:, :, :] = 255
# cv2.drawContours(m3, a, -1, (0, 0, 255), 2)

c1 = cv2.VideoCapture(0)
while c1.isOpened() == True:
    ret, m1 = c1.read()
    if ret == True:
        # 邊緣偵測
        C = cv2.Canny(m1, 20, 100)
        # 平均值模糊法
        B = cv2.blur(m1,(50,50))
        # 中值模糊法
        MB = cv2.medianBlur(m1, 51)
        # 銳利化
        EH = m1.copy()
        EH[:, :, 0] = cv2.equalizeHist(m1[:, :, 0])
        EH[:, :, 1] = cv2.equalizeHist(m1[:, :, 1])
        EH[:, :, 2] = cv2.equalizeHist(m1[:, :, 2])
        # 侵蝕
        ER = cv2.erode(m1, np.ones((20, 1)))
        # 膨脹
        DL = cv2.dilate(m1, np.ones((20, 1)))
        # 去雜訊
        MPL = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((4, 4)))
        # 輪廓
        IR = cv2.inRange(m1, (50, 50, 50), (150, 150, 150))
        a, b = cv2.findContours(IR, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        IRI = m1.copy()
        IRI[:, :, :] = 255
        cv2.drawContours(IRI, a, -1, (0, 0, 255), 2)

        cv2.imshow("邊緣偵測", C)
        cv2.imshow("平均值模糊", B)
        cv2.imshow("中值模糊", MB)
        cv2.imshow("銳利化", MPL)
        cv2.imshow("侵蝕", ER)
        cv2.imshow("膨脹", DL)
        cv2.imshow("輪廓", IRI)


        # 每33毫秒執行
        # print(cv2.waitKey(33))
        if cv2.waitKey(33) != -1:
            break
cv2.destroyAllWindows()


# cv2.imshow("Image 1", m1)
# cv2.imshow("Image 2", m2)
# cv2.imshow("Image 3", m3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()