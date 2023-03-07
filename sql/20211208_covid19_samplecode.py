import requests
import csv

from bs4 import BeautifulSoup as bs

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson'
params ={'serviceKey' : 'ufkjV3bZypdnBV6v/GIstIO0ZoirtozNCTr6xdyNWVQ2oa8Bx/Q8f1REMcS3gkh5Kr/2N+G3aZUqwcNahnvxjw==',
         'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : '20211201', 'endCreateDt' : '20211208' }

response = requests.get(url, params=params)
#print(response.content)

# from urllib.request import Request, urlopen
# from urllib.parse import urlencode, quote
#
# import csv
#
# from bs4 import BeautifulSoup
#
# # 내 서비스키
# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson'
# skey = 'ufkjV3bZypdnBV6v%2FGIstIO0ZoirtozNCTr6xdyNWVQ2oa8Bx%2FQ8f1REMcS3gkh5Kr%2F2N%2BG3aZUqwcNahnvxjw%3D%3D'
# queryParams = '?ServiceKey=' + skey + '&' + \
#             urlencode({ quote('pageNo') : '1',
#                         quote('numOfRows') : '100',
#                         quote('startCreateDt') : '20211102',
#                         quote('endCreateDt') : '20211202' })
#
# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print(response_body)
content = response.content
soup = bs(content, 'html.parser')
print(soup)
createDt = soup.find('gubun')
print(createDt)

items = soup.select('item')
print(len(items))


its_list = list()

for item in items:
    i_list = list()
    i_dict = dict()
    confcase = item.find('confcase').text
    death = item.find('death').get_text()
    gubun = item.find('gubun').get_text()
    createDt = item.find('createdt').get_text()
    i_list.append(createDt)
    i_list.append(gubun)
    i_list.append(confcase)
    i_list.append(death)

    i_dict['createdt'] = createDt
    i_dict['gubun'] = gubun
    i_dict['confcase'] = confcase
    i_dict['death'] = death

    print(i_list)
    print(i_dict)
    its_list.append(i_dict)
print(its_list)

# with open('covid19.csv', 'w', newline='') as csvfile:
#     fieldnames = ['createDt', 'gubun','confcase', 'death']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for data in its_list:
#         writer.writerow({'createDt': data['createdt'], 'gubun': data['gubun'],'confcase':data['confcase'], 'death':data['death'],})
