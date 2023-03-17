import difflib
import tools.disposition.GetGuildMember as gm

# 유사도검증을 통해 닉네임 보정
def findMember(detectedList, guildUrl):

    Realname = gm.getMemebers(guildUrl)

    for i in range(int(len(detectedList)/2)):
        similarList = difflib.get_close_matches(detectedList[i], Realname)
        before = detectedList[i] # 변경 전 이름

        if len(similarList) >= 1:
            detectedList[i] = similarList[0] # 제일 근사한 값으로 자동 수정
        else:
            print("근사값이 발견 되지 않은 이름 : ", before)
            detectedList[i] = input("직접 이름 입력 : ") # 근사한 값이 없을 때에는 직접 입력받음

        print("보정 결과 : ", before, " ---> ", detectedList[i])

    return detectedList