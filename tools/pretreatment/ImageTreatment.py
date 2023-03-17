import os
from PIL import Image
import numpy as np
import cv2

origin_path = "./origin/"
cutted_path = "./cutted/"

def treatment(fileName):
    pre_cut(fileName)
    extraction(fileName)
    clearImage(fileName)
    labelling(fileName)
    post_cut(fileName)

def pre_cut(fileName): # 점수 부분만 자름
    image = Image.open(origin_path + fileName)
    croppedImage=image.crop((500,155,957,565))
    croppedImage.save(cutted_path + fileName )

def extraction(fileName): # 색 제거 후 반전
    path = cutted_path + fileName
    image = cv2.imread(path)
    bgrResult = cv2.bitwise_not(bgrExtraction(image))
    cv2.imwrite(path, bgrResult)

def bgrExtraction(image): # BGR로 특정 색을 추출하는 함수 (배경제거)
    bgrLower = np.array([179, 179, 179])    # 추출할 색의 하한
    bgrUpper = np.array([255, 255, 255])    # 추출할 색의 상한
    img_mask = cv2.inRange(image, bgrLower, bgrUpper) 
    return cv2.bitwise_and(image, image, mask=img_mask)

def clearImage(fileName):
    src = cv2.imread(cutted_path + fileName, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        cv2.drawContours(src, [contours[i]], 0, (0, 0, 0), 1)

    cv2.imwrite(cutted_path + fileName, src)

def labelling(fileName):
    src1 = cv2.imread(cutted_path + fileName)
    src2 = cv2.imread("./labellingFilter.png")
    src3 = cv2.add(src1, src2)
    src4 = src3 + src2
    cv2.imwrite(cutted_path + fileName, src4)

def post_cut(fileName):
    pos_x1 = [0, 187, 252]
    pos_x2 = [190, 255, 454]
    name = ["name/", "position/", "score/"]
    image = Image.open(cutted_path + fileName)

    for i in range(3):     
        croppedImage = image.crop((pos_x1[i],0, pos_x2[i],406))
        croppedImage.save("./" + name[i] + fileName)