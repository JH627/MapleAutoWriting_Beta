import os
from openpyxl import Workbook
import shutil as sh

# 엑셀 기본 값 설정
def initFile():
    write_wb = Workbook()
    write_ws = write_wb.active
    category = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
    content = ['닉네임', '레벨', '직위', '주간점수', '수로', '플래그']

    for i in range(len(category)):
        write_ws[category[i]] = content[i]

    return write_wb, write_ws

# 파일 생성 후 각 주차별 위치로 이미지 이동
def moveImage(week):
    week = "week" + str(week)
    category = ["name", "position", "score", "origin", "cutted"]

    for dir in category:
        folder_dir = "./result/" + week + "/temp/" + dir
        os.makedirs(folder_dir, exist_ok = True)

    for file in os.listdir("./originImage"):
        src = "./originImage/"
        dir = "./result/" + week + "/temp/origin/"
        sh.move(src + file, dir + file)

    sh.copy2("./labellingFilter.png", "./result/" + week + "/temp")

# 작업중인 시트에 저장
def store(write_ws, name, pos, score):
    size = len(pos)
    for i in range(size):
        write_ws.append([name[i], name[i+size], pos[i], score[i], score[i + size], score[i + 2 * size]])
    
    return write_ws