# # 2020-07-29 RUDA LEE
# # SK_infosec - Cloud AI 전문가 과정 교육 
# import PyQt5.QtWidgets as qtw
# import sys
# import controller_
# import time
# import service
# from domain import MemberEntity, ClubEntity, MemberShipEntity 

# controller = controller_.DataController()

# # Qt에서 상속 받아서 MyWindow클래스를 만든다.
# class MyWindow(qtw.QMainWindow):
#     # 클래스의 초기 상태를 설정한다.
#     def __init__(self): 
#         # 상속으로 가져온 부모클래스(QMainWindow)의 초기설정을 들고온다
#         super().__init__()  # 상속으로 가져온 클래스의 초기설정 즉, QMainWindow 내부에 있는 def __init__(self): 안에 있는 내용을 가져와 그대로 사용한다는 뜻.
#         self.setupUI()

#     def setupUI(self):
#         self.setGeometry(800, 300, 350, 280)

#         groupBox = qtw.QGroupBox("커뮤니티 맴버인지 클럽 관리자인지 선택해주세요", self)
#         groupBox.move(10, 10)
#         groupBox.resize(320, 260)

#         self.button1 = qtw.QPushButton("-- 커뮤니티 맴버 --", self)
#         self.button1.move(20, 60)
#         self.button1.resize(300, 30)
#         self.button1.clicked.connect(self.Button_1_Clicked)

#         self.button2 = qtw.QPushButton("-- 클럽 관리자 --", self)
#         self.button2.move(20, 110)
#         self.button2.resize(300, 30)
#         self.button2.clicked.connect(self.Button_2_Clicked)

#         self.button3 = qtw.QPushButton("-- 프로그램 종료 --", self)
#         self.button3.move(20, 230)
#         self.button3.resize(300, 30)
#         self.button3.clicked.connect(self.Button_3_Clicked)

#     def Button_1_Clicked(self):
#         win = SubWindow_1()
#         win.text_ID = "E-mail"
#         win.initUI()
#         r = win.showModal()
#         if r:
#             email_ = win.line_1.text()
#             bm = service.CommunityService()
#             result = bm.is_exist(email_, "member_")
        
#             if not bool(result):
#                 message_display("커뮤니티에 등록되어 있지 않습니다. 맴버 등록이 필요합니다.")
#                 register_win = RegisterCommunityMember()
#                 if(register_win.showModal()):
#                     email = email_
#                     name = register_win.line_1.text()
#                     phone_number = register_win.line_2.text()
#                     birthday = register_win.line_3.text()

#                     message_ = controller.register_controller(email, MemberEntity(email, name, phone_number, birthday), "member_")
#                     message_display(message_)
      
#             else:
#                 # 맴버를 환영하는 창. 맴버 메뉴 창 띄우기
#                 member_menu = MemberMenuWindow()
#                 member_menu.Entity_ = result
#                 member_menu.setupUI()
#                 member_menu.showModal()
            

#     def Button_2_Clicked(self):
#         win = SubWindow_1()
#         win.text_ID = "clubID"
#         win.initUI()
#         r = win.showModal()
#         if r:
#             clubID_ = win.line_1.text()
#             bm = service.CommunityService()
#             result = bm.is_exist(clubID_, "club_")

#             if not bool(result):
#                 message_display("커뮤니티에 등록되어 있지 않습니다. 클럽 등록이 필요합니다.")
#                 regider_win = RegisterClub()
#                 if(regider_win.showModal()):
#                     clubID = clubID_
#                     name = regider_win.line_1.text()
#                     phone_number = regider_win.line_2.text()
#                     foundation_date = regider_win.line_3.text()
#                     address = regider_win.line_4.text()

#                     message_ = controller.register_controller(clubID, ClubEntity(clubID, name, phone_number, foundation_date, address), "club_")
#                     message_display(message_)
  
#             else:
#                 # 클럽 관리자를 환영하는 창. 클럽 메뉴 창 띄우기
#                 club_menu = ClubMenuWindow()
#                 club_menu.Entity_ = result
#                 club_menu.setupUI()
#                 club_menu.showModal()

#     def Button_3_Clicked(self):
#         # 프로그램 종료
#         sys.exit()

# class SubWindow_1(qtw.QDialog):
#     def __init__(self):
#         super().__init__()
#         self.text_ID = ""

#     def initUI(self):
#         self.setWindowTitle('ID 확인')
#         self.setGeometry(750, 330, 350, 130)

#         label1 = qtw.QLabel('{0}를 입력해 주세요 : '.format(self.text_ID), self)
#         label1.move(20, 15)
#         self.line_1 = qtw.QLineEdit(self)
#         # 아래 처럼 하면, QLineEdit에 기본 텍스트를 줄수 있다. 나중에 Update 기능을 넣을때 유용할 것.
#         # self.line_1.setText("test 값입니다.")
#         self.line_1.move(20, 35)
#         self.line_1.resize(310, 20)
        
#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(50, 90)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(200, 90)
#         self.btnCancel.resize(100, 20)
  
#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()


# class ListPrintWindow(qtw.QDialog):
#     def __init__(self):
#         super().__init__()

#     def initUI(self, table_name, ID_, key_name):

#         lists_ = controller.get_all_entity_controller(table_name, ID_, key_name)
#         self.setWindowTitle('선택된 항목에 저장된 값')
        
#         height_ = 10

#         text_ = ""
#         for value in lists_:
#             text_ += ("{0}\n".format(str(value)) )
#             height_ += 20
        
#         self.Qlabel_ = qtw.QLabel(text_, self)
#         self.Qlabel_.resize(700, height_ + 20)
#         self.Qlabel_.move(20, 20)
#         self.setGeometry(550, 330, 760, height_ + 60)

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(330, height_ + 20)
#         self.btnOK.resize(100, 20)
        
#     def onOKButtonClicked(self):
#         self.accept()
#     def showModal(self):
#         return super().exec_()


# class RegistMembership(qtw.QDialog):
#     def __init__(self):
#         super().__init__()

#     def initUI(self, table_name, ID_, key_name):

#         lists_ = controller.get_all_entity_controller(table_name, ID_, key_name)
#         self.setWindowTitle('항목에 저장된 값')
        
#         height_ = 10
#         text_ = ""
#         for value in lists_:
#             text_ += ("{0}\n".format(str(value)) )
#             height_ += 20
        
#         self.Qlabel_ = qtw.QLabel(text_, self)
#         self.Qlabel_.resize(700, height_ + 20)
#         self.Qlabel_.move(20, 20)
#         self.setGeometry(550, 330, 760, height_ + 100)

#         label1 = qtw.QLabel('맴버쉽으로 등록할 클럽ID 또는 맴버 이메일 값 : ', self)
#         label1.move(130, height_ + 20)
#         self.line_1 = qtw.QLineEdit(self)
#         self.line_1.move(400, height_ + 15)
#         self.line_1.resize(300, 20)

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(230, height_ + 50)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(360, height_ + 50)
#         self.btnCancel.resize(100, 20)

       
#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()


# class DeleteMembership(qtw.QDialog):
#     def __init__(self):
#         super().__init__()

#     def initUI(self, table_name, ID_, key_name):

#         self.setWindowTitle('항목에 저장된 값')
#         height_ = 10
#         lists_ = controller.get_all_entity_controller(table_name, ID_, key_name)

#         text_ = ""
        
#         for value in lists_:
#             text_ += ("{0}\n".format(str(value)) )
#             height_ += 20
        
#         self.Qlabel_ = qtw.QLabel(text_, self)
#         self.Qlabel_.resize(700, height_ + 20)
#         self.Qlabel_.move(20, 20)
#         self.setGeometry(550, 330, 760, height_ + 100)

#         label1 = qtw.QLabel('맴버쉽에서 탈퇴할(시킬) 멤버쉽ID를 입력하세요 : ', self)
#         label1.move(130, height_ + 20)
#         self.line_1 = qtw.QLineEdit(self)
#         self.line_1.move(400, height_ + 15)
#         self.line_1.resize(300, 20)

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(230, height_ + 50)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(360, height_ + 50)
#         self.btnCancel.resize(100, 20)

#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()

# class ModifyMember(qtw.QDialog):
#     def __init__(self):
#         super().__init__()
#     def initUI(self, Entity_member):
#         self.setWindowTitle('정보 수정')
#         self.setGeometry(750, 330, 350, 250)

#         label1 = qtw.QLabel('맴버 이름 : ', self)
#         label1.move(10, 15)
#         self.line_1 = qtw.QLineEdit(self)
#         self.line_1.move(10, 35)
#         self.line_1.resize(310, 20)
#         self.line_1.setText(Entity_member["name"])

#         label2 = qtw.QLabel('핸드폰 번호 : ', self)
#         label2.move(10, 75)
#         self.line_2 = qtw.QLineEdit(self)
#         self.line_2.move(10, 95)
#         self.line_2.resize(310, 20)
#         self.line_2.setText(Entity_member["phone_number"])

#         label3 = qtw.QLabel('생일 : ', self)
#         label3.move(10, 135)
#         self.line_3 = qtw.QLineEdit(self)
#         self.line_3.move(10, 155)
#         self.line_3.resize(310, 20)
#         self.line_3.setText(Entity_member["birthday"])

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(50, 200)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(200, 200)
#         self.btnCancel.resize(100, 20)
  
#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()

# class RegisterCommunityMember(qtw.QDialog):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle('커뮤니티 맴버 등록')
#         self.setGeometry(750, 330, 350, 250)

#         label1 = qtw.QLabel('맴버 이름 : ', self)
#         label1.move(10, 15)
#         self.line_1 = qtw.QLineEdit(self)
#         self.line_1.move(10, 35)
#         self.line_1.resize(310, 20)

#         label2 = qtw.QLabel('핸드폰 번호 : ', self)
#         label2.move(10, 75)
#         self.line_2 = qtw.QLineEdit(self)
#         self.line_2.move(10, 95)
#         self.line_2.resize(310, 20)

#         label3 = qtw.QLabel('생일 : ', self)
#         label3.move(10, 135)
#         self.line_3 = qtw.QLineEdit(self)
#         self.line_3.move(10, 155)
#         self.line_3.resize(310, 20)

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(50, 200)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(200, 200)
#         self.btnCancel.resize(100, 20)
  
#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()


# class RegisterClub(qtw.QDialog):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle('클럽 등록')
#         self.setGeometry(750, 330, 350, 310)

#         label1 = qtw.QLabel('클럽 이름 : ', self)
#         label1.move(10, 15)
#         self.line_1 = qtw.QLineEdit(self)
#         self.line_1.move(10, 35)
#         self.line_1.resize(310, 20)

#         label2 = qtw.QLabel('클럽 전화 번호 : ', self)
#         label2.move(10, 75)
#         self.line_2 = qtw.QLineEdit(self)
#         self.line_2.move(10, 95)
#         self.line_2.resize(310, 20)

#         label3 = qtw.QLabel('클럽 설립일 : ', self)
#         label3.move(10, 135)
#         self.line_3 = qtw.QLineEdit(self)
#         self.line_3.move(10, 155)
#         self.line_3.resize(310, 20)

#         label4 = qtw.QLabel('클럽 주소 : ', self)
#         label4.move(10, 195)
#         self.line_4 = qtw.QLineEdit(self)
#         self.line_4.move(10, 215)
#         self.line_4.resize(310, 20)

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(50, 260)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(200, 260)
#         self.btnCancel.resize(100, 20)
  
#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()

# class ModifyClub(qtw.QDialog):
#     def __init__(self):
#         super().__init__()
#         # self.initUI()
#     def initUI(self, Entity_club):
#         self.setWindowTitle('클럽 정보 수정')
#         self.setGeometry(750, 330, 350, 310)

#         label1 = qtw.QLabel('클럽 이름 : ', self)
#         label1.move(10, 15)
#         self.line_1 = qtw.QLineEdit(self)
#         self.line_1.move(10, 35)
#         self.line_1.resize(310, 20)
#         self.line_1.setText(Entity_club["name"])

#         label2 = qtw.QLabel('클럽 전화 번호 : ', self)
#         label2.move(10, 75)
#         self.line_2 = qtw.QLineEdit(self)
#         self.line_2.move(10, 95)
#         self.line_2.resize(310, 20)
#         self.line_2.setText(Entity_club["phone_number"])

#         label3 = qtw.QLabel('클럽 설립일 : ', self)
#         label3.move(10, 135)
#         self.line_3 = qtw.QLineEdit(self)
#         self.line_3.move(10, 155)
#         self.line_3.resize(310, 20)
#         self.line_3.setText(Entity_club["foundation_date"])

#         label4 = qtw.QLabel('클럽 주소 : ', self)
#         label4.move(10, 195)
#         self.line_4 = qtw.QLineEdit(self)
#         self.line_4.move(10, 215)
#         self.line_4.resize(310, 20)
#         self.line_4.setText(Entity_club["address"])

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(50, 260)
#         self.btnOK.resize(100, 20)

#         self.btnCancel = qtw.QPushButton("취소", self)
#         self.btnCancel.clicked.connect(self.onCancelButtonClicked)
#         self.btnCancel.move(200, 260)
#         self.btnCancel.resize(100, 20)
  
#     def onOKButtonClicked(self):
#         self.accept()
#     def onCancelButtonClicked(self):
#         self.reject()
#     def showModal(self):
#         return super().exec_()

# class MemberMenuWindow(qtw.QDialog):

#     def __init__(self): 
        
#         super().__init__()  
#         self.Entity_ = {}
#     def setupUI(self):
#         self.setGeometry(740, 280, 350, 320)

#         groupBox = qtw.QGroupBox("{0}님 환영합니다. 메뉴를 선택해주세요".format(self.Entity_["name"]), self)
#         groupBox.move(10, 10)
#         groupBox.resize(320, 310)

#         self.button1 = qtw.QPushButton("-- 클럽 맴버쉽 가입 --", self)
#         self.button1.move(20, 60)
#         self.button1.resize(300, 30)
#         self.button1.clicked.connect(self.Button_1_Clicked)

#         self.button2 = qtw.QPushButton("-- 내 정보 수정 --", self)
#         self.button2.move(20, 110)
#         self.button2.resize(300, 30)
#         self.button2.clicked.connect(self.Button_2_Clicked)

#         self.button3 = qtw.QPushButton("-- 클럽 맴버쉽 탈퇴 --", self)
#         self.button3.move(20, 160)
#         self.button3.resize(300, 30)
#         self.button3.clicked.connect(self.Button_3_Clicked)

#         self.button4 = qtw.QPushButton("-- 커뮤니티 맴버 보기 --", self)
#         self.button4.move(20, 210)
#         self.button4.resize(300, 30)
#         self.button4.clicked.connect(self.Button_4_Clicked)

#         self.button5 = qtw.QPushButton("-- 메뉴창 닫기 --", self)
#         self.button5.move(20, 260)
#         self.button5.resize(300, 30)
#         self.button5.clicked.connect(self.Button_5_Clicked)

#     def Button_1_Clicked(self):
#         # 클럽 맴버쉽에 등록하는 창 띄우기
#         win_ = RegistMembership()
#         win_.initUI("club_", '0', 0)
#         if(win_.showModal()):
#             clubID = win_.line_1.text()
#             lists_ = controller.get_all_entity_controller("membership_", "0", 0)
#             key_val = len(lists_) + 1
#             time_now_ = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#             message_ = controller.register_controller(key_val, MemberShipEntity(key_val, clubID, self.Entity_["email"], time_now_, "member"), "membership_")
#             message_display(message_)

#     def Button_2_Clicked(self):
#         # 내 정보 수정하는 창 띄우기
#         win_ = ModifyMember()
#         win_.initUI(self.Entity_)
#         if(win_.showModal()):
#             email_ = self.Entity_["email"]
#             name = win_.line_1.text()
#             phone_number = win_.line_2.text()
#             birthday = win_.line_3.text()

#             message_ = controller.update_controller(email_, MemberEntity(email_, name, phone_number, birthday), "member_")
#             message_display(message_)

#     def Button_3_Clicked(self):
#         # 클럽 맴버쉽에 탈퇴하는 창 띄우기
#         win_ = DeleteMembership()
#         win_.initUI("membership_", str(self.Entity_["email"]), "member_email")
#         if(win_.showModal()):
#             membershipID = win_.line_1.text()
#             message_ = controller.delete_controller(membershipID, "membership_")
#             message_display(message_)

#     def Button_4_Clicked(self):
#         # 커뮤니티 맴버들을 출력하는 창 띄우기
#         win_ = ListPrintWindow()
#         win_.initUI("member_", '0', 0)
#         win_.showModal()

#     def Button_5_Clicked(self):
#         # 프로그램 종료
#         self.accept()

#     def showModal(self):
#         return super().exec_()


# class ClubMenuWindow(qtw.QDialog):

#     def __init__(self): 
        
#         super().__init__() 
#         self.Entity_ = {}

#     def setupUI(self):
#         self.setGeometry(740, 280, 350, 360)

#         groupBox = qtw.QGroupBox("{0}클럽 관리자님. 메뉴를 선택해주세요".format(self.Entity_["name"]), self)
#         groupBox.move(10, 10)
#         groupBox.resize(320, 320)

#         self.button1 = qtw.QPushButton("-- 클럽에 등록되어있는 맴버쉽 --", self)
#         self.button1.move(20, 60)
#         self.button1.resize(300, 30)
#         self.button1.clicked.connect(self.Button_1_Clicked)

#         self.button2 = qtw.QPushButton("-- 클럽 정보 수정하기 --", self)
#         self.button2.move(20, 110)
#         self.button2.resize(300, 30)
#         self.button2.clicked.connect(self.Button_2_Clicked)

#         self.button3 = qtw.QPushButton("-- 맴버쉽 등록 시키기 --", self)
#         self.button3.move(20, 160)
#         self.button3.resize(300, 30)
#         self.button3.clicked.connect(self.Button_3_Clicked)

#         self.button4 = qtw.QPushButton("-- 맴버쉽 탈퇴 시키기 --", self)
#         self.button4.move(20, 210)
#         self.button4.resize(300, 30)
#         self.button4.clicked.connect(self.Button_4_Clicked)

#         self.button5 = qtw.QPushButton("-- 커뮤니티 맴버 보기 --", self)
#         self.button5.move(20, 260)
#         self.button5.resize(300, 30)
#         self.button5.clicked.connect(self.Button_5_Clicked)

#         self.button6 = qtw.QPushButton("-- 메뉴창 닫기 --", self)
#         self.button6.move(20, 310)
#         self.button6.resize(300, 30)
#         self.button6.clicked.connect(self.Button_6_Clicked)

#     def Button_1_Clicked(self):
#         # 현재 해당 클럽에 등록되어있는 맴버쉽 출력하는 창 띄우기
#         win_ = ListPrintWindow()
#         win_.initUI("membership_", self.Entity_["clubID"], "clubID")
#         win_.showModal()
#         pass

#     def Button_2_Clicked(self):
#         # 클럽 정보 수정하는 창 띄우기
#         win_ = ModifyClub()
#         win_.initUI(self.Entity_)
#         if(win_.showModal()):
#             clubID_ = self.Entity_["clubID"]
#             name = win_.line_1.text()
#             phone_number = win_.line_2.text()
#             foundation_date = win_.line_3.text()
#             address = win_.line_4.text()

#             message_ = controller.update_controller(clubID_, ClubEntity(clubID_, name, phone_number, foundation_date, address), "club_")
#             message_display(message_)

#     def Button_3_Clicked(self):
#         # 클럽에 맴버쉽을 등록시키는 창 띄우기
#         win_ = RegistMembership()
#         win_.initUI("member_", '0', 0)
#         if(win_.showModal()):
#             member_email = win_.line_1.text()
#             lists_ = controller.get_all_entity_controller("membership_", "0", 0)
#             key_val = len(lists_) + 1

#             time_now_ = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#             message_ = controller.register_controller(key_val, MemberShipEntity(key_val, self.Entity_["clubID"], member_email, time_now_, "member"), "membership_")
#             message_display(message_)
#         pass

#     def Button_4_Clicked(self):
#         # (현재 클럽에) 등록되어있는 맴버쉽 탈퇴시키는 창 띄우기
#         win_ = DeleteMembership()
#         win_.initUI("membership_", self.Entity_["clubID"], "clubID")
#         if(win_.showModal()):
#             membershipID = win_.line_1.text()
#             message_ = controller.delete_controller(membershipID, "membership_")
#             message_display(message_)
#         pass

#     def Button_5_Clicked(self):
#         # 커뮤니티 맴버들을 출력하는 창 띄우기
#         win_ = ListPrintWindow()
#         win_.initUI("member_", '0', 0)
#         win_.showModal()
#         pass

#     def Button_6_Clicked(self):
#         # 프로그램 종료
#         self.accept()

#     def showModal(self):
#         return super().exec_()


# class SubWindowMessage(qtw.QDialog):
#     def __init__(self):
#         super().__init__()
#         self.text_7 = ""
#     def initUI(self):
#         self.setWindowTitle('메세지 출력')
#         text_ = self.text_7

#         self.Qlabel_ = qtw.QLabel(text_, self)
#         self.Qlabel_.resize(480, 20)
#         self.Qlabel_.move(20, 20)
#         self.setGeometry(770, 330, 430, 90)

#         self.btnOK = qtw.QPushButton("확인", self)
#         self.btnOK.clicked.connect(self.onOKButtonClicked)
#         self.btnOK.move(150, 60)
#         self.btnOK.resize(100, 20)
        
#     def onOKButtonClicked(self):
#         self.accept()
#     def showModal(self):
#         return super().exec_()

# def message_display(message):
#     win_text = SubWindowMessage()
#     win_text.text_7 = message
#     win_text.initUI()  
#     win_text.showModal()
