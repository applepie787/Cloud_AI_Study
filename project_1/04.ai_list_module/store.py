import pymysql.cursors
from domain import AIEntity
# use aidb;

# CREATE TABLE member (
# 	name varchar(20) NOT NULL,
# 	age int(3),
# 	email varchar(50) PRIMARY KEY,
# 	major varchar(20) NOT NULL
# );

# connection pool을 사용하면 여러명이서 같이 사용하는 환경에 서비스를 원활하게 할 수 있다.
class AIStore:
    connection=None

    # db 연결
    def __init__(self):
        # 인스턴스 생성 순간 실행
        # 
        AIStore.connection = pymysql.connect(host='localhost',  #url 정보
                                    user='aiadmin',
                                    password='password',
                                    db='aidb',
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)

    # db 연결 종료
    def close(self):
        AIStore.connection.close()

    def insert(self, ai_entity):
        try:
            with AIStore.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO member (name, age, email, major) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (ai_entity.name, ai_entity.age, ai_entity.email, ai_entity.major))
                AIStore.connection.commit()

    # connection is not autocommit by default. So you must commit to save
    # your changes.

        finally:
            pass  # connection pool을 사용할때 close 사용

    def select_all(self):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "SELECT * FROM member"
                cursor.execute(sql)
                result = cursor.fetchall()
                # select 문이라 commit 할 필요없다.
        finally: 
            pass
        return result

    def update(self, ai_entity):
        try:
            with AIStore.connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE member SET name = %s, age= %s, major=%s WHERE email = %s"
                cursor.execute(sql, (ai_entity.name, ai_entity.age, ai_entity.major, ai_entity.email))
                AIStore.connection.commit()
        finally:
            pass  # connection pool을 사용할때 close 사용

    def delete(self, email):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "DELETE FROM member WHERE email= %s"
                cursor.execute(sql, (email))
                AIStore.connection.commit()
        
        finally:
            pass
        

    def select_by_email(self, email):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "SELECT * FROM member WHERE email = %s"
                cursor.execute(sql, (email))
                result = cursor.fetchone() # 하나의 데이터

        finally:
            pass
        return result

test_1 = AIStore()

# test_1.insert(AIEntity("김주희", 24, "kj32h@skinfosec.co.kr", "전자공학"))
# print(test_1.select_all())

# test_1.update(AIEntity("이루다", 28, "kjh@skinfosec.co.kr", "전자공학"))
# print(test_1.select_all())

# test_1.delete("kjh@skinfosec.co.kr")

# test_1.insert(AIEntity("김주희", 24, "kjh@skinfosec.co.kr", "전자공학"))
# print(test_1.select_all())
