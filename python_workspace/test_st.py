import student_test


ai_list = [ student_test.Student_("ai01", "김주희", "전자공학"),
            student_test.Student_("ai01", "정종우", "컴공"),

            student_test.Teacher_("T001", "최재호", "파이썬"),
            student_test.Employee_("e001", "이준용", "교육")
 ]
if(ai_list[0] == ai_list[1]):
    print("존재하는 데이터")
else:
    print("등록가능한 데이터")

# ai01 = student_test.Student_("ai01", "김주희", "전자공학")
# ai01.student_info()

# t001 = student_test.Teacher_("T001", "최재호", "파이썬")
# t001.teacher_info()

# e001 = student_test.Employee_("e001", "이준용", "교육")
# e001.employee_info()


for ai in ai_list:
    if(isinstance(ai, student_test.Student_)):
        ai.student_info()
    elif(isinstance(ai, student_test.Teacher_)):
        ai.teacher_info()
    elif(isinstance(ai, student_test.Employee_)):
        ai.info()
    else:
        print("타입이 잘못되었습니다")
