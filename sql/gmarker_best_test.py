import requests
from bs4 import BeautifulSoup
from requests.api import request

import pymysql.cursors

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='zxcv1234',
    db='bestproducts',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)


# DB Insert
def save_data(rankingData, itemsData):
    print(itemsData)
    print(rankingData)
    # items 먼저 입력 (FK 문제)
    cursor = db.cursor()
    # items 테이블에 같은 item_code가 등록되어 있는지 검사
    sql = "select count(*) from items where item_code = '{}'".format(itemsData['item_code'])
    cursor.execute(sql)
    result = cursor.fetchone()
    # items 테이블에 item_code 등록
    if result['count(*)'] == 0:
        sql = "insert into items(item_code, title, ori_price, dis_price, discount_percent, provider, url, img) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            itemsData['item_code'], itemsData['title'], itemsData['ori_price'], itemsData['dis_price'],
            itemsData['discount_percent'], itemsData['provider'], itemsData['url'], itemsData['img'])

        resultByItems = cursor.execute(sql)
        if resultByItems == 1:
            db.commit()
            print('Success Items')
    # ranking 테이블에 등록
    sql = "insert into ranking(main_category, sub_category, item_ranking, item_code) values('{}','{}','{}','{}')".format(
        rankingData['main_category'], rankingData['sub_category'], rankingData['item_ranking'],
        rankingData['item_code'])
    resultByRanking = cursor.execute(sql)
    if resultByRanking == 1:
        db.commit()
        print('Success Ranking')

    return 0


# Get Provider
def get_provider(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    if soup.select_one('a.link__seller') != None:
        return soup.select_one('a.link__seller').get_text()
    else:
        return ''


# BEST ITEM
def get_bestItem(url, mainCategory, subCategory):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    # datas = soup.select('div.best-list ul li a.itemname')
    datas = soup.select('div.best-list ul:not(.plus) li')
    for item in datas:
        ranking_dict = dict()
        items_dict = dict()
        if item.select_one('a.itemname').get_text() != "":
            # null check
            pointOPrice = item.select_one('div.o-price span')
            pointSPrice = item.select_one('div.s-price > span')

            # get data
            URL = item.select_one('a.itemname')['href']
            item_ranking = item.select_one('p').get_text()
            item_img = item.select_one('div.thumb a img.lazy')['data-original']
            item_code = item.select_one('a.itemname')['href'].split('=')[1].replace('&ver', '')
            title = item.select_one('a.itemname').get_text()
            dis_price = item.select_one('div.s-price strong span span').get_text().replace('원', '').replace(',', '')
            provider = get_provider(item.select_one('a.itemname')['href'])

            # table ranking
            # main_category, sub_category, item_ranking, item_code
            ranking_dict['main_category'] = mainCategory
            ranking_dict['sub_category'] = subCategory
            ranking_dict['item_ranking'] = item_ranking
            ranking_dict['item_code'] = item_code
            # table items
            # item_code, title, ori_price, dis_price, discount_percent, provider, url, img
            items_dict['item_code'] = item_code
            items_dict['title'] = title
            items_dict['dis_price'] = dis_price
            items_dict['provider'] = provider
            items_dict['url'] = URL
            items_dict['img'] = item_img
            if pointOPrice != None:
                items_dict['ori_price'] = item.select_one('div.o-price span span').get_text().replace('원', '').replace(
                    ',', '')
            else:
                items_dict['ori_price'] = 0
            if pointSPrice != None:
                items_dict['discount_percent'] = item.select_one('div.s-price span em').get_text().replace('%', '')
            else:
                items_dict['discount_percent'] = 0
            # print(ranking_dict)
            # print(items_dict)
            save_data(ranking_dict, items_dict)

    return return_data


# Sub Category
def get_subCategory(url, mainCategory):
    print(url, category)
    if url == 'http://corners.gmarket.co.kr/Bestsellers':
        get_bestItem(url, mainCategory, mainCategory)
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas1 = soup.select('div.navi ul li a')
    for item in datas1:
        # print(item.get_text())
        # print('------------')
        get_bestItem('http://corners.gmarket.co.kr' + item['href'], mainCategory, item.get_text())
        return_data.append(item.get_text())
    return return_data


# Main Category
res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
soup = BeautifulSoup(res.content, 'html.parser')

categories = soup.select('div.gbest-cate ul.by-group li a')

for category in categories:
    # print(category.get_text())
    get_subCategory('http://corners.gmarket.co.kr' + category['href'], category.get_text())
