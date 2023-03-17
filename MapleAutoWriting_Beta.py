import os
import tools.pretreatment.ImageTreatment as pre
import tools.pretreatment.GoogleVisionAPI as gva
import tools.pretreatment.FileManage as fm
import tools.disposition.ListFilter as flt

week = 1 # 몇 주차인지 기입
guildUrl = "https://maplestory.nexon.com/Common/Guild?gid=277190&wid=5&orderby=1&page=" #크롤링을 위한 길드 홈페이지 URL

write_wb, write_ws = fm.initFile()
fm.moveImage(week)

os.chdir("./result/week" + str(week) + "/temp")
for fileName in os.listdir("./origin"):
    print("\n현재 작업 중인 파일 : ", fileName)

    # 이미지 전처리 작업
    pre.treatment(fileName)

    # Google Vision API로 글자 탐색
    name, pos, score = gva.detect(fileName)
    
    # 탐색된 단어 1차 필터링
    name = flt.filter(name, guildUrl, isName = True)
    pos = flt.filter(pos)
    score = flt.filter(score)

    # 탐색된 단어 2차 필터링
    name, pos, score = flt.final_filter(name, pos, score)

    # 임시 저장
    write_ws = fm.store(write_ws, name, pos, score)

# 엑셀파일에 저장
os.chdir("../")
write_wb.save("./week" + str(week) + ".xlsx")