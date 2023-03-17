import tools.disposition.CheckDiff as cd

# 최초로 GVA에서 반환된 값을 1차 검열
def filter(list, guildUrl = "", isName = False):

    blackList = ['10A', "LO"] # 자주 오류나는 문자
    result = [] # 반환 값

    for i in range(len(list)):
        if (list[i] not in blackList):
            result.append(list[i])

    if isName == True :
        result = cd.findMember(result, guildUrl)

    return result


def final_filter(name, pos, score):

    if len(name) != 34 or len(pos) != 17 or len(score) != 51: # 일반적인 케이스는 통과
        while (True):            
            printContent(name, pos, score)
            if int(input("문제 없을 시 0, 있을 시 1 : ")) == 1:
                num = int(input("수정할 리스트 (이름, 레벨 ->  0, 직위 -> 1, 점수 -> 2) : "))
                if num == 0:
                    name = changeContent(name)
                elif num == 1:
                    pos = changeContent(pos) 
                elif num == 2:
                    score = changeContent(score)    
                else :
                    break
            else :
                break

    return name, pos, score


def printContent(name, pos, score):
    print(name);print(len(name))
    print(pos);print(len(pos))
    print(score);print(len(score))
    
def changeContent(ret):
    mode = int(input("삭제 1, 변경 2, 추가 3: "))
    index = int(input("고칠 인덱스 : "))
    if mode == 1 :
        del ret[index]; print("삭제 완료")
    elif mode == 2:
        ret[index] = input("내용 : "); print("변경 완료")
    else :
        ret.insert(index, input("내용 : ")); print("추가 완료")
    
    return ret