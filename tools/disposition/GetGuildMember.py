from bs4 import BeautifulSoup
import requests

# 크롤링을 통해 길드원 이름 배열 반환
def getMemebers(guildUrl):
    name = []
    for n in range(10):
        path = guildUrl + str(n)
        res = requests.get(path)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        p = soup.findChildren("td")
        if p != None:
            for i in range(len(p)):
                if (i % 5) == 1:
                    name.append(p[i].text.strip("\n").split("\n")[0])
                    
    return name