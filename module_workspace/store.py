import pymysql.cursors

class DBStore:
    connection=None
    def __init__(self):
        # 인스턴스 생성 순간 실행
        # 
        DBStore.connection = pymysql.connect(host='localhost',  #url 정보
                                    user='aiadmin',  # product 정보로 수정 예정.
                                    password='password',
                                    db='module_db',       # product 정보로 수정 예정.
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)

    # db 연결 종료
    def close(self):
        DBStore.connection.close()

    def insert(self, entity, table_name):
        with DBStore.connection.cursor() as cursor:

            if(table_name == "club_"):
                sql = "INSERT INTO club_ (clubID, name, phone_number, foundation_date, address) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (entity.clubID, entity.name, entity.phone_number, entity.foundation_date, entity.address))
            elif(table_name == "member_"):
                sql = "INSERT INTO member_ (email, name, phone_number, birthday) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (entity.email, entity.name, entity.phone_number, entity.birthday))
            elif(table_name == "membership_"):
                sql = "INSERT INTO membership_ (membershipID, clubID, member_email, join_date, role_in_club) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (entity.membershipID, entity.clubID, entity.member_email, entity.join_date, entity.role_in_club))

            DBStore.connection.commit()

    def select_records(self, table_name, ID_, key_name):

        with DBStore.connection.cursor() as cursor:
            if(ID_ == '0'):
                sql = "SELECT * FROM {0}".format(table_name)
                cursor.execute(sql)
            elif(table_name == 'membership_'):
                sql = "SELECT * FROM {0} WHERE {1} = %s".format(table_name, key_name)
                cursor.execute(sql, (ID_))
 
            result = cursor.fetchall()
        return result

    def update(self, entity, table_name):

         with DBStore.connection.cursor() as cursor:
            if(table_name == "club_"):
                sql = "UPDATE club_ SET name = %s, phone_number = %s, foundation_date = %s, address = %s WHERE clubID = %s"
                cursor.execute(sql, (entity.name, entity.phone_number, entity.foundation_date, entity.address, entity.clubID))
            elif(table_name == "member_"):
                sql = "UPDATE member_ SET name = %s, phone_number = %s, birthday = %s WHERE email = %s"
                cursor.execute(sql, (entity.name, entity.phone_number, entity.birthday, entity.email))
            elif(table_name == "membership_"):
                sql = "UPDATE membership_ SET clubID = %s, member_email = %s, join_date = %s, role_in_club = %s WHERE membershipID = %s"
                cursor.execute(sql, (entity.clubID, entity.member_email, entity.join_date, entity.role_in_club, entity.membershipID))

            DBStore.connection.commit()

    def delete(self, IDcode, table_name):

         with DBStore.connection.cursor() as cursor:
            if(table_name == "club_"):
                sql = "DELETE FROM club_ WHERE clubID = %s"
            elif(table_name == "member_"):
                sql = "DELETE FROM member_ WHERE email = %s"
            elif(table_name == "membership_"):
                sql = "DELETE FROM membership_ WHERE membershipID = %s"

            cursor.execute(sql, (IDcode))
            DBStore.connection.commit()

    def select_by_product_code(self, IDcode, table_name):

        with DBStore.connection.cursor() as cursor:
            if(table_name == "club_"):
                sql = "SELECT * FROM club_ WHERE clubID = %s"
            elif(table_name == "member_"):
                sql = "SELECT * FROM member_ WHERE email = %s"
            elif(table_name == "membership_"):
                sql = "SELECT * FROM membership_ WHERE membershipID = %s"


            cursor.execute(sql, (IDcode))
            result = cursor.fetchone() # 하나의 데이터

        return result

