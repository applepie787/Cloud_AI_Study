# 2020-07-19 RUDA LEE
# SK_infosec - Cloud AI 전문가 과정 교육 

import sys
import PyQt5.QtWidgets as qtw  # from pyqt5.qtwidgets import * 로 했을시, 모듈 네임 인식이 안되어 이렇게 import 하였음.

product_list = []

# Qt에서 상속 받아서 MyWindow클래스를 만든다.
class MyWindow(qtw.QMainWindow):
    # 클래스의 초기 상태를 설정한다.
    def __init__(self): 
        # 상속으로 가져온 부모클래스(QMainWindow)의 초기설정을 들고온다
        super().__init__()  # 상속으로 가져온 클래스의 초기설정 즉, QMainWindow 내부에 있는 def __init__(self): 안에 있는 내용을 가져와 그대로 사용한다는 뜻.
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 500, 300, 190)

        groupBox = qtw.QGroupBox("원하는 기능을 클릭해주세요", self)
        groupBox.move(10, 10)
        groupBox.resize(280, 150)

        self.radio1 = qtw.QRadioButton("1 -- 제품등록", self)
        self.radio1.move(20, 30)
        self.radio1.resize(200, 20)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = qtw.QRadioButton("2 -- 제품목록", self)
        self.radio2.move(20, 50)
        self.radio2.resize(200, 20)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = qtw.QRadioButton("3 -- 제품정보 수정", self)
        self.radio3.move(20, 70)
        self.radio3.resize(200, 20)
        self.radio3.clicked.connect(self.radioButtonClicked)

        self.radio4 = qtw.QRadioButton("4 -- 제품 삭제", self)
        self.radio4.move(20, 90)
        self.radio4.resize(200, 20)
        self.radio4.clicked.connect(self.radioButtonClicked)

        self.radio5 = qtw.QRadioButton("5 -- 제품 검색", self)
        self.radio5.move(20, 110)
        self.radio5.resize(200, 20)
        self.radio5.clicked.connect(self.radioButtonClicked)

        self.radio6 = qtw.QRadioButton("6 -- 프로그램 종료", self)
        self.radio6.move(20, 130)
        self.radio6.resize(200, 20)
        self.radio6.clicked.connect(self.radioButtonClicked)

        self.Qlabel_ = qtw.QLabel("test_1", self)
        self.Qlabel_.resize(200, 200)
        self.Qlabel_.move(20, 200)


    def radioButtonClicked(self):
        if self.radio1.isChecked():
            win = SubWindow_1()  # 제품 등록 새창을 띄우는 객체를 생성.
            r = win.showModal()
            if r:
                text_1 = win.line_1.text()
                text_2 = win.line_2.text()
                text_3 = win.line_3.text()
                dict_1 = {"name" : text_1, "price" : text_2, "num" : text_3}
                product_list.append(dict_1)
                print("<상품이 성공적으로 등록되었습니다.>")
                print(text_1)
                print(text_2)
                print(text_3)

        elif self.radio2.isChecked():
            win_2 = SubWindow_2() 
            win_2.showModal()

        elif self.radio3.isChecked():
            win_3 = SubWindow_3() 
            r = win_3.showModal()
            if r:
                text_1 = win_3.line_1.text()
                text_2 = win_3.line_2.text()
                text_3 = win_3.line_3.text()
                for i, dict_ in enumerate(product_list):
                     if(dict_["name"] == text_1 or str(i + 1) == text_1):
                        dict_["price"] = text_2
                        dict_["num"] = text_3
                        print("<상품이 성공적으로 수정되었습니다.>")
                        return
                print("일치하는 상품이 없습니다")

        elif self.radio4.isChecked():
            win_4 = SubWindow_4()  
            r = win_4.showModal()
            if r:
                text_ = win_4.line_1.text()
                for i, dict_ in enumerate(product_list):
                     if(dict_["name"] == text_ or str(i + 1) == text_):
                        del product_list[i]
                        print("<상품이 성공적으로 삭제되었습니다.>")
                        return
                print("일치하는 상품이 없습니다")

        elif self.radio5.isChecked():
            win_5 = SubWindow_5()  
            r = win_5.showModal()
            text_5 = win_5.line_1.text()
            if r:
                win_6 = SubWindow_6()
                win_6.text_6 = text_5
                win_6.initUI()
                win_6.showModal()
                
        elif self.radio6.isChecked():
            print(save_list(product_list))
            sys.exit()
            

class SubWindow_1(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('제품 등록')
        self.setGeometry(800, 600, 350, 250)

        label1 = qtw.QLabel('제품 이름 : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)

        label2 = qtw.QLabel('제품 가격 : ', self)
        label2.move(10, 70)
        self.line_2 = qtw.QLineEdit(self)
        self.line_2.move(10, 90)
        self.line_2.resize(300, 20)

        label3 = qtw.QLabel('제품 번호 : ', self)
        label3.move(10, 130)
        self.line_3 = qtw.QLineEdit(self)
        self.line_3.move(10, 150)
        self.line_3.resize(300, 20)

        
        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 200)
        self.btnOK.resize(100, 20)

        self.btnCancel = qtw.QPushButton("취소", self)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.btnCancel.move(180, 200)
        self.btnCancel.resize(100, 20)
  
    def onOKButtonClicked(self):
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
    def showModal(self):
        return super().exec_()



class SubWindow_2(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('등록된 제품 목록')
        self.setGeometry(800, 600, 500, 250)
        height_ = 10

        text_ = ""
        for index_, value_ in enumerate(product_list):
            text_ += ("{0} -- 상품이름 : {1}, 가격 : {2}, 상품번호 : {3}\n".format(index_ + 1, value_["name"], value_["price"], value_["num"]))
            height_ += 20
        self.Qlabel_ = qtw.QLabel(text_, self)
        self.Qlabel_.resize(480, height_ + 20)
        self.Qlabel_.move(20, 20)
        self.setGeometry(800, 500, 450, height_ + 100)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, height_ + 40)
        self.btnOK.resize(100, 20)

       
    def onOKButtonClicked(self):
        self.accept()
    def showModal(self):
        return super().exec_()


class SubWindow_3(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('제품 정보 수정')
        self.setGeometry(800, 600, 350, 250)

        label1 = qtw.QLabel('수정 할 제품 이름 또는 번호(Key) : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)

        label2 = qtw.QLabel('수정 할 제품의 가격 : ', self)
        label2.move(10, 70)
        self.line_2 = qtw.QLineEdit(self)
        self.line_2.move(10, 90)
        self.line_2.resize(300, 20)

        label3 = qtw.QLabel('수정 할 제품 번호 : ', self)
        label3.move(10, 130)
        self.line_3 = qtw.QLineEdit(self)
        self.line_3.move(10, 150)
        self.line_3.resize(300, 20)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 200)
        self.btnOK.resize(100, 20)

        self.btnCancel = qtw.QPushButton("취소", self)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.btnCancel.move(180, 200)
        self.btnCancel.resize(100, 20)
  
    def onOKButtonClicked(self):
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
    def showModal(self):
        return super().exec_()


class SubWindow_4(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('제품 삭제')
        self.setGeometry(800, 600, 350, 250)

        label1 = qtw.QLabel('삭제할 제품 이름이나 번호 : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 200)
        self.btnOK.resize(100, 20)

        self.btnCancel = qtw.QPushButton("취소", self)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.btnCancel.move(180, 200)
        self.btnCancel.resize(100, 20)

       
    def onOKButtonClicked(self):
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
    def showModal(self):
        return super().exec_()


class SubWindow_5(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('제품 검색')
        self.setGeometry(800, 600, 350, 250)

        label1 = qtw.QLabel('검색할 제품 이름이나 번호 : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)


        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 200)
        self.btnOK.resize(100, 20)

        self.btnCancel = qtw.QPushButton("취소", self)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.btnCancel.move(180, 200)
        self.btnCancel.resize(100, 20)

       
    def onOKButtonClicked(self):
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
    def showModal(self):
        return super().exec_()


class SubWindow_6(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.text_6 = ""
    def initUI(self):
        self.setWindowTitle('목록 중 검색된 제품')
        self.setGeometry(800, 600, 500, 250)
        height_ = 10

        for index_, value_  in enumerate(product_list):
            if(value_ ["name"] == self.text_6 or str(index_ + 1) == self.text_6):
                text_ = ("{0} -- 상품이름 : {1}, 가격 : {2}, 상품번호 : {3}\n".format(index_ + 1, value_ ["name"], value_["price"], value_["num"]))
                print("<상품이 성공적으로 검색되었습니다.>")

                self.Qlabel_ = qtw.QLabel(text_, self)
                self.Qlabel_.resize(480, height_ + 20)
                self.Qlabel_.move(20, 20)
                self.setGeometry(800, 500, 450, height_ + 100)

                self.btnOK = qtw.QPushButton("확인", self)
                self.btnOK.clicked.connect(self.onOKButtonClicked)
                self.btnOK.move(30, height_ + 40)
                self.btnOK.resize(100, 20)
                return
                
        print("일치하는 상품이 없습니다")
        text_ = ("일치하는 상품이 없습니다")
        self.Qlabel_ = qtw.QLabel(text_, self)
        self.Qlabel_.resize(480, height_ + 20)
        self.Qlabel_.move(20, 20)
        self.setGeometry(800, 500, 450, height_ + 100)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, height_ + 40)
        self.btnOK.resize(100, 20)
        
    def onOKButtonClicked(self):
        self.accept()
    def showModal(self):
        return super().exec_()


def product_search(name_):
    for i, dict_ in enumerate(product_list):
        if(dict_["name"] == name_):
            print("<검색하신 상품은 " + str(i + 1) + "번 입니다.>")
            return 

def save_list(list_):
    file_obj = open("product_list.txt", "w", encoding = "utf-8")

    for dict_ in list_:
        str_ =  dict_["name"] + " " + dict_["price"] + " " + dict_["num"] + " \n"
        file_obj.write(str(str_))
    
    file_obj.close()
    return "<파일에 데이터가 저장되었습니다.>"

def read_data():
    file_obj = open("product_list.txt", "r", encoding = "utf-8")
    str_1 = file_obj.read()
    list_ = str_1.split(" ")
    i = 0
    for value_ in list_:

        if(i % 3 == 0):
            name_temp = value_.lstrip("\n")
        elif(i % 3 == 1):
            price_temp = value_.lstrip("\n")
        elif(i % 3 == 2):
            num_temp = value_.lstrip("\n")
            dict_1 = {"name" : name_temp, "price" : price_temp, "num" : num_temp}
            print(dict_1)
            product_list.append(dict_1)

        i += 1
        
    file_obj.close()


try:
    read_data()
except:
    0


if __name__ == "__main__":

    # sys,argv 값은 현재 소스코드에 대한 절대 경로를 나타낸다. 즉, 현재 파일이름.py의 절대 경로를 나타낸다.
    # QApplication클래스의 인스턴스를 생성할 떄 생성자로 이 값(절대경로)을 전달해야 한다.
    # app이라는 이름의 qt 객체 생성. 애플리케이션 내에 반드시 하나만 존재해야 한다.
    app = qtw.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    
    # app = QApplication(sys.argv)와 app.exec_()사이에 원하는 이벤트를 넣으면 된다.
    app.exec_()
    print(save_list(product_list))
 





