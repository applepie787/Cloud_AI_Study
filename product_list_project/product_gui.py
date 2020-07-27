# 2020-07-19 RUDA LEE
# SK_infosec - Cloud AI 전문가 과정 교육 

import sys
import controller_
import product_windows
from domain import Entity_1
import PyQt5.QtWidgets as qtw  # from pyqt5.qtwidgets import * 로 했을시, 모듈 네임 인식이 안되어 이렇게 import 하였음.

controller = controller_.ProductController()
product_list = []

# Qt에서 상속 받아서 MyWindow클래스를 만든다.
class MyWindow(qtw.QMainWindow):
    # 클래스의 초기 상태를 설정한다.
    def __init__(self): 
        # 상속으로 가져온 부모클래스(QMainWindow)의 초기설정을 들고온다
        super().__init__()  # 상속으로 가져온 클래스의 초기설정 즉, QMainWindow 내부에 있는 def __init__(self): 안에 있는 내용을 가져와 그대로 사용한다는 뜻.
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 300, 240, 280)

        groupBox = qtw.QGroupBox("원하는 기능을 클릭해주세요", self)
        groupBox.move(10, 10)
        groupBox.resize(220, 260)

        self.radio1 = qtw.QPushButton("-- 제품등록 --", self)
        self.radio1.move(20, 30)
        self.radio1.resize(200, 30)
        self.radio1.clicked.connect(self.Button_1_Clicked)

        self.radio2 = qtw.QPushButton("-- 제품목록 --", self)
        self.radio2.move(20, 70)
        self.radio2.resize(200, 30)
        self.radio2.clicked.connect(self.Button_2_Clicked)

        self.radio3 = qtw.QPushButton("-- 제품정보 수정 --", self)
        self.radio3.move(20, 110)
        self.radio3.resize(200, 30)
        self.radio3.clicked.connect(self.Button_3_Clicked)

        self.radio4 = qtw.QPushButton("-- 제품 삭제 --", self)
        self.radio4.move(20, 150)
        self.radio4.resize(200, 30)
        self.radio4.clicked.connect(self.Button_4_Clicked)

        self.radio5 = qtw.QPushButton("-- 제품 검색 --", self)
        self.radio5.move(20, 190)
        self.radio5.resize(200, 30)
        self.radio5.clicked.connect(self.Button_5_Clicked)

        self.radio6 = qtw.QPushButton("-- 프로그램 종료 --", self)
        self.radio6.move(20, 230)
        self.radio6.resize(200, 30)
        self.radio6.clicked.connect(self.Button_6_Clicked)

    def Button_1_Clicked(self):
        win = product_windows.SubWindow_1()
        r = win.showModal()
        if r:
            product_name = win.line_1.text()
            product_code = win.line_2.text()
            product_description = win.line_3.text()
            message_ = controller.register_controller(Entity_1(product_name, product_code, product_description))
            product_windows.message_display(message_)

    def Button_2_Clicked(self):
        win_2 = product_windows.SubWindow_2() 
        win_2.showModal()

    def Button_3_Clicked(self):
        win_3 = product_windows.SubWindow_3()
        r = win_3.showModal()
        if r:
            product_code = win_3.line_1.text()  # line_1에서 제품의 코드 값을 받는다
            product_name = win_3.line_2.text()  # line_2에서 제품의 이름 값을 받는다
            product_description = win_3.line_3.text()
            message_ = controller.update_controller(Entity_1(product_name, product_code, product_description))
            product_windows.message_display(message_)

    def Button_4_Clicked(self):
        win_4 = product_windows.SubWindow_4() 
        r = win_4.showModal()
        if r:
            product_code = win_4.line_1.text()
            message_ = controller.delete_controller(product_code)
            product_windows.message_display(message_)

    def Button_5_Clicked(self):
        win_5 = product_windows.SubWindow_5()  
        r = win_5.showModal()
        product_code = win_5.line_1.text()
        if r:
            win_6 = product_windows.SubWindow_6()
            win_6.text_6 = product_code
            win_6.initUI()
            win_6.showModal()

    def Button_6_Clicked(self):
        sys.exit()

if __name__ == "__main__":

    # sys,argv 값은 현재 소스코드에 대한 절대 경로를 나타낸다. 즉, 현재 파일이름.py의 절대 경로를 나타낸다.
    # QApplication클래스의 인스턴스를 생성할 떄 생성자로 이 값(절대경로)을 전달해야 한다.
    # app이라는 이름의 qt 객체 생성. 애플리케이션 내에 반드시 하나만 존재해야 한다.
    app = qtw.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()

    app.exec_()
 





