import pymysql.cursors
from domain import Entity_1
# use aidb;

# CREATE TABLE product (
# 	product_name varchar(20) NOT NULL,
# 	product_code int(5) PRIMARY KEY,
# 	product_description varchar(50)
# );

# connection pool을 사용하면 여러명이서 같이 사용하는 환경에 서비스를 원활하게 할 수 있다.
class ProductStore:
    connection=None

    # db 연결
    def __init__(self):
        # 인스턴스 생성 순간 실행
        # 
        ProductStore.connection = pymysql.connect(host='localhost',  #url 정보
                                    user='aiadmin',  # product 정보로 수정 예정.
                                    password='password',
                                    db='aidb',       # product 정보로 수정 예정.
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)

    # db 연결 종료
    def close(self):
        ProductStore.connection.close()

    def insert(self, entity):
        try:
            with ProductStore.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO product (product_name, product_code, product_description) VALUES (%s, %s, %s)"
                cursor.execute(sql, (entity.product_name, entity.product_code, entity.product_description))
                ProductStore.connection.commit()

    # connection is not autocommit by default. So you must commit to save
    # your changes.

        finally:
            pass  # connection pool을 사용할때 close 사용

    def select_all(self):
        try:
            with ProductStore.connection.cursor() as cursor:
                sql = "SELECT * FROM product"
                cursor.execute(sql)
                result = cursor.fetchall()
                # select 문이라 commit 할 필요없다.
        finally: 
            pass
        return result

    def update(self, entity):
        try:
            with ProductStore.connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE product SET product_name = %s, product_description = %s WHERE product_code = %s"
                cursor.execute(sql, (entity.product_name, entity.product_description, entity.product_code))
                ProductStore.connection.commit()
        finally:
            pass  # connection pool을 사용할때 close 사용

    def delete(self, product_code):
        try:
            with ProductStore.connection.cursor() as cursor:
                sql = "DELETE FROM product WHERE product_code = %s"
                cursor.execute(sql, (product_code))
                ProductStore.connection.commit()
        
        finally:
            pass
        

    def select_by_product_code(self, product_code):
        try:
            with ProductStore.connection.cursor() as cursor:
                sql = "SELECT * FROM product WHERE product_code = %s"
                cursor.execute(sql, (product_code))
                result = cursor.fetchone() # 하나의 데이터

        finally:
            pass
        return result

# test_1 = ProductStore()

# test_1.insert(Entity_1("무선이어폰", 123, "고품질의무선이어폰입니다"))
# test_1.insert(Entity_1("무선이어폰2", 123434, "두번째이어폰입니다"))
# test_1.insert(Entity_1("무선이어폰3", 12342, "세번째이어폰입니다"))
# test_1.insert(Entity_1("무선이어폰4", 12342323, "4"))
# test_1.insert(Entity_1("무선이어폰5", 12345, "5"))
# print(test_1.select_all())

# test_1.update(AIEntity("이루다", 28, "kjh@skinfosec.co.kr", "전자공학"))
# print(test_1.select_all())

# test_1.delete("kjh@skinfosec.co.kr")

# test_1.insert(AIEntity("김주희", 24, "kjh@skinfosec.co.kr", "전자공학"))
# print(test_1.select_all())
