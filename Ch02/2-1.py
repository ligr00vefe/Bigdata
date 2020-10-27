"""
날짜 : 2020/07/16
이름 : 권기민
내용 : 파이썬 MongoDB 실습하기
"""

from pymongo import MongoClient as mongo
from datetime import datetime as dt

# mongodb 접속
conn = mongo('mongodb://kkm:1234@192.168.100.101:27017')

# db 선택
db = conn.get_database('test')

# 컬렉션 조회
collections = db.list_collection_names()
print(collections)

# 컬렉션(테이블) 선택
people = [{'uid':'A103', 'name':'강감찬', 'hp':'010-1234-1113', 'pos':'부장', 'dep':103, 'rdate':dt.now()},
          {'uid':'A104', 'name':'장보고', 'hp':'010-1234-1114', 'pos':'과장', 'dep':104, 'rdate':dt.now()},
          {'uid':'A105', 'name':'이순신', 'hp':'010-1234-1115', 'pos':'대리', 'dep':105, 'rdate':dt.now()}]

collection = db.get_collection('member')
collection.insert_one({'uid':'A101', 'name':'김유신', 'hp':'010-1234-1111', 'pos':'과장', 'dep':101, 'rdate':dt.now()})
collection.insert_one({'uid':'A102', 'name':'김춘추', 'hp':'010-1234-1112', 'pos':'신입', 'dep':102, 'rdate':dt.now()})
collection.insert_many(people)

print('데이터 Insert 완료...')