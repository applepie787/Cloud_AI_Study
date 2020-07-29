# 2020-07-29 RUDA LEE
# SK_infosec - Cloud AI 전문가 과정 교육 
import sys
import GUI_windows
import PyQt5.QtWidgets as qtw  # from pyqt5.qtwidgets import * 로 했을시, 모듈 네임 인식이 안되어 이렇게 import 하였음.

# host='localhost' url 정보
# user='aiadmin'
# password='password'
# db='module_db'
# docker에서 mysql 실행. port 3306
# 테이블 선언은 아래와 같이 수행 됨.
"""
use module_db; 
 
CREATE TABLE member_ (
 	email varchar(50) PRIMARY KEY,
 	name varchar(30),
 	phone_number varchar(20),
 	birthday varchar(20)
 );
ALTER TABLE member_ convert to character set UTF8;

CREATE TABLE club_ (
 	clubID varchar(20) PRIMARY KEY,
 	name varchar(50),
 	phone_number varchar(20),
 	foundation_date varchar(20),
 	address varchar(50)
 );
ALTER TABLE club_ convert to character set UTF8;
 
CREATE TABLE membership_ (
	membershipID varchar(20) PRIMARY KEY,
 	clubID varchar(20),
 	member_email varchar(50),
 	join_date varchar(20),
 	role_in_club varchar(20)
 );
ALTER TABLE membership_ convert to character set UTF8;
 """
if __name__ == "__main__":
    # sys,argv 값은 현재 소스코드에 대한 절대 경로를 나타낸다. 즉, 현재 파일이름.py의 절대 경로를 나타낸다.
    # QApplication클래스의 인스턴스를 생성할 떄 생성자로 이 값(절대경로)을 전달해야 한다.
    # app이라는 이름의 qt 객체 생성. 애플리케이션 내에 반드시 하나만 존재해야 한다.

    app = qtw.QApplication(sys.argv)
    mywindow = GUI_windows.MyWindow()
    mywindow.show()

    app.exec_()
 





