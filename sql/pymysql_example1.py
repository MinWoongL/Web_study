import pymysql
import pymysql.cursors

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user='root',
    passwd='disappear1!',
    db='market',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

sql = """
    select * from goods
 """
cursor.execute(sql)
result = cursor.fetchmany(2)
print(result)
for item in result:
    print(item)

# for index in range(6,10):
#     print(index)
#     id = index
#     goodsno = 1290
#     category1 = index``
#     category1_name = "소세지" + str(category1)
#     sql = "insert into detailgoods values({},{},{},'{}');".format(id,goodsno, category1, category1_name)
#     print(sql)
#     cursor.execute(sql)

db.commit()
db.close()
