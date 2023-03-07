import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# auth.json 에 인증 정보 저장
# firebase 프로젝트에 생성한 realtime database의 url 가져오기
cred = credentials.Certificate("database-test-deee5-firebase-auth.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://database-test-deee5-default-rtdb.firebaseio.com/'
})

# dbref=db.reference()
# data={'모델':'bbb', 'color': 'yellow', '제조사':'mscompany'}
# dbref.child("car").child('truck').push(data) # push 를 이용하면 시스템에서 자동생성하는 키 아래에 묶어서 data 를 저장함

# reference 아래에 data 를 저장함, 리스트를 이용하면 key 가 0,1,2 로 지정됨
# dbref=db.reference('부서/인사팀')
# data={'직원':['홍길동','이이경','아이유']}
# dbref.update(data)

# 기본위치에 저장되어 있는 값을 모두 조회하는 방법
dbref=db.reference()
print(dbref.get())
#
# # reference 를 이용하여 저장되어 있는 값을 조회하는 방법
dbref=db.reference('부서/인사팀')
print(dbref.get())
#
dbref=db.reference('부서/인사팀/직원/0')
print(dbref.get())