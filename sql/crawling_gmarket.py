import requests
from bs4 import BeautifulSoup
import pymysql
db = pymysql.connect(
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='1111', 
    db='gmarket',
    charset='utf8')
cursor = db.cursor()

def save_data(item_info):
    print (item_info)
    sql = """SELECT COUNT(*) FROM items WHERE item_code = '""" + item_info['item_code'] + """';"""
    cursor.execute(sql)
    result = cursor.fetchone()
    print (result[0])
    if result[0] == 0:
        sql = """INSERT INTO items VALUES('""" + item_info['item_code'] + """',
        '""" + item_info['title'] + """', 
        """ + str(item_info['ori_price']) + """, 
        """ + str(item_info['dis_price']) + """, 
        """ + str(item_info['discount_percent']) + """, 
        '""" + item_info['provider'] + """')"""
        cursor.execute(sql)
    
    sql = """INSERT INTO ranking (main_category, sub_category, item_ranking, item_code) VALUES('""" + item_info['category_name'] + """',
    '""" + item_info['sub_category_name'] + """', 
    '""" + str(item_info['ranking']) + """', 
    '""" + item_info['item_code'] + """')"""     
    cursor.execute(sql)


def get_items(html, category_name, sub_category_name):
    items_list = list()
    bestlists = html.select('div.best-list')
    items = bestlists[1].select('li') # 3개의 best-list 클래스 태그 중 두번째 100개의 상품을 포함한 내용만 가져오기 위함
    print(len(items))
    #index = 0

    for index, bestlist in enumerate(items):
    #    index = index+1
        item_dict = {}
        #print(bestlist)
        name = bestlist.select_one('a.itemname')
        ori_price = bestlist.select_one('div.o-price')
        dis_price = bestlist.select_one('div.s-price strong span')
        discount_percent = bestlist.select_one('div.s-price em')
        item_link = bestlist.select_one('.thumb a')['href']

        if ori_price == None :  # 할인가만 있고 ori 가 없는 경우
            ori_price = dis_price

        if discount_percent == None: # 할인율이 없는 경우
            discount_percent = 0
        else :
            discount_percent = discount_percent.get_text().replace('%','')

        item_dict['ranking']=index+1
        item_dict['main']=category_name
        item_dict['sub']=sub_category_name
        item_dict['name']=name.get_text()
        item_dict['ori']=ori_price.get_text().replace(',','').replace('원','')
        item_dict['dis']=dis_price.get_text().replace(',','').replace('원','')
        item_dict['per']=discount_percent
        item_dict['item_code']=item_link.split('=')[1].split('&')[0]

        prov_res = requests.get(item_link)
        prov_soup = BeautifulSoup(prov_res.content, "html.parser")

        provider = prov_soup.select_one('a.link__seller')
        
        if provider == None:
            item_dict['provider']=' '
        else:
            item_dict['provider']=provider.get_text()    #print(index+1, item_dict)
        
        save_data(item_dict)

# 각 메인카테고리별 링크를 이용하여 
def get_category(category_link, category_name):
    print (category_link, category_name)
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')

    get_items(soup, category_name, "ALL")
    
    sub_categories = soup.select('div.navi.group ul li > a')  # navi.group ul li a  로 주면 유아동/출산에서 오류 발생
                                                        # related 관련상품군도 a 태그라서 그것을 제외하기 위해 
                                                        # li a  에서 li > a 로 변경
    for sub_category in sub_categories:               
        res = requests.get('http://corners.gmarket.co.kr/' + sub_category['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        get_items(soup, category_name, sub_category.get_text()) 

# main 시작 지점

res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
soup = BeautifulSoup(res.content, 'html.parser')

# 메인 카테고리 가져오기
categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    get_category('http://corners.gmarket.co.kr/' + category['href'], category.get_text())


db.commit()
db.close()

 






