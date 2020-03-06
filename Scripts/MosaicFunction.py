#モザイク掛け機能
import cv2
Imagefile = "C://python//BlogMosaicPython//Image//lena.jpg"
######## 画面の一部をモザイク処理 ###################
MOSAIC = cv2.imread(Imagefile, 1)

#画像に対してモザイクをかける
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

#モザイクの範囲を決定
def mosaic_area(img, x, y, width, height, ratio=0.1):
    dst = img.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

#特定の位置に特定の大きさのモザイクをかける
dst_area = mosaic_area(MOSAIC, 0, 0, 150, 150)
cv2.imwrite("../Image/mosaic.jpg", dst_area)
######################################
