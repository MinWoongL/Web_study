import requests
from bs4 import BeautifulSoup

# requests 라이브러리로 특정 HTML 페이지 요청

# HTML 요청
res = requests.get('https://finance.naver.com/sise/lastsearch2.naver')

# HTML을 parsing
soup = BeautifulSoup(res.content, "html.parser")
# title 검색
# find, find_all
lines = soup.select('.type_5 tr')
count = -1
temp = []
list = []
list_new = []
new_dict = dict()
data = soup.find('title').text
print(data)


for line in lines:
    # count += 1;
    #
    # if count == 0 or count == 61 or count == 62 or count == 63:
    #     print(count)
    # else:
    #     temp.append(line.text.strip())
    #
    # print(line.text.strip())
    # if count % 12 == 0:
    #     print(temp)
    #     list.append(temp)
    #     print(list)
    #     print('----------')
    #     temp.clear()
    # if count == 63:
    #     count = 0
    # list_new = list
    print(line)

# print(temp)
# print(list_new)
# for i in list:
#     print(i)
# 순위, 종목명, 검색비율, 현재가, 전일비, 등락률, 거래량, 시가, 고가, 저가, PER, ROE
