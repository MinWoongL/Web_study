import requests
from bs4 import BeautifulSoup

# requests 라이브러리로 특정 HTML 페이지 요청

# HTML 요청
res = requests.get('https://finance.naver.com/sise/lastsearch2.naver')

# HTML을 parsing
soup = BeautifulSoup(res.text, "html.parser")
# title 검색
# find, find_all
lines = soup.select('.type_5 tr')

data_list = list()

index = 0

for line in lines:
    new_dict = dict()
    no = line.select('.no')
    title = line.select('.tltle')
    number = line.select('.number')

    if len(no)>0:
        index=index+1
        new_dict['no'] = no[0].get_text()
        new_dict['title'] = title[0].get_text()
        new_dict['curr_price'] = number[1].get_text()
        new_dict['전일비'] = number[2].find('span').get_text().replace('\n', '').replace('\t', '')
        data_list.append(new_dict)

print(data_list)



# 순위, 종목명, 검색비율, 현재가, 전일비, 등락률, 거래량, 시가, 고가, 저가, PER, ROE
