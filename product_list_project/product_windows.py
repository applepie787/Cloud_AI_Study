import PyQt5.QtWidgets as qtw
import sys
import controller_

controller = controller_.ProductController()

class SubWindow_1(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('제품 등록')
        self.setGeometry(750, 330, 350, 250)

        label1 = qtw.QLabel('제품 이름 : ', self)
        label1.move(20, 15)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(20, 35)
        self.line_1.resize(300, 20)

        label2 = qtw.QLabel('제품 코드 : ', self)
        label2.move(20, 75)
        self.line_2 = qtw.QLineEdit(self)
        self.line_2.move(20, 95)
        self.line_2.resize(300, 20)

        label3 = qtw.QLabel('제품 설명 : ', self)
        label3.move(20, 135)
        self.line_3 = qtw.QLineEdit(self)
        self.line_3.move(20, 155)
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
        lists_ = controller.get_all_entity_controller()

        self.initUI(lists_)

    def initUI(self, product_list):
        self.setWindowTitle('등록된 제품 목록')
        
        height_ = 10

        text_ = ""
        for value in product_list:
            text_ += ("{0}\n".format(str(value)) )
            height_ += 20
        
        self.Qlabel_ = qtw.QLabel(text_, self)
        self.Qlabel_.resize(700, height_ + 20)
        self.Qlabel_.move(20, 20)
        self.setGeometry(550, 330, 760, height_ + 60)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(330, height_ + 20)
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
        self.setGeometry(750, 330, 350, 250)

        label1 = qtw.QLabel('수정 할 제품의 코드 : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)

        label2 = qtw.QLabel('수정 할 제품의 이름 : ', self)
        label2.move(10, 70)
        self.line_2 = qtw.QLineEdit(self)
        self.line_2.move(10, 90)
        self.line_2.resize(300, 20)

        label3 = qtw.QLabel('수정 할 제품의 설명 : ', self)
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
        self.setGeometry(750, 330, 340, 110)

        label1 = qtw.QLabel('삭제할 제품의 코드 : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 80)
        self.btnOK.resize(100, 20)

        self.btnCancel = qtw.QPushButton("취소", self)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.btnCancel.move(180, 80)
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
        self.setGeometry(750, 330, 340, 110)

        label1 = qtw.QLabel('검색할 제품의 코드 : ', self)
        label1.move(10, 10)
        self.line_1 = qtw.QLineEdit(self)
        self.line_1.move(10, 30)
        self.line_1.resize(300, 20)


        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 80)
        self.btnOK.resize(100, 20)

        self.btnCancel = qtw.QPushButton("취소", self)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.btnCancel.move(180, 80)
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
        product_entity = controller.get_entity_controller(self.text_6)
        text_ = ("상세정보 : {0}".format(product_entity))

        self.Qlabel_ = qtw.QLabel(text_, self)
        self.Qlabel_.resize(480, 20)
        self.Qlabel_.move(20, 20)
        self.setGeometry(770, 330, 460, 90)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 60)
        self.btnOK.resize(100, 20)
        
    def onOKButtonClicked(self):
        self.accept()
    def showModal(self):
        return super().exec_()


class SubWindow_7(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.text_7 = ""
    def initUI(self):
        self.setWindowTitle('메세지 출력')
        text_ = self.text_7

        self.Qlabel_ = qtw.QLabel(text_, self)
        self.Qlabel_.resize(480, 20)
        self.Qlabel_.move(20, 20)
        self.setGeometry(770, 330, 460, 90)

        self.btnOK = qtw.QPushButton("확인", self)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnOK.move(30, 60)
        self.btnOK.resize(100, 20)
        
    def onOKButtonClicked(self):
        self.accept()
    def showModal(self):
        return super().exec_()

def message_display(message):
    win_text = SubWindow_7()
    win_text.text_7 = message
    win_text.initUI()  
    win_text.showModal()
