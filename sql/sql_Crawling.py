import requests
from bs4 import BeautifulSoup

# 1) requests 라이브러리를 활용한 HTML 페이지 요청
# 2) req 객체에 HTML 데이터가 저장되고, req.content 로 데이터를 추출할 수 있음

# naver.com 접속해서 enter 치기
res = requests.get('http://www.naver.com')

# HTML 에 있는 코드 가져와서 parsing
soup = BeautifulSoup(res.text, "html.parser")

#3) HTML 페이지 파싱 - BeautifulSoup(HTML데이터, 파싱방법)
soup = BeautifulSoup(res.text, "html.parser")

#4) 필요한 데이터 검색 - ex
title = soup.find('title')

#5) 필요한 데이터 추출
print(title.get_text())